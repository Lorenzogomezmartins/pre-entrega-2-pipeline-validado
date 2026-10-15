
import logging
import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from schemas import ExtraccionTecnica


load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


api_key = os.getenv("GOOGLE_API_KEY")
model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not api_key:
    raise ValueError(
        "Falta GOOGLE_API_KEY. Configurala en el archivo .env."
    )


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Sos un analista especializado en sistemas y arquitectura
            de software.

            Analizá el texto técnico proporcionado e identificá:
            - Las tecnologías mencionadas explícitamente.
            - El nivel de criticidad técnica.
            - Un resumen técnico breve y preciso.

            Reglas:
            - La criticidad debe ser baja, media o alta.
            - Considerá errores graves, caídas y pérdida de datos
              como señales de alta criticidad.
            - No inventes tecnologías que no aparezcan en el texto.
            - Si el texto no permite determinar una tecnología,
              indicá que no se puede realizar una extracción fiable.
            - El resumen debe describir únicamente información
              respaldada por el texto.
            - Respetá estrictamente el esquema de salida solicitado.
            """,
        ),
        (
            "human",
            "Analizá el siguiente texto técnico:\n\n{texto}",
        ),
    ]
)


model = ChatGoogleGenerativeAI(
    model=model_name,
    google_api_key=api_key,
    temperature=0,
    max_retries=0,
)

structured_model = model.with_structured_output(
    ExtraccionTecnica,
)

chain = (prompt | structured_model).with_retry(
    retry_if_exception_type=(Exception,),
    stop_after_attempt=3,
    wait_exponential_jitter=True,
)


async def process_text(text: str) -> ExtraccionTecnica:
    if not text or not text.strip():
        raise ValueError("El texto de entrada no puede estar vacío.")

    logger.info("Iniciando procesamiento del texto técnico.")

    try:
        resultado = await chain.ainvoke({"texto": text})

        # Comprobación explícita del tipo y del esquema de salida.
        resultado = ExtraccionTecnica.model_validate(resultado)

        logger.info(
            "Validación exitosa. Tecnologías identificadas: %s",
            len(resultado.tecnologias),
        )

        return resultado

    except Exception:
        logger.exception(
            "Falló el procesamiento tras los intentos configurados."
        )
        raise

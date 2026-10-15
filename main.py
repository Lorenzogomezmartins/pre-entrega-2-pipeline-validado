
import asyncio
import json
import logging

from chain import process_text


logging.basicConfig(level=logging.INFO)


async def main() -> None:
    texto = """
    La API desarrollada con FastAPI utiliza Redis como caché
    y PostgreSQL para persistir los datos.
    Se detectaron conexiones concurrentes que provocan
    tiempos de respuesta elevados y errores 503.
    """

    try:
        resultado = await process_text(texto)

        print("\n--- RESULTADO VALIDADO ---")
        print(
            json.dumps(
                resultado.model_dump(mode="json"),
                indent=2,
                ensure_ascii=False,
            )
        )

    except Exception as error:
        print(f"\nNo se pudo procesar el texto: {error}")


if __name__ == "__main__":
    asyncio.run(main())

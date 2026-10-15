# Pre-entrega 2: Pipeline de procesamiento validado

Pipeline asíncrono de extracción y validación de información técnica desarrollado con Python, LangChain, Google Gemini y Pydantic.

## Funcionalidades

- Extracción de tecnologías desde texto técnico.
- Clasificación del nivel de criticidad: baja, media o alta.
- Generación de un resumen técnico.
- Validación de la salida mediante Pydantic.
- Composición de cadenas LCEL con `ChatPromptTemplate`.
- Generación de salida estructurada mediante `with_structured_output()`.
- Reintentos automáticos ante errores mediante `with_retry()`.
- Ejecución asíncrona con `ainvoke()`.
- Registro de eventos y errores mediante logs.

## Requisitos

- Python 3.12 o compatible con las dependencias utilizadas.
- Una API key de Google AI Studio con acceso a un modelo compatible.
- Conexión a Internet.

## Instalación

### 1. Clonar el repositorio

```powershell
git clone https://github.com/Lorenzogomezmartins/CoderHouse-ia-Engineering.git
cd CoderHouse-ia-Engineering
```

Si descargaste únicamente esta entrega, abrí PowerShell en la carpeta del proyecto.

### 2. Crear y activar el entorno virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```powershell
python -m pip install langchain-core langchain-google-genai pydantic python-dotenv
```

### 4. Configurar las variables de entorno

Crear el archivo `.env` a partir de la plantilla:

```powershell
Copy-Item .env.example .env
```

Editar `.env` y completar las variables:

```dotenv
GOOGLE_API_KEY=tu_api_key_aqui
GEMINI_MODEL=gemini-3.5-flash-lite
```

Reemplazar `tu_api_key_aqui` por una clave válida de Google AI Studio. Nunca publicar la clave ni subir el archivo `.env` al repositorio.

El modelo configurado es el utilizado durante las pruebas del proyecto. Su disponibilidad puede depender del acceso habilitado para cada cuenta.

## Ejecución

Con el entorno virtual activado y las variables configuradas, ejecutar:

```powershell
python main.py
```

El programa procesa un texto técnico de ejemplo, solicita una respuesta estructurada al modelo y valida el resultado con Pydantic. Finalmente, muestra los datos obtenidos en formato JSON.

## Estructura del proyecto

- `schemas.py`: modelo Pydantic, tipos de datos y validaciones.
- `chain.py`: configuración del modelo, prompt, cadena LCEL, reintentos y procesamiento asíncrono.
- `main.py`: ejemplo de ejecución del pipeline.
- `.env.example`: plantilla de configuración.
- `.gitignore`: archivos excluidos del control de versiones.
- `README.md`: documentación del proyecto.

## Ejemplo de salida

```json
{
  "tecnologias": [
    "FastAPI",
    "Redis",
    "PostgreSQL"
  ],
  "nivel_de_criticidad": "alta",
  "resumen_tecnico": "La API construida con FastAPI, que utiliza Redis y PostgreSQL, presenta problemas de tiempos de respuesta elevados y errores 503 debido a conexiones concurrentes."
}
```

La salida concreta depende del texto analizado y de la respuesta generada por el modelo.

## Manejo de errores

El pipeline registra el inicio y el resultado del procesamiento. Si ocurre un error durante la ejecución, registra la excepción y la propaga para que pueda ser gestionada por el programa que lo invoca.
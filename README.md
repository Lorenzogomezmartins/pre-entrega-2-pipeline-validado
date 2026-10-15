# Pre-entrega 2: Pipeline de procesamiento validado

## Descripción

Este proyecto implementa un pipeline asíncrono de procesamiento de textos técnicos utilizando un modelo de lenguaje (LLM), LangChain, Google Gemini y Pydantic.

El objetivo es analizar un texto técnico y generar una extracción estructurada y validada con información relevante para identificar tecnologías, determinar el nivel de criticidad y producir un resumen técnico.

## Funcionalidades

- Extracción automática de tecnologías mencionadas en un texto.
- Clasificación del nivel de criticidad en `baja`, `media` o `alta`.
- Generación de un resumen técnico.
- Validación de los datos mediante modelos de Pydantic.
- Definición de un prompt con `ChatPromptTemplate`.
- Composición del pipeline mediante LCEL.
- Uso de `with_structured_output()` para obtener resultados estructurados.
- Reintentos ante errores de procesamiento.
- Ejecución asíncrona mediante `ainvoke()`.
- Registro de eventos y errores mediante logs.

## Tecnologías utilizadas

- Python
- LangChain
- Google Gemini
- Pydantic
- python-dotenv

## Estructura del proyecto

```text
pre-entrega-2/
├── schemas.py       # Modelos y validaciones de Pydantic
├── chain.py         # Prompt, modelo LLM y pipeline LCEL
├── main.py          # Ejecución de ejemplo
├── .env.example     # Plantilla de variables de entorno
├── .gitignore       # Archivos excluidos de Git
└── README.md        # Documentación del proyecto
```

## Requisitos

- Python instalado.
- Una API key de Google AI Studio para utilizar Gemini.

## Instalación

### 1. Clonar el repositorio

```powershell
git clone https://github.com/Lorenzogomezmartins/pre-entrega-2-pipeline-validado.git
cd pre-entrega-2-pipeline-validado
```

### 2. Crear y activar un entorno virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```powershell
pip install langchain-core langchain-google-genai pydantic python-dotenv
```

### 4. Configurar las variables de entorno

Copiar el archivo de ejemplo:

```powershell
Copy-Item .env.example .env
```

Editar `.env` y configurar las siguientes variables:

```env
GOOGLE_API_KEY=tu_api_key_aqui
GEMINI_MODEL=gemini-3.5-flash-lite
```

Reemplazar `tu_api_key_aqui` por una API key propia de Google AI Studio. No publicar ni subir el archivo `.env` a GitHub.

## Ejecución

Con el entorno virtual activado y las variables de entorno configuradas, ejecutar:

```powershell
python main.py
```

El programa procesa un texto técnico de ejemplo y muestra el resultado estructurado en formato JSON.

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

El resultado puede variar según el texto analizado y la respuesta del modelo.

## Validación y manejo de errores

El esquema definido con Pydantic verifica que la respuesta respete la estructura esperada y los tipos de datos establecidos.

El pipeline incluye reintentos ante errores de procesamiento y registros mediante logs para facilitar el seguimiento de la ejecución y el diagnóstico de fallos.

## Autor

Lorenzo Gómez Martins

GitHub: [Lorenzogomezmartins](https://github.com/Lorenzogomezmartins)
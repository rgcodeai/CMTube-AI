# CMTube AI: Resumidor de Videos de YouTube con IA

CMTube AI es una herramienta de código abierto que utiliza inteligencia artificial para resumir videos de YouTube de forma gratuita y sin límites. Además de generar resúmenes detallados, la aplicación incluye un chatbot que permite a los usuarios hacer preguntas específicas sobre el contenido del video.

## Características principales

- Resumen automático de videos de YouTube
- Chatbot interactivo para preguntas sobre el contenido del video
- Procesamiento de videos largos mediante segmentación
- Interfaz de usuario intuitiva
- Gratuito y de código abierto

## Requisitos del sistema

- Python 3.10 o superior (probado con 3.11.3)
- pip (gestor de paquetes de Python)
- Git (opcional, pero recomendado)
- VS Code u otro editor de código de tu preferencia

## Instalación rápida Windows

1. Clona o descarga el repositorio
2. Ejecuta el archivo de configuración del entorno (`setup_environment.bat` en Windows)
3. Configura tu clave API de Groq en el archivo `.env`
4. Ejecuta la aplicación con `run_app.bat` (Windows) o `streamlit run app.py` (Mac/Linux)

**Nota**: Para instrucciones detalladas de instalación, incluyendo pasos específicos para Mac y Linux, consulta nuestra [guía completa de instalación](https://mistercontenidos.com/como-resumir-videos-de-youtube-con-IA-gratis). El artículo proporciona información paso a paso para configurar el entorno y resolver problemas comunes.

## Estructura del proyecto

- `app.py`: Script principal de la aplicación Streamlit
- `.env`: Almacena la clave API de Groq
- `src/video_info.py`: Obtiene información básica del video de YouTube
- `src/transcript.py`: Maneja la obtención de la transcripción del video
- `src/analyzer.py`: Combina la información del video y la transcripción para el análisis
- `src/groq_api.py`: Gestiona las interacciones con el modelo de IA a través de la API de Groq

## Contacto

Para más información, visita [MISTER CONTENIDOS](https://mistercontenidos.com/) o contáctanos a través de contacto@mistercontenidos.com.

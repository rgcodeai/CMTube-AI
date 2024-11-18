import groq
import os
from dotenv import load_dotenv

# Load environment variables and configure Groq
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

def generate_segment_summary(transcript_text, language_code, segment_number):
    prompt = f"""Tu eres Analista YT-MC, un especialista en analizar el contenido y transcripciones de videos de YouTube para realizar resumenes detallados y facilitar el aprendizaje del contenido de YouTube. Tu propósito principal es analizar el contenido de la transcripción y realizar un informe que resuma toda la información del video de manera detallada.

El tono de comunicación de Analista YT-MC es amigable y simple, diseñado para ser comprendido por usuarios de todas las edades y niveles de habilidad técnica.

Para analizar el video y realizar el informe, Analista YT-MC debe seguir el siguiente conjunto de instrucciones detalladas:

1. Escribe el análisis en ESPAÑOL.
2. Solamente usa la información disponible en la trascripción para el resumen. NO puedes agregar información que no se mencionen explícitamente en la transcripción, de lo contrario podrías proporcionar información falsa o desactualizada.
3. Identifica el tema central del video y genera un resumen detallado enfocado en resolver exactamente la intencion de busqueda del usuario cuando ve el video.
4. Inicia el informe con una breve explicación de lo que se habla en el video sin entrar en detalle.
5. Para el cuerpo del resumen usa titulos, listas para explicar temas detalladasdas de manera simple y parafos cortos para temas sencillos.

Analiza la siguiente transcripción del segmento {segment_number} y genera el informe detallado:

La transcripción está en el idioma: {language_code}. Transcripción:\n\n{transcript_text}"""
    return get_ai_response(prompt, transcript_text, [])  # Pass an empty list as chat_history

def get_ai_response(prompt, context, chat_history):
    try:
        client = groq.Groq(api_key=groq_api_key)
        messages = [
            {"role": "system", "content": f"Eres un asistente útil que responde preguntas basadas en la siguiente transcripción de un video de YouTube: {context}"},
        ]
        
        # Agregar el historial de chat al contexto
        for message in chat_history:
            messages.append({"role": message["role"], "content": message["content"]})
        
        # Agregar la pregunta actual
        messages.append({"role": "user", "content": prompt})
        
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.1-8b-instant",
            temperature=0.7,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error al obtener respuesta de AI: {str(e)}"

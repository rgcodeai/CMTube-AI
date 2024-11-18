import streamlit as st
import time
from src.video_info import get_video_id
from src.analyzer import analyze_video
from src.groq_api import get_ai_response, generate_segment_summary

def initialize_session_state():
    default_states = {
        'analysis_complete': False,
        'transcript_chunks': [],
        'summaries': [],
        'video_id': "",
        'chat_history': [],
        'title': "",
        'current_view': "summary",
        'language_code': "",
        'video_duration': 0
    }
    for key, value in default_states.items():
        if key not in st.session_state:
            st.session_state[key] = value

def setup_sidebar():
    with st.sidebar:
        st.title("💬 Resuma y converse con videos de YouTube")
        st.caption("🚀 Impulsado por Groq")
        url = st.text_input("Ingrese la URL del video de YouTube:", key="url_input")
        analyze_button = st.button("Analizar Video", type="primary")
        
        st.subheader("Modos")
        st.info("Utiliza los botones de abajo para cambiar entre el resumen del video y el chatbot interactivo.")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📊 Resumen", use_container_width=True):
                st.session_state.current_view = "summary"
        with col2:
            if st.button("💬 Chatbot", use_container_width=True):
                st.session_state.current_view = "chatbot"

        st.markdown("---")    
        st.subheader("Links Importantes")  
        "- 📖 [Directorio de IA](https://mistercontenidos.com/directorio-ia/)"      
        "- [Obtén una clave API de Groq](https://console.groq.com/keys)"
        "Hecho con 🖤 por [Mister Contenidos](https://mistercontenidos.com)"
    
    return url, analyze_button

def seconds_to_minutes(seconds):
    minutes, remaining_seconds = divmod(int(seconds), 60)
    return f"{minutes}:{int(remaining_seconds):02d}"

def display_summary():
    st.title(st.session_state.title)
    st.components.v1.iframe(f"https://www.youtube.com/embed/{st.session_state.video_id}", width=400, height=225)
    st.subheader("Análisis Detallado por Segmentos")
    
    for i, summary in enumerate(st.session_state.summaries):
        start_time = st.session_state.transcript_chunks[i]['start_time']
        end_time = st.session_state.transcript_chunks[i]['end_time']
        with st.expander(f"Análisis del video del minuto {seconds_to_minutes(start_time)} al minuto {seconds_to_minutes(end_time)}", expanded=True):
            st.write(summary)

def analyze_video_content(url):
    st.session_state.analysis_complete = False
    st.session_state.summaries = []
    new_video_id = get_video_id(url)
    if new_video_id != st.session_state.video_id:
        st.session_state.video_id = new_video_id
        st.session_state.chat_history = []
    
    if st.session_state.video_id:
        st.session_state.title, st.session_state.transcript_chunks, st.session_state.language_code, st.session_state.video_duration = analyze_video(url)
        if st.session_state.title and st.session_state.transcript_chunks:
            st.session_state.analysis_complete = True
            display_video_analysis()
        else:
            st.error("No se pudo obtener la información del video o la transcripción. Verifique la URL y asegúrese de que el video tenga subtítulos disponibles.")
    else:
        st.error("No se pudo obtener el ID del video. Verifique la URL.")

def display_video_analysis():
    st.title(st.session_state.title)
    st.components.v1.iframe(f"https://www.youtube.com/embed/{st.session_state.video_id}", width=400, height=225)
    st.subheader("Análisis Detallado por Segmentos")
    
    progress_bar = st.progress(0)
    segments_container = st.empty()
    
    for i, chunk in enumerate(st.session_state.transcript_chunks):
        with st.spinner(f"Analizando sección {i+1} de {len(st.session_state.transcript_chunks)}..."):
            summary = generate_segment_summary(chunk['text'], st.session_state.language_code, i+1)
            st.session_state.summaries.append(summary)
            
            update_segments_display(segments_container)
            progress_bar.progress((i + 1) / len(st.session_state.transcript_chunks))
            
            if i < len(st.session_state.transcript_chunks) - 1:
                time.sleep(30)
    
    progress_bar.empty()

def update_segments_display(container):
    with container.container():
        for j, summary in enumerate(st.session_state.summaries):
            start_time = st.session_state.transcript_chunks[j]['start_time']
            end_time = st.session_state.transcript_chunks[j]['end_time']
            with st.expander(f"Análisis del video del minuto {seconds_to_minutes(start_time)} al minuto {seconds_to_minutes(end_time)}", expanded=True):
                st.write(summary)

def display_chatbot():
    st.title("Chatbot Interactivo")
    st.caption("⚠️ Puede tener alucinaciones")
    st.components.v1.iframe(f"https://www.youtube.com/embed/{st.session_state.video_id}", width=400, height=225)

    if not st.session_state.chat_history:
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": "¡Hola! Soy tu asistente virtual para este video. Puedes hacerme preguntas sobre el contenido del video o pedir aclaraciones sobre cualquier parte específica. ¿En qué puedo ayudarte?"
        })

    for msg in st.session_state.chat_history:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("Haz una pregunta sobre el video:"):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        with st.spinner("Generando respuesta..."):
            full_transcript = "\n\n".join([chunk['text'] for chunk in st.session_state.transcript_chunks])
            response = get_ai_response(prompt, full_transcript, st.session_state.chat_history)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

def main():
    st.set_page_config(page_title="Resume y Chatea con videos de YouTube - Gratis")
    initialize_session_state()
    url, analyze_button = setup_sidebar()

    if analyze_button and url:
        analyze_video_content(url)
    elif st.session_state.analysis_complete:
        if st.session_state.current_view == "summary":
            display_summary()
        elif st.session_state.current_view == "chatbot":
            display_chatbot()
    else:
        st.info("Por favor, analiza un video para comenzar.")

if __name__ == "__main__":
    main()

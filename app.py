import streamlit as st

from audio.recorder import record_audio
from stt.transcriber import transcribe_audio
from llm.gemini_engine import generate_response
from tts.speaker import speak_text

# Initialize session memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Page config
st.set_page_config(
    page_title="AI Voice Assistant",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI Voice Assistant")

st.markdown("---")

st.subheader("🎤 Voice Conversation")

# Start button
if st.button("Start Conversation"):

    # Record audio
    with st.spinner("🎤 Listening..."):
        audio_path = record_audio()

    # Transcribe audio
    with st.spinner("🧠 Transcribing speech..."):
        transcript = transcribe_audio(audio_path)

    # Generate AI response
    with st.spinner("🤖 Thinking..."):
        response = generate_response(transcript)

    # Store conversation in session state
    st.session_state.chat_history.append(
        {"role": "user", "message": transcript}
    )

    st.session_state.chat_history.append(
        {"role": "assistant", "message": response}
    )

    # Display full conversation history
    st.markdown("## 💬 Conversation")

    for chat in st.session_state.chat_history:

        if chat["role"] == "user":
            st.markdown(f"🧑 You: {chat['message']}")

        else:
            st.markdown(f"🤖 Nova: {chat['message']}")

    # Speak response
    speak_text(response)
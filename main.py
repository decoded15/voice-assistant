from audio.recorder import record_audio
from stt.transcriber import transcribe_audio
from llm.gemini_engine import generate_response

if __name__ == "__main__":
    # Record user speech
    audio_path = record_audio()

    # Convert speech to text
    transcript = transcribe_audio(audio_path)

    print("\nYou Said:")
    print(transcript)

    # Generate AI response
    response = generate_response(transcript)

    print("\n🤖 Assistant:")
    print(response)
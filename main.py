from audio.recorder import record_audio
from stt.transcriber import transcribe_audio
from llm.gemini_engine import generate_response
from tts.speaker import speak_text

print("🤖 AI Voice Assistant Started!")
print("Say 'exit' anytime to stop.\n")

while True:
    # Record speech
    audio_path = record_audio()

    # Speech → text
    transcript = transcribe_audio(audio_path)

    print("\n📝 You Said:")
    print(transcript)

    # Exit condition
    if "exit" in transcript.lower():
        print("👋 Exiting assistant...")
        break

    # Generate AI response
    response = generate_response(transcript)

    print("\n🤖 Assistant:")
    print(response)

    # Speak response
    speak_text(response)
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

def speak_text(text):
    print("🔊 Speaking response...")

    engine.say(text)

    engine.runAndWait()

    print("✅ Finished speaking!")
import asyncio
import edge_tts
from playsound import playsound
import os

VOICE = "en-US-GuyNeural"

async def generate_speech(text, output_file="audio/temp/response.mp3"):
    communicate = edge_tts.Communicate(text, VOICE)

    await communicate.save(output_file)

def speak_text(text):
    print("🔊 Speaking response...")

    os.makedirs("audio/temp", exist_ok=True)

    output_file = "audio/temp/response.mp3"

    # Generate speech
    asyncio.run(generate_speech(text, output_file))

    # Play generated audio
    playsound(output_file)

    print("✅ Finished speaking!")
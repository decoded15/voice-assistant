import asyncio
import edge_tts
from playsound import playsound
import os
import uuid

VOICE = "en-US-GuyNeural"

async def generate_speech(text, output_file):
    communicate = edge_tts.Communicate(text, VOICE)

    await communicate.save(output_file)

def speak_text(text):
    print("🔊 Speaking response...")

    os.makedirs("audio/temp", exist_ok=True)

    # Generate unique filename
    output_file = f"audio/temp/{uuid.uuid4()}.mp3"

    # Generate speech
    asyncio.run(generate_speech(text, output_file))

    # Play generated audio
    playsound(output_file)

    print("✅ Finished speaking!")
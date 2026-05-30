import sounddevice as sd
from scipy.io.wavfile import write
import os
 
# Audio settings
SAMPLE_RATE = 16000
DURATION = 5

def record_audio(filename="audio/temp/input.wav"):
    print("🎤 Recording started...")

    # Record audio
    recording = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype='int16'
    )

    # Wait until recording finishes
    sd.wait()

    print("✅ Recording complete!")

    # Ensure folder exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Save recording
    write(filename, SAMPLE_RATE, recording)

    return filename
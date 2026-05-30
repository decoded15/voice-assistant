from faster_whisper import WhisperModel

# Load Whisper model
model = WhisperModel("base")

def transcribe_audio(audio_path):
    print("🧠 Transcribing audio...")

    segments, info = model.transcribe(audio_path)

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    print("✅ Transcription complete!")

    return transcript.strip()
from audio.recorder import record_audio
from stt.transcriber import transcribe_audio

if __name__ == "__main__":
    audio_path = record_audio()

    transcript = transcribe_audio(audio_path)

    print("\n📝 Transcript:")
    print(transcript)
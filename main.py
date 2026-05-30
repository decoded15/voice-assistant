from audio.recorder import record_audio

if __name__ == "__main__":
    audio_path = record_audio()

    print(f"Audio saved at: {audio_path}")
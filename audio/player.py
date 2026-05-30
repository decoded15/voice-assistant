import sounddevice as sd
from scipy.io.wavfile import read

def play_audio(filename):
    print("🔊 Playing audio...")

    # Read WAV file
    sample_rate, data = read(filename)

    # Play audio
    sd.play(data, sample_rate)

    # Wait until playback finishes
    sd.wait()

    print("✅ Playback complete!")
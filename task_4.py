import sounddevice as sd
import wavio

def record_voice(filename, duration, samplerate=44100):
    print("Recording started...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")
    
    # Save the recording as a WAV file
    wavio.write(filename, recording, samplerate, sampwidth=2)
    print(f"Recording saved as {filename}")

if __name__ == "__main__":
    filename = "my_recording.wav"
    duration = 10  # seconds
    samplerate = 44100  # samples per second
    
    record_voice(filename, duration, samplerate)

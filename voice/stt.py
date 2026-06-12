from faster_whisper import WhisperModel
import sounddevice as sd
from scipy.io.wavfile import write

model_size = "base"

def record_audio(
    filename="input.wav",
    duration=5,
    sample_rate=16000
):
    print("Listening...")
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )
    
    sd.wait()
    write(filename, sample_rate, recording)
    
    return filename

# Run on GPU with FP16
model = WhisperModel(model_size, device="cpu", compute_type="int8")

def transcribe_audio(audio_path):
    segments, info = model.transcribe(audio_path)
    text = ""
    
    for segment in segments:
        text += segment.text
    
    return text.strip()

audio_file = record_audio()
query = transcribe_audio(audio_file)
print("You: ", query)


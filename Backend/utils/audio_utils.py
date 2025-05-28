import sounddevice as sd
import scipy.io.wavfile as wav

def grabar_audio(nombre, duracion=5, fs=44100):
    print("🎙️ Grabando...")
    audio = sd.rec(int(duracion * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wav.write(nombre, fs, audio)
    print(f"✅ Guardado como: {nombre}")
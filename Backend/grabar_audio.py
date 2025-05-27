import sounddevice as sd
from scipy.io.wavfile import write
import os

def grabar_audio(nombre_archivo, duracion=5, fs=44100):
    print("Grabando...")
    audio = sd.rec(int(duracion * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    if not os.path.exists("audios"):
        os.makedirs("audios")
    ruta = os.path.join("audios", nombre_archivo)
    write(ruta, fs, audio)
    print("Grabación guardada:", ruta)
    return ruta

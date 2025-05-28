import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
import os
import time

def grabar_audio(nombre_archivo, duracion=5):
    print("🎙️ Grabando...")
    fs = 44100
    audio = sd.rec(int(duracion * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    time.sleep(1)
    wav.write(nombre_archivo, fs, audio)
    print(f"✅ Guardado como: {nombre_archivo}")

def transcribir_audio(audio_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
    try:
        texto = r.recognize_google(audio, language="es-PE")  # Español Perú
        return texto.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

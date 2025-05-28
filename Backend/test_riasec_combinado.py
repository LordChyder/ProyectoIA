import os
import time
import whisper
import joblib
import sounddevice as sd
import scipy.io.wavfile as wav
import librosa
import numpy as np
import pandas as pd

# ================= CONFIGURACIÓN =================
duracion = 5
modelo_whisper = whisper.load_model("base")
modelo_emocional = joblib.load("model/modelo_riasec.pkl")  # Cargamos tu modelo original
grabaciones_dir = "backend/data/grabaciones_test_final"
os.makedirs(grabaciones_dir, exist_ok=True)

puntajes_riasec = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}

preguntas = [
    ("¿Te gustaría reparar artefactos eléctricos?", "R"),
    ("¿Te interesa trabajar en un laboratorio de ciencia?", "I"),
    ("¿Te gustaría escribir poesía o pintar?", "A")
]

# ================ FUNCIONES ===================
def grabar_audio(nombre_archivo, duracion=5):
    print("🎙️ Grabando...")
    fs = 44100
    audio = sd.rec(int(duracion * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    time.sleep(1)
    wav.write(nombre_archivo, fs, audio)
    print(f"✅ Guardado como: {nombre_archivo}")

def extraer_modulacion(path):
    y, sr = librosa.load(path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rms = librosa.feature.rms(y=y)
    pitch, _ = librosa.piptrack(y=y, sr=sr)
    return {
        'mfcc_mean': np.mean(mfcc),
        'chroma_mean': np.mean(chroma),
        'centroid_mean': np.mean(centroid),
        'bandwidth_mean': np.mean(bandwidth),
        'rms_mean': np.mean(rms),
        'pitch_mean': np.mean(pitch[pitch > 0])
    }

# ================ FLUJO PRINCIPAL ===================
for i, (pregunta, tipo) in enumerate(preguntas, start=1):
    print(f"\n🔹 Pregunta {i}: {pregunta}")
    nombre_archivo = os.path.join(grabaciones_dir, f"respuesta_{i:02d}.wav")
    grabar_audio(nombre_archivo, duracion=duracion)

    # Transcripción con Whisper
    result = modelo_whisper.transcribe(nombre_archivo, language="es")
    texto = result["text"].strip().lower()
    print(f"📝 Transcripción: {texto}")

    # Clasificación sí/no
    if "sí" in texto or "si" in texto:
        decision = "SI"
        puntajes_riasec[tipo] += 1
    elif "no" in texto:
        decision = "NO"
    else:
        decision = "DUDOSO"
    print(f"🧠 Clasificación por contenido: {decision}")

    # Análisis acústico + predicción del modelo
    mod = extraer_modulacion(nombre_archivo)
    df_mod = pd.DataFrame([mod])
    prediccion_modelo = modelo_emocional.predict(df_mod)[0]
    print(f"🎯 Predicción IA por voz (modelo emocional): {prediccion_modelo}")
    print(f"🎛️ Modulación: pitch={mod['pitch_mean']:.2f} Hz, energía={mod['rms_mean']:.5f}")

# ================ RESULTADO FINAL ===================
print("\n📊 Puntaje final por conteo de 'sí':")
for tipo, pts in puntajes_riasec.items():
    print(f"  {tipo}: {pts}")
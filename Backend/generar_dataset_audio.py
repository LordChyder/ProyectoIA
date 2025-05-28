import os
import pandas as pd
import numpy as np
import librosa

# Ruta base donde están los audios
ruta_audios = 'Backend/data/grabaciones/PREFERENCIAS'

# Lista para almacenar datos
datos = []

# Recorremos todos los archivos de audio
for carpeta, _, archivos in os.walk(ruta_audios):
    for archivo in archivos:
        if archivo.endswith('.wav'):
            ruta_completa = os.path.join(carpeta, archivo)

            # Cargar audio
            y, sr = librosa.load(ruta_completa, sr=None)

            # Extraer características
            mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
            chroma = librosa.feature.chroma_stft(y=y, sr=sr)
            centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
            bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
            rms = librosa.feature.rms(y=y)
            pitch, _ = librosa.piptrack(y=y, sr=sr)

            # Inferir etiqueta desde el nombre de archivo (ej: TRABAJOS_A_01.wav)
            nombre = os.path.basename(ruta_completa)
            partes = nombre.split('_')
            if len(partes) >= 2:
                etiqueta = partes[1]  # Segunda parte suele ser R, I, A, S, E, C
            else:
                etiqueta = "?"

            datos.append({
                'archivo': nombre,
                'mfcc_mean': np.mean(mfcc),
                'chroma_mean': np.mean(chroma),
                'centroid_mean': np.mean(centroid),
                'bandwidth_mean': np.mean(bandwidth),
                'rms_mean': np.mean(rms),
                'pitch_mean': np.mean(pitch[pitch > 0]),
                'etiqueta_RIASEC': etiqueta
            })

# Guardar como CSV
df = pd.DataFrame(datos)
df.to_csv('data/dataset_riasec_etiquetas.csv', index=False)
print("✅ Dataset generado: data/dataset_riasec_etiquetas.csv")
print(df.head())

import os
import pandas as pd
from features.extract_audio_features import extract_audio_features

csv_path = "Backend/data/dataset_riasec_etiquetas.csv"
grabaciones_path = "Backend/data/grabaciones"
nuevos_datos = []

# Cargar dataset existente si hay
if os.path.exists(csv_path):
    df_existente = pd.read_csv(csv_path)
    archivos_existentes = set(df_existente["archivo"])
else:
    df_existente = pd.DataFrame()
    archivos_existentes = set()

# Recorrer todos los .wav
for root, _, files in os.walk(grabaciones_path):
    for file in files:
        if file.endswith(".wav") and file not in archivos_existentes:
            ruta = os.path.join(root, file)
            caracteristicas = extract_audio_features(ruta)
            etiqueta = file.split("_")[1]  # extrae R, I, A...
            fila = {"archivo": file, "etiqueta_RIASEC": etiqueta}
            fila.update(caracteristicas)
            nuevos_datos.append(fila)

# Crear nuevo DataFrame y unir con el anterior
df_nuevo = pd.DataFrame(nuevos_datos)
df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)

# Guardar
df_final.to_csv(csv_path, index=False)
print(f"✅ Dataset actualizado: {len(df_nuevo)} nuevos audios añadidos.")

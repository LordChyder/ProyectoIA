from preguntas_data.bloques_preguntas import bloques_preguntas
from utils.audio_utils import grabar_audio
from model.predict import predecir_tipo
import os

# Carpeta donde se guardan las grabaciones
carpeta_base = "Backend/data/grabaciones"

# Recorrer por bloque y tipo RIASEC
for bloque, categorias in bloques_preguntas.items():  # ✅ FUNCIONA
    print(f"Bloque: {bloque}")
    for tipo, lista_preguntas in categorias.items():
        print(f"\n🔹 Tipo RIASEC: {tipo}")
        for i, pregunta in enumerate(lista_preguntas, start=1):
            print(f"\nPregunta {i}: {pregunta}")

            # Crear subcarpeta por bloque si no existe
            carpeta_bloque = os.path.join(carpeta_base, bloque)
            os.makedirs(carpeta_bloque, exist_ok=True)

            # Definir nombre de archivo
            nombre_archivo = os.path.join(carpeta_bloque, f"{bloque}_{tipo}_{i:02d}.wav")

            # Grabar audio
            grabar_audio(nombre_archivo, duracion=5)

            # Predecir tipo RIASEC a partir de la voz
            #tipo_detectado = predecir_tipo(nombre_archivo)
            #print(f"🎯 Predicción IA: {tipo_detectado}")

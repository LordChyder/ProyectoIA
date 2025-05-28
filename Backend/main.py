from preguntas_data.bloques_preguntas import bloques_preguntas
from utils.audio_utils import grabar_audio, transcribir_audio
import os
from collections import defaultdict

# Carpeta de grabaciones
carpeta_base = "data/grabaciones"
respuestas = defaultdict(int)

# Recorremos preguntas por bloque y tipo
for bloque, categorias in bloques_preguntas.items():
    print(f"\n🗂️ Bloque: {bloque}")
    for tipo, preguntas in categorias.items():
        print(f"\n🔹 Tipo RIASEC: {tipo}")
        for i, pregunta in enumerate(preguntas, 1):
            print(f"Pregunta {i}: {pregunta}")

            carpeta_tipo = os.path.join(carpeta_base, bloque)
            os.makedirs(carpeta_tipo, exist_ok=True)
            nombre_archivo = os.path.join(carpeta_tipo, f"{bloque}_{tipo}_{i:02d}.wav")

            grabar_audio(nombre_archivo, duracion=5)
            transcripcion = transcribir_audio(nombre_archivo)

            print(f"📝 Transcripción: {transcripcion}")

            if "sí" in transcripcion or "si" in transcripcion:
                respuestas[tipo] += 1
            elif "no" in transcripcion:
                pass  # también puedes registrar "no" si deseas

# Mostrar resultado final tipo Holland
print("\n✅ Resultado final (conteo de 'sí'):")
for tipo, cantidad in respuestas.items():
    print(f"{tipo}: {cantidad} respuestas afirmativas")

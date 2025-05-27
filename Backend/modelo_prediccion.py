from tensorflow.keras.models import load_model
import os

def cargar_modelo():
    ruta = "modelo_guardado/modelo_voz_risasec.h5"
    if os.path.exists(ruta):
        model = load_model(ruta)
        print("✅ Modelo cargado correctamente.")
        return model
    else:
        print("❌ No se encontró el modelo entrenado. Ejecuta primero modelo_entrenamiento.py")
        return None

from grabar_audio import grabar_audio
from extraer_features import extraer_features
from clasificador_holland import clasificar_por_reglas, predecir_con_modelo
from modelo_prediccion import cargar_modelo

# 1. Grabar audio del usuario
archivo = grabar_audio("respuesta_test.wav", duracion=7)

# 2. Extraer características vocales
features = extraer_features(archivo)

# 3. Cargar modelo entrenado
modelo = cargar_modelo()

# 4. Clasificación por red neuronal (si el modelo existe)
if modelo:
    tipo, confianza, carreras = predecir_con_modelo(features, modelo)
    print(f"\n🎯 Predicción con modelo IA:")
    print(f"Tipo Holland: {tipo} (confianza: {confianza:.2f})")
    print("Carreras sugeridas:")
    for c in carreras:
        print(f"— {c}")
else:
    # 5. Alternativa: usar reglas básicas si no hay modelo
    tipo, carreras = clasificar_por_reglas(features)
    print(f"\n🔍 Clasificación por reglas:")
    print(f"Tipo Holland: {tipo}")
    print("Carreras sugeridas:")
    for c in carreras:
        print(f"— {c}")

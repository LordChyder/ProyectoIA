import numpy as np

def clasificar_por_reglas(features):
    energia = features[1]
    pitch = features[6]
    varianza_pitch = features[9]
    pausas = features[3]

    if energia > 0.3 and pitch > 3000 and varianza_pitch > 0.2:
        tipo = "Emprendedor"
        carreras = ["Administración", "Turismo", "Derecho"]
    elif energia < 0.2 and pitch < 2000 and pausas < 0.05:
        tipo = "Investigador"
        carreras = ["Medicina Humana", "Sistemas", "Agroindustrial"]
    elif energia < 0.25 and pitch > 2500 and varianza_pitch > 0.25:
        tipo = "Artístico"
        carreras = ["Arquitectura", "Idiomas"]
    elif energia < 0.25 and pausas > 0.1:
        tipo = "Social"
        carreras = ["Educación", "Enfermería", "Obstetricia"]
    elif energia > 0.25 and pitch < 2500 and varianza_pitch < 0.15:
        tipo = "Realista"
        carreras = ["Agronomía", "Veterinaria", "Civil", "Ambiental"]
    else:
        tipo = "Convencional"
        carreras = ["Contabilidad", "Economía", "Informática"]

    return tipo, carreras

def predecir_con_modelo(features, model):
    features = np.expand_dims(features, axis=0)
    pred = model.predict(features)[0]
    idx = np.argmax(pred)
    tipos = ["Realista", "Investigador", "Artístico", "Social", "Emprendedor", "Convencional"]

    tipo = tipos[idx]
    confianza = pred[idx]

    carreras_sugeridas = {
        "Realista": ["Agronomía", "Veterinaria", "Ingeniería Civil", "Ambiental"],
        "Investigador": ["Medicina", "Sistemas", "Agroindustrial"],
        "Artístico": ["Arquitectura", "Idiomas"],
        "Social": ["Educación", "Enfermería", "Obstetricia"],
        "Emprendedor": ["Administración", "Turismo", "Derecho"],
        "Convencional": ["Contabilidad", "Economía", "Informática"]
    }

    return tipo, confianza, carreras_sugeridas[tipo]

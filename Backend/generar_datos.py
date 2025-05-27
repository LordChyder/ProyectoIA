import numpy as np

def generar_datos_sinteticos(n_por_clase=100):
    tipos = {
        "Realista": {"media": 0.3, "var": 0.05},
        "Investigador": {"media": 0.2, "var": 0.03},
        "Artístico": {"media": 0.5, "var": 0.07},
        "Social": {"media": 0.25, "var": 0.04},
        "Emprendedor": {"media": 0.6, "var": 0.06},
        "Convencional": {"media": 0.15, "var": 0.02}
    }

    X = []
    y = []

    for i, tipo in enumerate(tipos):
        media = tipos[tipo]["media"]
        var = tipos[tipo]["var"]
        for _ in range(n_por_clase):
            sample = np.random.normal(loc=media, scale=var, size=34)
            X.append(sample)
            y.append(i)

    return np.array(X), np.array(y)

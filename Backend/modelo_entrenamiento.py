import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical
from generar_datos import generar_datos_sinteticos
import os

def entrenar_y_guardar_modelo():
    X, y = generar_datos_sinteticos()
    y_cat = to_categorical(y, num_classes=6)

    model = Sequential([
        Dense(64, activation='relu', input_shape=(X.shape[1],)),
        Dropout(0.3),
        Dense(64, activation='relu'),
        Dropout(0.3),
        Dense(6, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(X, y_cat, epochs=30, batch_size=8, validation_split=0.2)

    if not os.path.exists("modelo_guardado"):
        os.makedirs("modelo_guardado")

    model.save("modelo_guardado/modelo_voz_risasec.h5")
    print("Modelo guardado en modelo_guardado/")

if __name__ == "__main__":
    entrenar_y_guardar_modelo()

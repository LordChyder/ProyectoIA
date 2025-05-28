import joblib
import pandas as pd
from features.extract_audio_features import extract_audio_features

def predecir_tipo(audio_path):
    modelo = joblib.load('model/modelo_riasec.pkl')
    features = extract_audio_features(audio_path)
    df = pd.DataFrame([features])
    resultado = modelo.predict(df)
    return resultado[0]
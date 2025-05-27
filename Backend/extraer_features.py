import librosa
import numpy as np

def extraer_features(ruta_audio):
    y, sr = librosa.load(ruta_audio, sr=None)
    
    # Extraer características comunes
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))
    centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    rolloff = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr))
    bandwidth = np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr))
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfccs_mean = np.mean(mfccs, axis=1)

    # Combinar en un solo vector
    features = np.hstack([zcr, centroid, rolloff, bandwidth, mfccs_mean])
    return features

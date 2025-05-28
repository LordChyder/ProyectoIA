import librosa
import numpy as np

def extract_audio_features(filepath):
    y, sr = librosa.load(filepath, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rms = librosa.feature.rms(y=y)
    pitch, _ = librosa.piptrack(y=y, sr=sr)

    return {
        'mfcc_mean': np.mean(mfcc),
        'chroma_mean': np.mean(chroma),
        'centroid_mean': np.mean(centroid),
        'bandwidth_mean': np.mean(bandwidth),
        'rms_mean': np.mean(rms),
        'pitch_mean': np.mean(pitch[pitch > 0])
    }
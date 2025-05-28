import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Ruta al archivo de audio
ruta_audio = 'data/grabaciones/PREFERENCIAS_R_01.wav'  # <-- cambia este nombre si es necesario

# Cargar audio
y, sr = librosa.load(ruta_audio, sr=None)

# Crear figura
plt.figure(figsize=(14, 10))

# 1. Forma de onda
plt.subplot(4, 1, 1)
librosa.display.waveshow(y, sr=sr)
plt.title('Forma de Onda')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# 2. Espectrograma (STFT)
plt.subplot(4, 1, 2)
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma (escala log)')

# 3. MFCCs
plt.subplot(4, 1, 3)
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCCs')

# 4. Pitch tracking (frecuencia fundamental)
plt.subplot(4, 1, 4)
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
pitch_values = pitches[magnitudes > np.median(magnitudes)]
plt.plot(pitch_values)
plt.title('Pitch (frecuencia fundamental)')
plt.xlabel('Frames')
plt.ylabel('Frecuencia (Hz)')

# Mostrar todo
plt.tight_layout()
plt.show()
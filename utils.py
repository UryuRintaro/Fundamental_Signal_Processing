import librosa
import numpy as np

class MelSpec:
    def __init__(self):
        pass

    def __call__(self, data, sr=44100):
        S = librosa.feature.melspectrogram(y=data, sr=sr, n_mels=128)
        S_dB = librosa.power_to_db(S, ref=np.max)
        return S_dB


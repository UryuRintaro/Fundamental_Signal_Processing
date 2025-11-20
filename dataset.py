import numpy as np
import librosa
from pathlib import Path
from torch.utils.data import Dataset
import matplotlib.pyplot as plt
import json

class MyDataset(Dataset):
    def __init__(self, dataset_dir, json_path):
        self.data_path = list(Path(dataset_dir).glob('**/*.wav'))
        json_open = open(json_path, 'r')
        self.json_load = json.load(json_open)
    
    def __len__(self):
        return len(self.data_path)
    
    def __getitem__(self, idx):
        data = self.data_path[idx]
        y, sr = librosa.load(data, sr=44100)
        label = self.json_load[data.parts[-2]]['id']
        return y, label
    
if __name__ == '__main__':
    dataset = MyDataset(dataset_dir='Data', json_path='label.json')
    y, label = dataset[0]
    print(f"label : {label}")
    print(y)
    D = np.abs(librosa.stft(y, n_fft=2048, hop_length=512))
    S = D[:,100]
    freq = librosa.fft_frequencies(sr=44100, n_fft=2048)
    plt.plot(freq, librosa.amplitude_to_db(S, ref=np.max))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.xlim(0, 22050)
    plt.savefig('data.png')
from pathlib import Path
import numpy as np
from scipy import signal
from scipy.io.wavfile import write
from random import randint
import os

parent_dir = "Data"
waveform = ['sine', 'square', 'sawtooth']

sr = 44100
duration = 3.
t = np.linspace(0., duration, int(duration*sr), endpoint=False)
max_amplitude = np.iinfo(np.int16).max
amplitude = 0.5

A4 = 440
tone = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
freq =  []
for i in range(12):
    freq.append(A4*2**((1/12)*(-9+i)))

for wave in waveform:
    dir_path = os.path.join(parent_dir, wave)
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    for i in range(10):
        idx = randint(0, 11)
        if wave == 'sine':
            y = (amplitude*max_amplitude*np.sin(2*np.pi*freq[idx]*t)).astype(np.int16)
        elif wave == 'square':
            y = (amplitude*max_amplitude*np.sign(np.sin(2*np.pi*freq[idx]*t))).astype(np.int16)
        elif wave == 'sawtooth':
            y = (amplitude*max_amplitude*signal.sawtooth(2*np.pi*freq[idx]*t)).astype(np.int16)
        file_path = os.path.join(dir_path, f"{wave}_{i}_{tone[idx]}.wav")
        write(file_path, sr, y)

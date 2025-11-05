import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt


# a) citire semnal 
fs, semnal = wavfile.read('lab4/vocale.wav')
semnal = semnal[:, 0] # folosim doar un canal ptc e stereo
semnal = semnal / np.max(np.abs(semnal)) # normalizam intre -1 si 1 pt procesare
N = len(semnal)

# b) grupam valorile 
#dimensiune 1% din totalul semnalului
dim = int(N * 0.01)
# suprapunere 50%
suprapunere = int(dim * 0.5)
# cat de mult avansam la fiecare pas
avans = dim - suprapunere

frames = [] # lista de frameuri
for i in range(0, N - dim, avans):
    frame = semnal[i : i + dim]
    window = np.hanning(dim) 
    windowed_frame = frame * window
    
    frames.append(windowed_frame)

# c) calculam FFT pt fiecare frame
lista_fft = [np.fft.rfft(frame) for frame in frames]

# d)
matr = np.abs(np.array(lista_fft).T)
matr_db = 20 * np.log10(matr + 1e-6) # adaugam o valoare mica pt a evita log(0)

# e)

t_total = N / fs
frecvente = np.fft.rfftfreq(dim, 1 / fs)
timp = np.linspace(0, t_total, len(frames))

# f)
plt.figure(figsize=(10, 5))
plt.imshow(matr_db,
           extent=[0, t_total, 0, fs / 2],
           origin='lower',
           aspect='auto',
           cmap='inferno')
plt.xlabel("Timp")
plt.ylabel("Frecventa")
plt.colorbar(label="Magnitudine (dB)")
plt.tight_layout()
plt.savefig("ex6.pdf", format='pdf')
plt.show()

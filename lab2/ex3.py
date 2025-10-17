import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

# a)
f = 400 # Hz (frecventa semnalului)
Fs = 8000 # Hz (frecventa de esantionare)
T = 1.0/Fs # s (perioada de esantionare)
nr_esantioane = 16000

n = np.arange(nr_esantioane) # vectorul de numere naturale 0-1599
x = np.cos(2*np.pi * (f/Fs) * n) # semnalul discret (formula)

t = n / Fs # vectorul timpului in secunde pt plotare

#redare sunet
sd.play(x, Fs)
sd.wait()

# b)
f_b = 800
durata = 3 # secunde
Fs_b = 4000

t_b = np.linspace(0, durata, Fs_b * durata) # vectorul timpului

x_b = np.sin(2 * np.pi * f_b * t_b)

sd.play(x_b, Fs_b)
sd.wait()

# c)
f_c = 240
Fs_c = 8000

t_c = np.linspace(0, 3, int(Fs_c * 3))
x_c =2 * (f_c * t_c - np.floor(0.5 + f_c * t_c)) # semnal sawtooth

sd.play(x_c, Fs_c)
sd.wait()

# d)
f_d = 300
Fs_d = 6000

t_d = np.linspace(0, 3, int(Fs_d * 3))
x_d = np.sign(np.sin(2 * np.pi * f_d * t_d)) # semnal patrat <=> aplicam sign pe semnalul sinusoidal

sd.play(x_d, Fs_d)
sd.wait()

wavfile.write("ex3.wav", Fs_d, x_d.astype(np.float32))

#Incarcare fisier
fs, semnal = wavfile.read("ex3.wav")
sd.play(semnal, fs)
sd.wait()
import numpy as np
import matplotlib.pyplot as plt

# a)
f = 400 # Hz (frecventa semnalului)
Fs = 8000 # Hz (frecventa de esantionare)
T = 1.0/Fs # s (perioada de esantionare)
nr_esantioane = 1600

n = np.arange(nr_esantioane) 
x = np.cos(2*np.pi * (f/Fs) * n) # semnalul discret (formula)

t = n / Fs # vectorul timpului in secunde pt plotare

plt.stem(t,x)
plt.show()

# b)
f_b = 800
durata = 3 # secunde
Fs_b = 4000

t_b = np.linspace(0, durata, Fs_b * durata) # vectorul timpului

x_b = x_b = np.sin(2 * np.pi * f_b * t_b)

plt.stem(t_b, x_b)
plt.xlim(0, 0.01) # zoom pe primii 10ms
plt.grid(True)
plt.show()


# c)
f_c = 240
Fs_c = 8000

t_c = np.linspace(0, 0.1, int(Fs_c * 0.1))
x_c =2 * (f_c * t_c - np.floor(0.5 + f_c * t_c)) # semnal sawtooth

plt.figure(figsize=(10, 4))
plt.stem(t_c, x_c)
plt.show()


# d)
f_d = 300
Fs_d = 6000

t_d = np.linspace(0, 0.01, int(Fs_d * 0.01))
x_d = np.sign(np.sin(2 * np.pi * f_d * t_d)) # semnal patrat <=> aplicam sign pe semnalul sinusoidal


plt.figure(figsize=(10, 4))
plt.stem(t_d, x_d)
plt.show()

# e)

arr = np.random.rand(128, 128)

plt.imshow(arr)
plt.show()

# f)

tabla = np.zeros((128, 128))

for i in range(0, 128, 16):
    for j in range(0, 128, 16):
        if (i // 16 + j // 16) % 2 == 0: # coloram patratele pare
            tabla[i:i+16, j:j+16] = 1

plt.imshow(tabla, cmap='gray')
plt.show()
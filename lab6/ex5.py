import numpy as np
import matplotlib.pyplot as plt

def fereastraDreptunghiulara(dim):
    return np.ones(dim)

def fereastraHanning(dim):
    return np.hanning(dim)


A = 1      
f = 100 
phi = 0     
dim = 100
fs = 1000

t = np.arange(0, dim) / fs

x = A * np.sin(2 * np.pi * f * t + phi)

drept = fereastraDreptunghiulara(dim)
hanning = fereastraHanning(dim)

x_drept = x * drept
x_hanning = x * hanning


plt.subplot(2, 1, 1)
plt.plot(t, x_drept, 'b-', label = 'Sinusoida')
plt.plot(t, drept, 'r--', label=f'Fereastra dreptunghiulara', alpha=0.7)
plt.title("Fereastra Dreptunghiulara")
plt.xlabel("Timp")
plt.ylabel("Amplitudine")
plt.grid(True, alpha=0.5)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, x_hanning, 'b-', label='Sinusoida')
plt.plot(t, hanning, 'g--', label=f'Fereastra Hanning', alpha=0.7)
plt.title("Fereastra Hanning")
plt.xlabel("Timp")
plt.ylabel("Amplitudine")
plt.grid(True, alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig("lab6/ex5.pdf", format='pdf')
plt.show()
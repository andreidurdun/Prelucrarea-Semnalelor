import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 128)
x1 = np.sin(2 * np.pi * 5 * t + np.pi)
x2 = np.sin(2 * np.pi * 5 * t + np.pi/2)
x3 = np.sin(2 * np.pi * 5 * t + np.pi/4)
x4 = np.sin(2 * np.pi * 5 * t + np.pi/8)

plt.plot(t, x1, label='phi=pi')
plt.plot(t, x2, label='phi=pi/2')
plt.plot(t, x3, label='phi=pi/4')
plt.plot(t, x4, label='phi=pi/8')
#plt.show()

valori_snr = [0.1, 1, 10, 100]
zgomot = np.random.normal(0, 1, size=len(x1)) # zgomot gaussian
norma_x = np.linalg.norm(x1)
norma_z = np.linalg.norm(zgomot)

fig, axs = plt.subplots(len(valori_snr), 1, figsize=(12, 10), sharex=True)

for i, snr in enumerate(valori_snr):
   
    gamma = norma_x / (np.sqrt(snr) * norma_z)
    
    # semnal cu zgomot: x[n] + gamma * z[n]
    semnal_zgomot = x1 + gamma * zgomot
    
    axs[i].plot(t, semnal_zgomot, label=f'SNR = {snr}', color='orange')
    axs[i].plot(t, x1, label='Semnal Original', color='blue', linestyle='--')
    axs[i].set_ylabel('Amplitudine')
    axs[i].legend()
    axs[i].grid(True)

plt.xlabel('Timp (s)')
plt.show()
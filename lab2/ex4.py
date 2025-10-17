import numpy as np
import matplotlib.pyplot as plt



t = np.linspace(0, 1, 128)
x = np.sin(2 * np.pi * 5 * t + np.pi/2)

f_c = 240
Fs_c = 8000

x_c =2 * (f_c * t - np.floor(0.5 + f_c * t)) # semnal sawtooth

adunare = x + x_c

fig, axs = plt.subplots(3)
axs[0].plot(t, x)
axs[1].plot(t, x_c)
axs[2].plot(t, adunare)
plt.show()
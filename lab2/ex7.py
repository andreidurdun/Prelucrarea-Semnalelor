import numpy as np
import matplotlib.pyplot as plt

Fs = 1000

t = np.linspace(0, 1, int(Fs * 1)) # vectorul timpului

x = np.sin(2 * np.pi * 10 * t)

Fs_decimat = 200
t_decimat = np.linspace(0, 1, int(Fs_decimat * 1))
x_decimat = np.sin(2 * np.pi * 10 * t_decimat)

Fs_decimat2 = 50
t_decimat2 = np.linspace(0, 1, int(Fs_decimat2 * 1))
x_decimat2 = np.sin(2 * np.pi * 10 * t_decimat2)
# a)
fig, axs = plt.subplots(3)
axs[0].stem(t, x)
axs[0].set_title('Semnal initial')
axs[1].stem(t_decimat, x_decimat)
axs[1].set_title('Semnal decimat')
axs[2].stem(t_decimat2, x_decimat2)
axs[2].set_title('Semnal decimat 2')
plt.show()

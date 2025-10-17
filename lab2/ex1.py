import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 128)
semnal_sin = np.sin(2 * np.pi * 5 * t)
semnal_cos = np.cos(2 * np.pi * 5 * t - np.pi/2)

fig, axs = plt.subplots(2)
axs[0].plot(t, semnal_sin)
axs[1].plot(t, semnal_cos)
plt.show()

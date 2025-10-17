import numpy as np
import matplotlib.pyplot as plt


Fs = 400 #frecv esantionare
n = 100 # nr esantioane

t = np.arange(n) / Fs
# a)

f_a = Fs/2
x_a = np.sin(2*np.pi*f_a*t)
# cum 2*pi*Fs/2*t = pi*n => sin(pi*n) = 0 pt n orice intreg => semnalul este 0, dar nu este plotat corect datorita erorilor de calcul ale python.

# b)
f_b = Fs/4
x_b = np.sin(2*np.pi*f_b*t)
# unda sinusoidala

# c)
f_c = 0
x_c = np.sin(2*np.pi*f_c*t)
# semnal constant = 0

fig, axs = plt.subplots(3)
axs[0].set_title('Fs/2')
axs[0].stem(t, x_a)
axs[1].set_title('Fs/4')
axs[1].stem(t, x_b)
axs[2].set_title('0 Hz')
axs[2].stem(t, x_c)
plt.show()
import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(-np.pi/2, np.pi/2, 5000)
sin = np.sin(2*np.pi*5*t)

aprox_pade = (t - (7.0/60.0) * t*3) / (1.0 + (1.0/20.0) * t*2)

err_tailor = sin - t
err_pade = sin - aprox_pade

fig, axs = plt.subplots(2)
axs[0].plot(t, err_tailor)
axs[0].set_title('Eroare Taylor')
axs[1].plot(t, err_pade)
axs[1].set_title('Eroare Pade')

plt.show()
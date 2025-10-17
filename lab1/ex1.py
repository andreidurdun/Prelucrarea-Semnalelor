import numpy as np
import matplotlib.pyplot as plt

# a)
t = np.linspace(0, 0.3 , 601)

# b)
xt = np.cos(520*np.pi*t + np.pi/3)
yt = np.cos(280*np.pi*t - np.pi/3)
zt = np.cos(120*np.pi*t + np.pi/3)

fig, axs = plt.subplots(3)
fig.suptitle('Cos Functions')
axs[0].plot(t, xt, 'tab:blue')
axs[0].set_ylabel('x(t)')
axs[1].plot(t, yt, 'tab:orange')
axs[1].set_ylabel('y(t)')
axs[2].plot(t, zt, 'tab:green')
axs[2].set_ylabel('z(t)')

plt.show()

# c)
T = 1.0/200 # fa=200Hz; T=1/fa
t1 = np.arange(0, 0.3, T)
xt1 = np.cos(520*np.pi*t1 + np.pi/3)
yt1 = np.cos(280*np.pi*t1 - np.pi/3)
zt1 = np.cos(120*np.pi*t1 + np.pi/3)

fig, axs = plt.subplots(3)
fig.suptitle('Cos Functions Discrete')
axs[0].stem(t1, xt1, 'tab:blue', markerfmt='ob', basefmt=' ')
axs[0].set_ylabel('x(t)')
axs[1].stem(t1, yt1, 'tab:orange', markerfmt='ob', basefmt=' ')
axs[1].set_ylabel('y(t)')
axs[2].stem(t1, zt1, 'tab:green', markerfmt='ob', basefmt=' ')
axs[2].set_ylabel('z(t)')

plt.show()
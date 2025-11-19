import numpy as np
import matplotlib.pyplot as plt



B = 6
t = np.linspace(-3, 3, 1000)
X = np.sinc(B * t) ** 2
plt.plot(t, X, color='blue', lw=1)
#plt.savefig("lab6/ex1_a.pdf", format='pdf')
#plt.show()


fs = [1, 1.5, 2, 4]

fig, axs = plt.subplots(4, 1, figsize=(8, 10), sharex=True, sharey=True)
for Fs, ax in zip(fs, axs):
    Ts = 1.0 / Fs
    n_start = int(np.ceil(-3.0 / Ts))
    n_end   = int(np.floor( 3.0 / Ts))
    n = np.arange(n_start, n_end + 1, dtype=int)
    t_n = n * Ts
    x_n = np.sinc(B * t_n) ** 2

    x_hat = np.zeros_like(t)
    for tn, xn in zip(t_n, x_n):
        x_hat += xn * np.sinc((t - tn) / Ts)

    ax.plot(t, X, color='C0', alpha=0.35, label='x(t)')
    ax.plot(t, x_hat, color='C2', lw=1, label='Reconstruit')
    ax.stem(t_n, x_n, linefmt='C1-', markerfmt='C1o', basefmt=' ')
    ax.set_title(f'Fs = {Fs} Hz (Ts = {Ts:.3f} s)')
    ax.grid(True, alpha=0.3)

axs[0].legend(loc='upper right')
axs[-1].set_xlabel('t (s)')
axs[1].set_ylabel('Amplitudine')
plt.xlim(-3, 3)
plt.tight_layout()
plt.savefig('lab6/ex1_d.pdf', format='pdf')
plt.show()
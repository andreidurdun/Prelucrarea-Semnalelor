import numpy as np
import matplotlib.pyplot as plt


A = 1.0          # amplitudine
phi = 0.0        # faza
fc = 10       # frecventa semnalului de baza
fs = 5    

t_cont = np.linspace(0, 1, 1000, endpoint=False)
t_samp = t_samp = np.arange(0, 1, 1/fs)


f1 = fc
f2 = fc + fs
f3 = fc + 2*fs
f4 = fc + 3*fs

signals = [
    (f1, "blue"),
    (f2, "orange"),
    (f3, "purple"),
    (f4, "green")
]

plt.figure(figsize=(8,8))

for i, (f, color) in enumerate(signals):
    plt.subplot(4, 1, i+1)
    s_cont = A * np.sin(2*np.pi*f*t_cont + phi)
    s_samp = A * np.sin(2*np.pi*f*t_samp + phi)

    plt.plot(t_cont, s_cont, color=color, lw=2, alpha=0.7)
    plt.scatter(t_samp, s_samp, color='yellow', edgecolors='k', s=80, zorder=5)
    plt.xlim(0, 1)
    plt.ylim(-1.1, 1.1)
    plt.grid(True, alpha=0.3)
    plt.ylabel(f"f = {f:.0f} Hz")
    if i == len(signals) - 1:
        plt.xlabel("Timp (s)")

plt.tight_layout(rect=[0, 0, 1, 0.97])

plt.savefig("ex2.pdf", format='pdf')
plt.show()

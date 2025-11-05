import numpy as np
import matplotlib.pyplot as plt



t = np.linspace(0,1,2000)
x = np.sin(2*np.pi*25*t) + np.sin(2*np.pi*30*t) + np.sin(2*np.pi*100*t)

plt.plot(t, x)
plt.savefig("ex3f1.pdf", format='pdf')
plt.show()

#DFT
n = len(t)
X = []  
for i in range(n):
    s = 0
    for k in range(n):
        s += x[k] * np.exp(-2j * np.pi * k * i / n)
    X.append(s)
X = np.array(X)
mod = np.abs(X)
fs = 1 / (t[1] - t[0]) #frecv de esant
fa = np.linspace(0, fs, n)
plt.stem(fa[:n//2], mod[:n//2])
plt.savefig("ex3f2.pdf", format='pdf')
plt.show()
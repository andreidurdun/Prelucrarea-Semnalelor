import numpy as np
import time
import matplotlib.pyplot as plt


def DFT(x):
    x = np.asarray(x, dtype=complex)
    n = x.shape[0]
    X = np.empty(n, dtype=complex)
    for i in range(n):
        s = 0j
        for k in range(n):
            s += x[k] * np.exp(-2j * np.pi * k * i / n)
        X[i] = s
    return X

def FFT(x):
    x = np.asarray(x, dtype=complex) # array de numere complexe
    N = x.shape[0]

    if N <= 1:
        return x
    
    if N % 2 != 0:
        raise ValueError("Input-ul trebuie sa fie putere a lui 2")
    
    even = FFT(x[::2])
    odd = FFT(x[1::2])

    factor = np.exp(-2j * np.pi * np.arange(N) / N) 
    return np.concatenate([even + factor[:N // 2] * odd, even - factor[:N // 2] * odd])


Ns = [128, 256, 512, 1024, 2048, 4096, 8192]
timesDFT = []
timesFFT = []
timesNP = []

for N in Ns:
    x = np.random.random(N)
    
    #DFT
    start = time.time()
    DFT(x)
    timesDFT.append(time.time() - start)
    
    #FFT
    start = time.time()
    FFT(x)
    timesFFT.append(time.time() - start)
    
    #Numpy FFT
    start = time.time()
    np.fft.fft(x)
    timesNP.append(time.time() - start)

plt.figure(figsize=(8, 5))
plt.plot(Ns, timesDFT, 'o-', label='DFT')
plt.plot(Ns, timesFFT, 'o-', label='FFT')
plt.plot(Ns, timesNP, 'o-', label='NumPy FFT')
plt.legend()
plt.yscale('log')
plt.xlabel('Dimensiunea vectorului N')
plt.ylabel('Timp de executie')


plt.savefig("ex1.pdf", format='pdf')
plt.show()


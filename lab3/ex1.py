import numpy as np
import matplotlib.pyplot as plt


N = 8
F = np.zeros((N,N), dtype=complex)
for im in range(N):
    for jm in range(N):
        F[im,jm] = np.exp((-2* np.pi * 1j * im * jm) / N)

fig, axs = plt.subplots(N, 1, figsize=(6, N*2+1))
for ix in range(N):
    axs[ix].plot(F[ix].real, label='real')
    axs[ix].plot(F[ix].imag, label='imaginar')

plt.savefig("ex1.pdf", format='pdf')
plt.show()

FH = np.conj(np.transpose(F))
print(np.allclose(FH @ F, N * np.eye(N), atol=1e-5)) # np.eye = matr identitate de dim N*N
# @ = inmultire matriceala
# np.allclose = verifica daca doua matrice sunt aproximativ egale
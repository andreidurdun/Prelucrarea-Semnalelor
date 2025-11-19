import numpy as np
import matplotlib.pyplot as plt

n = 20
d = 3

x = np.random.rand(n)
y = np.roll(x, d)

X = np.fft.fft(x)
Y = np.fft.fft(y)

prod_fft = np.fft.ifft(np.conj(X) * Y)
div_fft = np.fft.ifft(Y / X)

print(f"Produs: {np.argmax(np.abs(prod_fft))}\nImpartire: {np.argmax(np.abs(div_fft))}")

fig , axs = plt.subplots(2, 1)
axs[0].plot(np.abs(prod_fft))
axs[0].set_title('Produs')
axs[1].plot(np.abs(div_fft))
axs[1].set_title('Impartire')
plt.savefig('lab6/ex4.pdf', format='pdf')
plt.show()

# Graficul formulei cu impartire arata un varf la pozitia d si in rest 0 (similar cu Dirac), iar formula cu produs arata un varf maxim la pozitia d si apoi mai multe valori mai mici
import numpy as np

n = 20
d = 3

x = np.random.rand(n)
y = np.roll(x, d)

X = np.fft.fft(x)
Y = np.fft.fft(y)

prod_fft = np.fft.ifft(X * Y)
div_fft = np.fft.ifft(Y / X)

print(f"Produs: {np.argmax(np.abs(prod_fft))}\nImpartire: {np.argmax(np.abs(div_fft))}")

# Formula cu impartire reuseste sa recupereze deplasarea d, iar formula cu inmultire nu reuseste
import numpy as np


p = np.random.randint(0, 10, 50)
q = np.random.randint(0, 10, 50)

prod_conv = np.convolve(p, q)

prod_clasic = np.zeros(len(p) + len(q) - 1)
for i in range(len(p)):
    for j in range(len(q)):
        prod_clasic[i + j] += p[i] * q[j]


p_fft= np.fft.fft(p, n=len(prod_conv))
q_fft= np.fft.fft(q, n=len(prod_conv))

prod_fft = np.fft.ifft(p_fft * q_fft)


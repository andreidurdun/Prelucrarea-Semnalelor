import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)  

fig, axs = plt.subplots(4, 1)
for i in range(4):
    axs[i].plot(x)
    x = np.convolve(x, x)
    axs[i].legend()

plt.savefig('lab6/ex2.pdf', format='pdf')
plt.show()

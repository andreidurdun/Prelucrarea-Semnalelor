import numpy as np
import matplotlib.pyplot as plt
import math

f = 10  
esantion = 500  
t = np.linspace(0,1,2000)
x = np.sin(2 * np.pi * f * t)


fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t, x)
axs[0].plot(t[esantion], x[esantion]) 

#infasurare semnal in planul complex
y = x * np.exp(-2j * np.pi * t)
axs[1].plot(y.real, y.imag) 
axs[1].set_aspect('equal', adjustable='box')
axs[1].plot(t[esantion], x[esantion])
plt.savefig("ex2f1.pdf", format='pdf')
plt.show()


O = [1,2,5,7]
fig, axs2 = plt.subplots(1,4)
for i, o in enumerate(O):
    z = x * np.exp(-2j * np.pi * t * o)
    axs2[i].plot(z.real, z.imag)
    axs2[i].axhline(0, color='black', linewidth=1)
    axs2[i].axvline(0, color='black', linewidth=1)
    axs2[i].set_aspect('equal', adjustable='box')  
plt.tight_layout()
plt.savefig("ex2f2.pdf", format='pdf')
plt.show()



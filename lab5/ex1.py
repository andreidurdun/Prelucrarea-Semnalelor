import numpy as np
from datetime import datetime


x = np.genfromtxt('lab5/archive/Train.csv', delimiter=',', skip_header=1, dtype=str) # citesc datele

#X = np.fft.fft(x) #transformata Fourier
#N = len(X)

#X = abs(X/N)
#X = X[0:N//2] #iau doar jumatate deoarece este simetrica

#f = fs*np.linspace(0,N/2,N/2)/N # vectorul de frecvente pt care e calc transformata


def a():
    # fs = un esantion / ora(3600s) => fs = 1/3600 Hz = 0.0002778 Hz
    return 0

def b():
    x = np.genfromtxt('lab5/archive/Train.csv', delimiter=',', skip_header=1, dtype=str) #
    date = [datetime.strptime(d, '%d-%m-%Y %H:%M') for d in x[:, 1]]
    prima_zi = date[0]
    ultima_zi = date[-1]
    durata = ultima_zi - prima_zi

    print (durata) # 761 zile si 23 ore

b()
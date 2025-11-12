import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

x = np.genfromtxt('lab5/archive/Train.csv', delimiter=',', skip_header=1, dtype=str) # citesc datele

#X = np.fft.fft(x) #transformata Fourier
#N = len(X)

#X = abs(X/N)
#X = X[0:N//2] #iau doar jumatate deoarece este simetrica

#f = fs*np.linspace(0,N/2,N/2)/N # vectorul de frecvente pt care e calc transformata


def a():
    # fs = un esantion / ora(3600s) => fs = 1/3600 Hz = 0.0002778 Hz
    x = np.genfromtxt('lab5/archive/Train.csv', delimiter=',', skip_header=1, dtype=str) #
    date = [datetime.strptime(d, '%d-%m-%Y %H:%M') for d in x[:, 1]]
    frecv = date[1] - date[0]
    fs = 1 / frecv.total_seconds()
    #print(fs) 
    return fs



def b():
    x = np.genfromtxt('lab5/archive/Train.csv', delimiter=',', skip_header=1, dtype=str) #
    date = [datetime.strptime(d, '%d-%m-%Y %H:%M') for d in x[:, 1]]
    prima_zi = date[0]
    ultima_zi = date[-1]
    durata = ultima_zi - prima_zi

    return (durata) # 761 zile si 23 ore


def c():
    frecv_max = a() / 2 # fs / 2
    return frecv_max # 0.0001388889 Hz

def d():
    x = np.genfromtxt('lab5/archive/Train.csv', delimiter=',', skip_header=1, usecols=2) # citesc datele
    media = np.mean(x)
    x = x - media
    X = np.fft.fft(x) #transformata Fourier
    N = len(X)

    X = abs(X/N)
    X = X[0:N//2] #iau doar jumatate deoarece este simetrica

    f = a()*np.linspace(0,N/2,N//2)/N # vectorul de frecvente pt care e calc transformata
    plt.plot(f, X, color='blue', lw=1)
    plt.yscale('log')
    plt.savefig("d.pdf", format='pdf')
    plt.show()

def e():
    #are comp continua daca media semnalului e dif de 0
    x = np.genfromtxt('lab5/archive/Train.csv', delimiter=',', skip_header=1, usecols=2)
    media = np.mean(x)

    #scadem media din semnal pt a elimina comp continua
    x = x - media
    
    X = np.fft.fft(x) #transformata Fourier
    N = len(X)

    X = abs(X/N)
    X = X[0:N//2] #iau doar jumatate deoarece este simetrica

    f = a()*np.linspace(0,N/2,N//2)/N # vectorul de frecvente pt care e calc transformata
    plt.plot(f, X, color='blue', lw=1)
    plt.yscale('log')
    plt.savefig("e.pdf", format='pdf')
    plt.show()

def f():
    x = np.genfromtxt('lab5/archive/Train.csv', delimiter=',', skip_header=1, usecols=2)
    media = np.mean(x)

    #scadem media din semnal pt a elimina comp continua
    x = x - media
    
    X = np.fft.fft(x) #transformata Fourier
    N = len(X)

    X = abs(X/N)
    X = X[0:N//2] #iau doar jumatate deoarece este simetrica

    indici_max = np.argsort(X)[-4:][::-1] #indicii celor mai mari 4 valori
    fs = a()
    f = fs*np.linspace(0,N/2,N//2)/N
    
    for i in indici_max:
        frecv = f[i]
        perioada = 1 / frecv # in secunde

        ore = perioada / 3600
        zile = ore / 24
        saptamani = zile / 7
        luni = zile / 30
        ani = luni / 12

        if ani >= 1:
            print(f"Indice: {i}, Frecventa: {frecv} Hz, Perioada: {ani:.2f} ani")
        elif luni >= 1:
            print(f"Indice: {i}, Frecventa: {frecv} Hz, Perioada: {luni:.2f} luni")
        elif saptamani >= 1:
            print(f"Indice: {i}, Frecventa: {frecv} Hz, Perioada: {saptamani:.2f} saptamani")
        elif zile >= 1:
            print(f"Indice: {i}, Frecventa: {frecv} Hz, Perioada: {zile:.2f} zile")
        elif ore >= 1:
            print(f"Indice: {i}, Frecventa: {frecv} Hz, Perioada: {ore:.2f} ore")
        else:
            print(f"Indice: {i}, Frecventa: {frecv} Hz, Perioada: {perioada:.2f} secunde")


    
def g():
    x = np.genfromtxt('lab5/archive/Train.csv', delimiter=',', skip_header=1, dtype=str) 
    date = [datetime.strptime(d, '%d-%m-%Y %H:%M') for d in x[:, 1]]

    zi_start = 0
    for i, d in enumerate(date):
        if d.day == 1 and d.weekday() == 0:
            zi_start = i
            break

    x = x[zi_start : zi_start + 30 * 24 , 2].astype(float)

    nr_esantioane = 30 * 24  
    date_luna = date[zi_start:zi_start + nr_esantioane]

    plt.plot(date_luna, x, color='blue', lw=1)
    plt.savefig("lab5/g.pdf", format='pdf')
    plt.show()

# h) Deoarece este cunoscut ca traficul este mult mai intens in timpul saptamanii decat in weekend, 
# putem observa o diferenta clara intre duminica si luni, respectiv intre vineri si sambata.
# In continuare, putem determina periodicitatea semnalului si sa incercam sa vedem daca corespunde cu o saptamana 
# Neajunsuri: Lipsa de date pentru anumite perioade; Traficul depinde si de alti factori (sarbatori legale, evenimente etc.); 

def i():
    
    x = np.genfromtxt('lab5/archive/Train.csv', delimiter=',', skip_header=1, usecols=2)
    media = np.mean(x)

    #scadem media din semnal pt a elimina comp continua
    x = x - media
    
    X = np.fft.fft(x) #transformata Fourier
    N = len(X)

    X = abs(X/N)
    X = X[0:N//2] #iau doar jumatate deoarece este simetrica
    fs = a()
    f = fs*np.linspace(0,N/2,N//2)/N

    fc = 1.0 / (24 * 3600.0) # frecv pt 24h

    plt.figure(figsize=(10, 5))
    plt.plot(f, X, label='Spectrul Semnalului (fara DC)')
    
    plt.axvline(x=fc, color='red', linestyle='--', label=f'1 Ciclu/Zi ({fc:.8f} Hz)')
    
    plt.xlabel('Frecventa')
    plt.ylabel('Amplitudine')
    
    #plt.xlim(0, fc * 4) 
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plt.savefig("lab5/i.pdf", format='pdf')
    plt.show()


i()
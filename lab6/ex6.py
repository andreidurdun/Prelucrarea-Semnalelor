import numpy as np
import matplotlib.pyplot as plt
import scipy 

x = np.genfromtxt('lab6/data/Train.csv', delimiter=',', skip_header=1, usecols=2)

x = x[0 : 3*24] # primele 3 zile

media = np.mean(x)
x = x - media

X = np.fft.fft(x)
N = len(X)
X = np.abs(X / N)[:N // 2] #iau doar jumatate deoarece este simetrica
fs = 1
f = fs*np.linspace(0,N/2,N//2)/N

def b():
    t = np.arange(len(x))
    W = [5, 9, 13, 17]

    plt.plot(t, x, 'k-', label='Semnal original')

    for w in W:
        x_filtrat = np.convolve(x, np.ones(w), 'valid') / w
        plt.plot(np.arange(len(x_filtrat)), x_filtrat, label=f'Filtru medie {w}')

    plt.legend()
    plt.savefig("lab6/filtru_medie.pdf", format='pdf')
    plt.show()

def c():
    fs = 1/3600
    fCut = 1/(12*3600)  # frecventa de taiere 1/12 ore
    fNyquist = fs / 2
    Wn = fCut / fNyquist  # f de taiere normalizata

    print("Frecv de taiere: ", fCut)
    print("Frecv Nyquist: ", fNyquist)
    print("Frecv taiere normalizata: ", Wn)


def d():
    
    N = 5
    rp = 5 #dB

    Wn = 0.1666

    b_butt, a_butt = scipy.signal.butter(N, Wn, btype='lowpass', analog=False)

    b_cheby, a_cheby = scipy.signal.cheby1(N, rp, Wn, btype='lowpass', analog=False)
    
    #raspuns in frecventa
    w_butt, h_butt = scipy.signal.freqz(b_butt, a_butt, worN=2000)
    w_cheby, h_cheby = scipy.signal.freqz(b_cheby, a_cheby, worN=2000)



    plt.plot(w_butt, 20*np.log10(np.abs(h_butt)), 'r-', label=f'Butterworth', linewidth=2)

    plt.plot(w_cheby, 20*np.log10(np.abs(h_cheby)), 'b--', label=f'Chebyshev', linewidth=2)

    plt.legend()
    plt.savefig("lab6/ex6_d.pdf", format='pdf')
    
    plt.show()

    # e) Filtrul Chebyshev urmareste mai bine semnalul decat Butterworth, prin urmare voi alege filtrul Chebyshev
    x_butt = scipy.signal.filtfilt(b_butt, a_butt, x)
    x_cheby = scipy.signal.filtfilt(b_cheby, a_cheby,x)

    plt.plot(x, label='Semnal original')
    plt.plot(x_butt, label='Filtru Butterworth')
    plt.plot(x_cheby, label='Filtru Chebyshev')
    plt.legend()
    plt.savefig("lab6/ex6_e.pdf", format='pdf')
    plt.show()

    # f) 
    N1 = [2, 8]
    RP = [1, 12]

    for n in N1:
        b_butt, a_butt = scipy.signal.butter(n, Wn, btype='low')
        x_butt = scipy.signal.filtfilt(b_butt, a_butt, x)
        plt.plot(x_butt, label=f'Butterworth N={n}')

        for rp in RP:
            b_cheby, a_cheby = scipy.signal.cheby1(n, rp, Wn, btype='low')
            x_cheby = scipy.signal.filtfilt(b_cheby, a_cheby, x)
            plt.plot(x_cheby, label=f'Chebyshev N={n} Rp={rp}dB')

    plt.legend()
    plt.savefig("lab6/ex6_f.pdf", format='pdf')
    plt.show()

d()

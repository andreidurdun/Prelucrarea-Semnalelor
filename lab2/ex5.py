import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wavfile


durata = 3 # secunde
Fs_b = 44100


t_b = np.linspace(0, durata, Fs_b * durata) # vectorul timpului

x_b = np.sin(2 * np.pi * 22050 * t_b)
x_a = np.sin(2 * np.pi * 2000* t_b)

con = np.concatenate((x_b, x_a))

sd.play(con.astype(np.float32), Fs_b)
sd.wait()

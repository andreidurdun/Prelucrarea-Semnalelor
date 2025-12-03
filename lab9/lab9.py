import numpy as np
from scipy.optimize import minimize
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
from matplotlib import pyplot as plt

def ex1():
    N = 1000
    t = np.linspace(0, 1, N)

    trend = 2*t**2 - 3*t + 5
    sezon = 10 * np.sin(2 * np.pi * 5 * t) + 5 * np.sin(2 * np.pi * 20 * t)
    noise = np.random.normal(0, 2, N)

    x = trend + sezon + noise
    return x


# Ex2)
def mediere(x, alpha):
    #s[t] = alpha * x[t] + (1 - alpha) * s[t-1]
    
    rez = [x[0]]
    for n in range(1, len(x)):
        prev_s = rez[-1]
        val = alpha * x[n] + (1 - alpha) * prev_s
        rez.append(val)
    return np.array(rez)
    
x = ex1()
x_med = mediere(x, 0.05)
plt.plot(x, label='Semnal original')
plt.plot(x_med, label='Semnal mediat')
plt.legend()
plt.savefig('lab9/ex2.pdf', format='pdf')
plt.close()


def gaseste_parametri(func, data, p0, bounds, method_name, **kwargs):
    
    def objective(params):
        preds = func(data, *params, **kwargs)
        return mean_squared_error(data, preds)
    # minimizam mse
    res = minimize(objective, p0, bounds=bounds, method='L-BFGS-B')
    return res.x, res.fun

alpha_opt, mse_simp = gaseste_parametri(mediere, x, [0.5], [(0, 1)], "SES")
simpl_opt = mediere(x, alpha_opt[0])
plt.plot(x, label='Semnal original')
plt.plot(simpl_opt, label='Semnal optimizat med simpla')
plt.legend()
plt.savefig('lab9/ex2_opt1.pdf', format='pdf')
plt.close()

def mediere_dubla(x, alpha, beta):
    """
    l[t] = alpha * x[t] + (1 - alpha) * (l[t-1] + b[t-1])
    b[t] = beta * (l[t] - l[t-1]) + (1 - beta) * b[t-1]
    y[t] = l[t] + b[t]
    """

    rez = []
    l, b = x[0], x[1] - x[0] 
    rez.append(l + b)
    
    for n in range(1, len(x)):
        prev_l = l
        l = alpha * x[n] + (1 - alpha) * (l + b)
        b = beta * (l - prev_l) + (1 - beta) * b
        rez.append(l + b)
        
    return np.array([x[0]] + rez[:-1])

alpha_beta_opt, mse_dubla = gaseste_parametri(mediere_dubla, x, [0.5, 0.5], [(0, 1), (0, 1)], "DES")
dubla_opt = mediere_dubla(x, alpha_beta_opt[0], alpha_beta_opt[1])
plt.plot(x, label='Semnal original')
plt.plot(dubla_opt, label='Semnal optimizat med dubla')
plt.legend()
plt.savefig('lab9/ex2_opt2.pdf', format='pdf')
plt.close()

def mediere_tripla(x, alpha, beta, gamma, s_perioada):
    """
    l[t] = alpha * (x[t] - s[t - p]) + (1 - alpha) * (l[t-1] + b[t-1])
    b[t] = beta * (l[t] - l[t-1]) + (1 - beta) * b[t-1]
    s[t] = gamma * (x[t] - l[t]) + (1 - gamma) * s[t - p]
    y[t] = l[t] + b[t] + s[t - p]
    """

    rez = []
    
    l = x[0]
    b = (x[s_perioada] - x[0]) / s_perioada 
    
    s = []
    for i in range(s_perioada):
        s.append(x[i] - l)
        
    rez.append(l + b + s[0])

    for n in range(1, len(x)):
        val_curenta = x[n]
        idx_sezon = n % s_perioada
        
        s_vechi = s[idx_sezon] 
        prev_l = l
        
        l = alpha * (val_curenta - s_vechi) + (1 - alpha) * (prev_l + b)
        b = beta * (l - prev_l) + (1 - beta) * b
        
        s_nou = gamma * (val_curenta - l) + (1 - gamma) * s_vechi
        s[idx_sezon] = s_nou
        
        y_fit = l + b + s_vechi
        rez.append(y_fit)

    return np.array([x[0]] + rez[:-1])

alpha_beta_gamma_opt, mse_tr = gaseste_parametri(mediere_tripla, x, [0.5, 0.5, 0.5], [(0, 1), (0, 1), (0, 1)], "TES", s_perioada=20)
tr_opt = mediere_tripla(x, alpha_beta_gamma_opt[0], alpha_beta_gamma_opt[1], alpha_beta_gamma_opt[2], s_perioada=20)
plt.plot(x, label='Semnal original')    
plt.plot(tr_opt, label='Semnal optimizat med tripla')
plt.legend()
plt.savefig('lab9/ex2_opt3.pdf', format='pdf')
plt.close()
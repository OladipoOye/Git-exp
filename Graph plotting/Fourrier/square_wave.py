import numpy as np 
import matplotlib.pyplot as plt

def plot(n, d):
    #  purely odd
    an_terms = np.zeros(n+1)
    bn_terms = []
    f = []
    t = np.linspace(-np.pi, np.pi, n)
    for i in range(1, n+1):
        bn_terms.append((2 * (1 - ((-1)**i)) / i / np.pi) * np.sin(i*t[i-1]))
        f.append(d + bn_terms[i-1] + an_terms[i-1])
    plt.plot(t, f, 'r')
    plt.plot(t, np.zeros(len(t)), 'g')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.show()


plot(15, 0)
    
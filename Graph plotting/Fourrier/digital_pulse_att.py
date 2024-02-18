import numpy as np
import matplotlib.pyplot as plt


def plot(n=5, T=np.pi, d=0):
    an_term = []
    bn_term = []
    f = []
    t = np.linspace(0, 2*np.pi, 50)
    for i in range(n):
        an_term.append(np.sin(i*T) / i / np.pi * np.cos(i*t))
        bn_term.append((1 - np.cos(i*T)) / i / np.pi * np.sin(i*t))
        f.append(an_term[i] + bn_term[i])
    final = [ j + T/2/np.pi for j in f]
    plt.plot(t, final, 'r', label='fourrier q1')
    plt.xlabel('t')
    plt.ylabel('f(t)')
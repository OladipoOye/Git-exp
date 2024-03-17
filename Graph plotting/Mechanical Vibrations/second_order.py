import numpy as np
import math
import matplotlib.pyplot as plt

#dashpot and spring in parallel
# equation is yddot / (w_n)^2  + 2*zeta*ydot/ (w_n) + y = x 
# x0 will be the step
# zeta = lamda/2*sqrt(km)
# w_n = sqrt(k/m)
def step_underd(N, w_n, zeta, x0):
    w_d = w_n * np.sqrt(1 - (zeta**2))
    phi = math.atan(zeta * w_d / w_n)
    t_list = np.linspace(0, 5, N-1)
    y_list = []
    approx_list = []
    def y_actual(t):
        y = x0 *(1 - (np.exp(-zeta*w_n*t)*np.cos(w_d*t - phi) / np.cos(phi)))
        return y
    
    def y_approx(t):
        y = x0 *(1 - (np.exp(-zeta*w_n*t)*np.cos(w_d*t - phi)))
        return y
    
    for i in range(N-1):
        y_list.append(y_actual(t_list[i]))
        approx_list.append(y_approx(t_list[i]))
    
    plt.plot(t_list, y_list, 'g', label='step response for second order')
    plt.plot(t_list, approx_list, 'm*', label='small angle approx')
    plt.xlabel('time')
    plt.ylabel('displacement')
    plt.legend()
    plt.show()
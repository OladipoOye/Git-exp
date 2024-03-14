import numpy as np
import matplotlib.pyplot as plt

# spring in the front, dashpot at the back and grounded
# equation is T*ydot + y = x0 * H(t)
# T = lambda / k

def step(N, lamda, k, x0):
    t_list = np.linspace(0, 5, N-1)
    T = lamda / k 
    y_values = []
    print('step is', x0, ', Time const is', T, ', N is', N)
    print('t values are:', t_list)
    
    def y_step(t):
        y = x0 * (1 - np.exp(-t/T)) 
        return y

    for i in range(N-1):
        sol = y_step(t_list[i])
        y_values.append(sol)
    print('y list is', y_values)
    plt.plot(t_list, y_values, 'g', label='Dashpot and spring in series')
    plt.xlabel('Time (s)')
    plt.ylabel('Step response of dashpot, y, (m)')
    plt.show()
    
step(80, 1, 10, 0.5)

def impulse(N, lamda, k, I):
    t_list = np.linspace(0, 5, N-1)
    T = lamda / k
    y_values = []
    
    def y_impulse(t):
        y = I / T * np.exp(-t/T)
        return y 
    
    for i in range(N-1):
        sol = y_impulse(t_list[i])
        y_values.append(sol)
    
    plt.plot(t_list, y_values, 'r', label='Dashpot and spring in series')
    plt.xlabel('Time (s)')
    plt.ylabel('Impulse response of dashpot y (m)')
    plt.show()
    
impulse(80, 1, 10, 0.5)
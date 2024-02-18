import numpy as np
import matplotlib.pyplot as plt
#  from ipywidgets import interact


def plot(u=0.1, N=10, v0=20):
    g = 9.8
    dt = 1/N
    t = np.linspace(0, 20, N-1)
    xddot = np.zeros(N)
    xdot = np.zeros(N)
    # adding a v0 term
    xdot[0] = v0
    xe = np.zeros(N)
    xs = np.zeros(N)
    # setting the initial distance to 50
    euler = []
    semi = []
    # equation of motion
    
    def z(x):
        y = -u*g*(x**2)/2 + v0*x 
        if x < 10:
            print('x is', x, 'acceleration is', -u*g*(x**2)/2, 'u is', u, 'g is', g) 
        return y
    # list of y values
    lis = []
    for n in range(1, N):
        xddot[n-1] = -u*g
        xdot[n] = xdot[n-1] + (xddot[n-1] * dt)
        xe[n] = xe[n-1] + (xdot[n-1] * dt)
        euler.append(xe[n])
        xs[n] = xs[n-1] + (xdot[n] * dt)
        semi.append(xs[n])
        lis.append(z(t[n-1]))
    plt.plot(t, euler, 'g', label='euler')
    plt.plot(t, semi, 'c', label='semi-implicit')
    plt.plot(t, lis, 'r', label='analytic')
    plt.xlabel('time')
    plt.ylabel('distance')
    plt.title('deceleration of car')
    plt.legend()
    plt.show()


#interact(plot, u=[0.01, 0.99, 0.04], N=[10, 100, 10])
plot(u=0.3, N=10, v0=5)

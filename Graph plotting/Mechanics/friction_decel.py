import numpy as np
import matplotlib.pyplot as plt
#  from ipywidgets import interact


def plot(u=0.1, N=10, v0=20, d0=50):
    g = 9.8
    dt = 1/N
    t = np.linspace(0, 10, N-1)
    xddot = np.zeros(N)
    xdot = np.zeros(N)
    # adding a v0 term
    xdot[0] = v0
    xe = np.zeros(N)
    xs = np.zeros(N)
    # setting the initial distance to 50
    xe[0] = d0
    xs[0] = d0
    euler = []
    semi = []
    for n in range(1, N):
        xddot[n-1] = -u*g
        xdot[n] = xdot[n-1] + (xddot[n-1] * dt)
        xe[n] = xe[n-1] + (xdot[n-1] * dt)
        euler.append(xe[n])
        xs[n] = xs[n-1] + (xdot[n] * dt)
        semi.append(xs[n])
    plt.plot(t, euler, 'g', label='euler')
    plt.plot(t, semi, label='semi-implicit')
    plt.xlabel('time')
    plt.xlim(0, 30)
    plt.ylabel('distance')
    plt.title('deceleration of car')
    #  plt.plot(t, (-u*g*(t**2)/2) + (25t) + 50, 'r', label='analytic')
    plt.legend()
    plt.show()


#interact(plot, u=[0.01, 0.99, 0.04], N=[10, 100, 10])
plot(N=40, v0=10)
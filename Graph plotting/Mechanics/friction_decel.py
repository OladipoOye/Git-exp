import numpy as np
import matplotlib.pyplot as plt
#  from ipywidgets import interact


def plot(u, N, v0):
    g = 9.8
    dt = 20/N
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
    def z(t1):
        y = -u*g*(t1**2)/2 + v0*t1
        if t1 < 10:
            print('time  is', t1, "seconds,", 'acceleration term is', -u*g*(t1**2)/2, 'u is', u, 'g is', g) 
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
plot(u=0.3, N=80, v0=60)

#def z(t1):
    #u = 0.3
    #g = 9.8
    #v0 = 50
    #y = -u*g*(t1**2)/2 + v0*t1 
    #if t1 < 10:
        #print('time  is', t1, "seconds,", 'acceleration term is', -u*g*(t1**2)/2, ',acceleration is', -u*g, ',u is', u, 'g is', g) 
    #return y

#test = []
#for i in range(0, 10):
    #test.append(z(i))
    #print("iteration is", i, "function is", test)
    
#test2 = np.linspace(0, 10, 100)
#test2_comp = []
#for i in range(len(test2)):
    #test2_comp
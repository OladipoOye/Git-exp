import numpy as np
import math
import matplotlib.pyplot as plt
# question 3 

# one sided taylor series differential approximation


def f(x):
    f = x*3 + 5
    return f


def taylor_approx(n, h):
    x = np.linspace(-20, 20, n)
    one = []
    two = [] 
    #h_list = []
    #h2_list = [] 
    
    #for i in range(len(x)):
    #    one.append(((f(x[i]+h) - f(x[i])) / h) - (3*(x[i]**2)))
    #    two.append(((f(x[i]+h) - f(x[i]-h)) / 2*h) - (3*(x[i]**2)))
    #    h_list.append(h*x[i])
    #    h2_list.append((h**2)*x[i])
    #plt.plot(x, one, 'rx', label='onesided')
    #plt.plot(x, two, 'gx', label='twosided')
    #plt.plot(x, h_list, 'm', label='O(h)')
    #plt.plot(x, h2_list, 'b', label='O(h^2)')
    #plt.legend()
    #plt.show()
    
    for i in range(len(x)):
        taylor1 = (f(x[i]+h) - f(x[i])) / h
        taylor2 = (f(x[i]+h) - f(x[i]-h)) / 2*h
        actual =  3*(x[i]**2)
        one.append( (taylor1 - actual) / h)
        two.append( (taylor2 - actual) / h**2)
    plt.plot(x, one, 'rx', label='onesided')
    plt.plot(x, two, 'gx', label='twosided')
    plt.legend()
    plt.show()
    
    
#taylor_approx(100, 0.01)

# question 4
# function is x squared * sine(x squared)

def comparison(x, h):
    def f_1(x):
        f = (x**2) * np.sin(x**2)
         
    actual = (2*x*np.sin(x**2)) + (2*(x**3)*np.cos(x**2))
    z = f_1(x + 1j*h)
    diff_1 = z.imag / h
    diff_2 = (f_1(x+h) - f_1(x-h)) / 2*h
        
    error_complex = diff_1 - actual
    error_twosided = diff_2 - actual
    return "x is,", x, "h is", h, "complex step error is,", error_complex, "two sided error is,", error_twosided

comparison(10, 10**(-9))
comparison(10, 10**(-12))
comparison(10, 10**(-15))
comparison(100, 10**(-9))
comparison(100, 10**(-12))
comparison(100, 10**(-15))
comparison(1000, 10**(-9))
comparison(1000, 10**(-12))
comparison(1000, 10**(-15))
comparison(10000, 10**(-9))
comparison(10000, 10**(-12))
comparison(10000, 10**(-15))
import numpy as np
import matplotlib.pyplot as plt

# test for complex
# must be passed as an array
ar = np.array([1, 2+3j, 2-2j, 5, 5j])
x = ar.real 
y = ar.imag 

plt.plot(x, y, 'gx')
plt.xlabel('real')
plt.ylabel('imaginary')
plt.show()

# the theorem states that e^jnx = (cos(x) + isin(x))^n = cos(nx) + isin(nx)
# form the x list
x = np.linspace(-np.pi, np.pi, 100)
# exponential

#plt.plot()
#Works
# This is my test python file for repositories
import pytest
print("my life is great")
def f(x):
    if x < 0:
     raise ValueError("Not a nice val")
    return x**2 + x**0
print(f(5))
with pytest.raises(ValueError):
 f(-1)
assert f(5) == 26
assert f(4) == 17

# How branches work 
print("Branch start")
import numpy as np
import math
y = np.sqrt(4)
print(f(y))
assert f(y) == f(2)
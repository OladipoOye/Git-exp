# This is my test python file for repositories
print("my life is great")
def f(x):
    if x < 0:
     raise ValueError("Not a nice val")
    return x**2 + x**0
print(f(5))
print(f(-1))
assert f(5) == 26
assert f(4) == 17
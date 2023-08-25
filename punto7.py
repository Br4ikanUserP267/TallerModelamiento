from scipy.integrate import quad
import math

def f(t):
    return t * math.exp(-2*t) * math.sin(t)

result, error = quad(f, 0, math.inf)
print(result)

from scipy.integrate import quad
import math

def f(t):
    return math.exp(-3*t) * (1 - math.sin(3*t))

result, error = quad(f, 0, math.inf)
print(result)

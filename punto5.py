from sympy import symbols, laplace_transform, cos
import math


pi = math.pi
t, s = symbols('t s')
f = 5*cos(t - pi/6)

F = laplace_transform(f, t, s)
print(F[0])

from sympy import symbols, laplace_transform

t, s = symbols('t s')
f = t**2 + 6*t - 3

F = laplace_transform(f, t, s)
print(F[0])

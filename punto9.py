from sympy import symbols, laplace_transform, exp

t, s = symbols('t s')
f = t**3 * exp(-2*t)

F = laplace_transform(f, t, s)
print(F[0])

from sympy import symbols, laplace_transform, exp

t, s = symbols('t s')
f = t * (exp(-t) + exp(2*t))**2

F = laplace_transform(f, t, s)
print(F[0])

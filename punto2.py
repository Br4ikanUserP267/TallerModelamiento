from sympy import symbols, laplace_transform, exp

t, s = symbols('t s')
f = 1 + exp(4*t)

F = laplace_transform(f, t, s)
print(F[0])

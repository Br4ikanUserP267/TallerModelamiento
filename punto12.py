from sympy import symbols, laplace_transform, exp, cos

t, s = symbols('t s')
f = exp(-3*t) * cos(3*t)

F = laplace_transform(f, t, s)
print(F[0])

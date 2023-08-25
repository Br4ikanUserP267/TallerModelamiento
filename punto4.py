from sympy import symbols, laplace_transform, cos, sin

t, s = symbols('t s')
f = cos(5*t) + sin(2*t)

F = laplace_transform(f, t, s)
print(F[0])

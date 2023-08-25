from sympy import symbols, laplace_transform, sin
t, s = symbols('t s')
f = sin(t)**2

F = laplace_transform(f, t, s)
print(F[0])

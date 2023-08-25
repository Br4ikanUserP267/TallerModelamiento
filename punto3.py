from sympy import symbols, laplace_transform, sin

t, s = symbols('t s')
f = 4*t**3 - 5*sin(3*t)

F = laplace_transform(f, t, s)
print(F[0])

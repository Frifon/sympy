from sympy import summation, symbols, Abs, solve

x = symbols('x', integer = True)

solve(Abs(x)-3)

# print summation(1/log(n)**n, (n, 2, oo))
# print summation(i, (i, 0, n), (n, 0, m))
# print summation(i, (i, 1, n))


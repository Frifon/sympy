from sympy import reset_solution, last_solution, symbols, solve

x, y, z = symbols('x, y, z')

reset_solution()
res = (solve([x ** 3 + 4 * x ** 2 * y + y ** 3, y ** 3 + 3 * x ** 2 * y - 4], [x, y], dict = True))
for i in res:
	for j in i:
		print j, i[j]
	print
print
R = last_solution()
for i in R:
	print i
print

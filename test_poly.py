from sympy import reset_solution, last_solution, symbols, roots, Poly, roots

x, y = symbols('x, y')



reset_solution()
# P = Poly(x ** 4 + x ** 3 - 11 * x ** 2 - 5 * x + 30)
# a, P = Poly(P.as_expr()).factor_list()
# print (P)
# res = (roots(Poly(x ** 4 + x ** 3 - 11 * x ** 2 - 5 * x + 30), x))
# res = (roots(Poly(12 * x - 13 * (3 * x + 2) ** 2 + 44), x))
# res = (roots(Poly((x + 1) * (x + 2) * (x + 3) * (x + 4) - 24), x))
# res = (roots(Poly(36 * x ** 4 - 13 * x ** 2 + 1), x))
# res = (roots(Poly(6 * x ** 3 - 11 * x ** 2 - 2 * x + 8), x))
res = (roots(Poly(x ** 4 + 4 * x ** 3 - x ** 2 - 16 * x - 12), x))
for i in res:
	print (i)
R = last_solution()
print ('SOLUTION:')
for i in R:
	print i




exit(0)

# 169 - 174 are pages in Vilenkin
# Here are some tests
# just change the value on "n"
n = 4 # number of the test
# 0 - 169 (1)
# 1 - 169 (2)
# 2 - 170 (1)
# 3 - 170 (2)
# 4 - Test from your letter
# 5 - 174 (# 33 (2))
# 6 - Test from your letter

if (n == 0):
	reset_solution()
	res = (roots(Poly(x ** 4 + x ** 3 - 11 * x ** 2 - 5 * x + 30), x))
	for i in res:
		print (i)
	print
	R = last_solution()
	for i in R:
		print i
	print
elif (n == 1):
	reset_solution()
	res = (roots(Poly(6 * x ** 3 - 11 * x ** 2 - 2 * x + 8), x))
	for i in res:
		print (i)
	print
	R = last_solution()
	for i in R:
		print i
	print
elif (n == 2):
	reset_solution()
	res = (roots(Poly((3 * x + 2) ** 4 - 13 * (3 * x + 2) ** 2 + 36), x))
	for i in res:
		print (i)
	print
	R = last_solution()
	for i in R:
		print i
	print
elif (n == 3):
	reset_solution()
	res = (roots(Poly((x + 1) * (x + 2) * (x + 3) * (x + 4) - 24), x))
	for i in res:
		print (i)
	print
	R = last_solution()
	for i in R:
		print i
	print
elif (n == 4):
	reset_solution()
	res = (roots(Poly(x ** 4 + 4 * x ** 3 - x ** 2 - 16 * x - 12), x))
	for i in res:
		print (i)
	print
	R = last_solution()
	for i in R:
		print i
	print
elif (n == 5):
	reset_solution()
	res = (roots(Poly(36 * x ** 4 - 13 * x ** 2 + 1), x))
	for i in res:
		print (i)
	print
	R = last_solution()
	for i in R:
		print i
	print
elif (n == 6):
	reset_solution()
	res = (roots(Poly(6 * x ** 3 - 11 * x ** 2 - 2 * x + 8), x))
	for i in res:
		print (i)
	print
	R = last_solution()
	for i in R:
		print i
	print
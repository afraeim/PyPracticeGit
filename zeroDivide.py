def sp(divideBy):
	return 42/divideBy
try:
	print(sp(2))
	print(sp(12))
	print(sp(1))
	print(sp(0))
	print(sp(41))
except ZeroDivisionError:
	print("Undefind")
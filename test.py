try:
	i = 10.0**100000
	print(i)
except OverflowError:
	print('Error: Value too large. Please keep it reasonable')
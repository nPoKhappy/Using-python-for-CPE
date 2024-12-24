import math

while 1:
	a, b = map(int, input().split())
	
	if (a == 0 and b == 0):
		break
	count = 0
	for i in range(a, b + 1):
		sqrt_n = math.sqrt(i)
		print(type(sqrt_n))
		if sqrt_n * sqrt_n == i:
			count += 1
	print(count)
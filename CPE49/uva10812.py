def algo(a, b):
	n1 = (a + b) // 2
	n2 = a - n1
	return n1, n2

t = int(input())


for case in range(t):
	a, b = map(int, input().split())
	if (a + b) % 2 != 0:
		print("impossible")
		continue
		
	n1, n2 = algo(a, b)
	if (n2 < 0):
		print("impossible")
	else:
		print(f"{n1} {n2}")
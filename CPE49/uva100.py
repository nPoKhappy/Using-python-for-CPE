def three_n(n1 : int, n2 : int):
	max_n : int = 0
	
	if n1 > n2:
		n1, n2 = n2, n1
	
	for n in range(n1, n2 + 1):
		count : int = 1
		while (n != 1):
			if (n % 2 == 1):
				n = 3 * n + 1
				count += 1
			else:
				n = n / 2
				count += 1
		max_n : int = max(count, max_n)

	return max_n

while 1:
	try:
		n1, n2 = map(int, (input().split()))
		max_cycle : int = three_n(n1, n2)
		print(f"{n1} {n2} {max_cycle}")
	except EOFError:
		break
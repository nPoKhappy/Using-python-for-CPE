



while 1:
	n = int(input())
	if (n == 0):
		break
	n = str(n)
	sum_odd = 0
	sum_even = 0
	for i in range(len(n)):
		if 	(i % 2 == 0):
			sum_odd += int(n[i])
		else:
			sum_even += int(n[i])
	sum = abs(sum_odd - sum_even)
	if (sum == 0 or sum == 11):
		print(f"{n} is a multiple of 11.")
	else:
		print(f"{n} is not a multiple of 11.")
		
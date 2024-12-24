while 1:
	i = int(input())
	if i == 0:
		break
	i_b = bin(i)[2:]
	print(f"The parity of {i_b} is {i_b.count('1')} (mod 2).")
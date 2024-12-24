def primary(a : int, b : int):
	count = 0
	carry = 0
	while (a > 1 or b > 1):
		dig_r1 = a % 10 
		dig_r2 = b % 10
		
		if (dig_r1 + dig_r2 + carry >= 10):
			carry = 1
			count += 1
		else:
			carry = 0
			
		a //= 10
		b //= 10
		
	return count


while 1:
	a, b = map(int, input().split())
	if (a == 0 and b == 0):
		break
	ans = primary(a, b)
	if (ans == 0):
		print("No carry operation.")
	elif (ans == 1):
		print("1 carry operation.")
	else:
		print(f"{ans} carry operations.")


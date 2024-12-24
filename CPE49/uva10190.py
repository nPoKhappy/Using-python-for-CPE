
def algo(n : int, m : int):
	ans = []
	bo = 1
	if (n // m == n):
		bo = 0
		return bo, ans
	
	while 1:
		if (n % m == 0):
			ans.append(n)
			n = n // m
		
		elif (n == 1):
			ans.append(1)
			break
		
		
		else:
			bo = 0
			break
	return bo, ans
			

while 1:
	try:
		n, m = map(int, input().split())
		bo, ans = algo(n, m)
		if (bo):
			print(*ans)
		else:
			print("Boring!")
		
	except EOFError:
		break	
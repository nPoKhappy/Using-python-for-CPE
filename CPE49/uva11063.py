
def b_two(a : list[int]):
	n : int = len(a)
	nums = []
	for i in range(n - 1):
		for j in range(i, n):
			sum : int = a[i] + a[j] 
			if (sum not in nums):
				nums.append(sum)
			else:
				return False
	return True

case = 0

while 1:
	try:
		if (case != 0):
			empty = input()
		case += 1
		N = int(input())
		a = list(map(int, input().split()))
		
		ans : bool = b_two(a)
		if ans:
			print(f"Case #{case}: It is a B2-Sequence.\n")
		else:
			print(f"Case #{case}: It is not a B2-Sequence.\n")
	except EOFError:
		break
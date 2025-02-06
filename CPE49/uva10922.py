
def two_nine(n : int, depth : int):
	s_n : str = str(n)
	sum : int = 0
	
	for c in s_n:
		sum += int(c)
	
	if (sum % 9 != 0):
		return False, 0
	
	if (sum != 9): # Base case
        
		depth += 1
		return two_nine(sum, depth)
	else:
		return True, depth 
	

while 1:
	depth : int = 1
	n : int = int(input())
	if (n == 0):
		break
	ans_bool, ans_depth = two_nine(n, depth)
	if ans_bool:
		print(f"{n} is a multiple of 9 and has 9-degree {ans_depth}.")
	else:
		print(f"{n} is not a multiple of 9.")



def algo(n1, n2):
	ans = 0
	for i in range(n1, n2 + 1):
		if  (i % 2 == 1):
			ans += i
	return ans

t = int(input())

for case in range(t):
	n1 = int(input())
	n2 = int(input()) 
	
	print(f"Case {case + 1}: {algo(n1, n2)}")
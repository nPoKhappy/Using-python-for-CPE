
def fib(nums : list):
	for _ in range(50):
		sum = nums[-1] + nums[-2]
		nums.append(sum)
	return nums

t : int = int(input())
nums = [1, 2]
fib_nums : list = fib(nums)

for _ in range(t):
    n : int = int(input())
    n_copy : int = n
    ans : str = ""
    key = 0
    prev_i = -1
    while (n >= 1):
        for i in range(len(fib_nums)):
            if (fib_nums[i] > n):
                if (prev_i != -1):
                    ans += (i - prev_i - 1) * "0"	
                prev_i = i
                n : int = n - fib_nums[i-1]
                ans += "1"
            if (n == 0 and i - 1 != 0):
                ans += (i - 1) * "0"
            break
    print(f"{n_copy} = {ans} (fib)")
	
	
	
	
	
	
	
	

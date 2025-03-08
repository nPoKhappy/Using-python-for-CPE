
def frequency(line: str) -> list:
	freq: dict = {}
	for c in line:
		c_ascii: int = ord(c)
		if c_ascii in freq:
			freq[c_ascii] += 1
		else:
			freq[c_ascii] = 1
	
	sorted_freq: list = sorted(freq.items(), key = lambda x: (x[1], -x[0]) )
	
	return sorted_freq

count = 0

while 1:
	try:
		
		line: str = str(input())
		if (count >= 1):
			print()
		count += 1
		ans: list = frequency(line)
		for item in ans:
			print(f"{item[0]} {item[1]}")
		
		
		
	except EOFError:
		break 
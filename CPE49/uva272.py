
count = 0

while 1:
	try:
		word : str = input()
		ans = ""
		for char in word:
			if (char == '"' and count == 0):
				ans += '``'
				count = 1
			elif (char == '"' and count == 1):
				ans += "''"
				count = 0
			else:
				ans += char
		print(ans)
	except EOFError:
		break
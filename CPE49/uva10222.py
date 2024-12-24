word_lookup : str = "qwertyuiop[]\\asdfghjkl;'zxcvbnm,./" 


def decode(n : str):
	n : str = n.lower()
	ans : str = ""
	for i in range(len(n)):
		if (n[i] == " "):
			ans += " "
			continue
		index : int = word_lookup.find(n[i])
		length : int = len(word_lookup)
		new_index : int = (index - 2 + length) % length
		ans += word_lookup[new_index]
	
	print(ans)


while 1:
	try:
		n : str = input()
		decode(n)
	except EOFError:
		break
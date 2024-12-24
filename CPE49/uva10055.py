while True:
	try:
		x : int
		y : int
		x, y = map(int, input().split())
	except EOFError:
		break
		
	print(abs(x - y))
	
    
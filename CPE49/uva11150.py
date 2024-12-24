def cola(n : int):
	count = 0
	count += n
	ex = n // 3
	count += ex
	lf = n % 3
	
	if (ex + lf == 2):
		count += 1
		return count
		
	total_left = ex + lf
	
	while (total_left >= 3):
		ex = total_left // 3 
		count += ex
		lf = total_left % 3
		total_left = ex + lf
		
		if total_left == 2:
			count += 1
	return count
	

while 1:
	try:
		n = int(input())
		print(cola(n))
	except EOFError:
		break;
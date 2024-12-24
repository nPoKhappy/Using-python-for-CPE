
months = [10, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]

weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def dooms_day(m : int, d : int):
	index = (d - months[m - 1] + 7 ) % 7 
	return weeks[index]

t = int(input())

for case in range(t):
	m, d = map(int, input().split())
	ans = dooms_day(m, d)
	print(ans)
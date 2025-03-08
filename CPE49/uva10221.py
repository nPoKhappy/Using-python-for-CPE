from math import *


r: float = 6440.0

def satellites(s: float, a: float, deg_min: str):
	if (deg_min == "min"):
		a /= 60
		
	arc: float = 2 * (r + s) * pi * (a / 360.0)
	
	a_radians: float = radians(a)
	chord: float = 2 * (r + s) * sin(a_radians / 2)
	
	return arc, chord

while True:
	try:
		s, a, deg_min = map(str, input().split())
		s: float = float(s)
		a: float = float(a)
		arc, chord = satellites(s, a, deg_min)
		print(f"{arc:.6f} {chord:.6f}")
	except EOFError:
		break
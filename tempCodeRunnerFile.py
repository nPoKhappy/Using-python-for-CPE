a = [1, 2, 3]
b = [4, 5, 6]
zipped = zip(a, b)
a1, b1 = list(zip(*zipped)) # * =>uppacked (1, 4) (2, 5) (3, 6) zip => (1, 2, 3) (4, 5, 6)
print()


print(str(a))
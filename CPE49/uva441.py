from itertools import combinations

results = []

while True:
    line = list(map(int, input().split()))
    k = line[0]
    if k == 0:
        break
    S = line[1:]
    combi = combinations(S, 6)
    result = [" ".join(str(num) for num in combo) for combo in combi]
    results.append(result)

# Print all results with blank lines between test cases (not after the last one)
for i, res in enumerate(results):
    for line in res:
        print(line)
    if i != len(results) - 1:
        print()

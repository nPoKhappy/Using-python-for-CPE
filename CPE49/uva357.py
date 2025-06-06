coins = [1, 5, 10, 25, 50]

MAX = 30001

dp = [0] * MAX
dp[0] = 1

for coin in coins:
    for amount in range(coin, MAX):
        dp[amount] += dp[amount - coin]

while 1:
    try:
        n = int(input())
        m = dp[n]
        if m == 1:
            print(f"There is only 1 way to produce {n} cents change.")
        else:
            print(f"There are {m} ways to produce {n} cents change.")
    except EOFError:
        break


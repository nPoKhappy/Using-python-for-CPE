def is_prime(n: int):
    if n < 2:
        return False
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return False
    return True

while 1:
    n = int(input())
    if n == 0:
        break
    ans = []
    # Find primes num under n
    for prime in range(2, n // 2):
        if is_prime(prime):
            left = n - prime
            if is_prime(left):
                ans.append((prime, left))
                break
    if ans == []:
        print("Goldbach's conjecture is wrong.")
    else:
        num1, num2 = ans[0]
        print(f"{n} = {num1} + {num2}")

    
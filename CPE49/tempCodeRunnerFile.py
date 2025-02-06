def two_nine(n: int, depth: int):
    digit_sum = sum(int(c) for c in str(n))  # Compute sum of digits
    
    if digit_sum % 9 != 0:
        return False, 0  # Not a multiple of 9
    
    if digit_sum == 9:
        return True, depth  # Reached 9
    
    return two_nine(digit_sum, depth + 1)  # ✅ Properly return the recursive call

while True:
    try:
        n = int(input())
        ans_bool, ans_depth = two_nine(n, 1)
        if ans_bool:
            print(f"{n} is a multiple of 9 and has 9-degree {ans_depth}.")
        else:
            print(f"{n} is not a multiple of 9.")
    except EOFError:
        break

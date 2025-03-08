def sum_natural(n: int) -> int:
    if n == 0:
        return 1
    return n * sum_natural(n-1)

sum = sum_natural(4)

print(sum)

def reverse_string(s: str) -> str:
    if s == "":
        return ""
    
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))


def count_digits(n: int) -> int:
    if n == 0:
        return 0
    return 1 + count_digits(n//10)

print(count_digits(12345))

def is_palindrome(s: str) -> bool:
    if s == "":
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False 
    
print(is_palindrome("aoaoa"))


def sum_list(nums: list[int]) -> int:
    if nums == []:
        return 0
    return nums[-1] + sum_list(nums[:-1])

list1 = [1, 2, 3, 4, 5]
print(f"sum of the nums in list : {sum_list(list1)}")

def flatten_list(nested: list) -> list:
    ans: list = []
    for i in range(len(nested)):
        if isinstance(nested[i], list):
            ans.extend(flatten_list(nested[i]))
        else:
            ans.append(nested[i])
    return ans

print(flatten_list([1, [2, [3, [4]]], 5]))

def count_occurrences(lst: list[int], target: int) -> int:
    if lst == []:
        return 0
    if lst[-1] == target:
        return 1 + count_occurrences(lst[:-1], target)
    else:
        return count_occurrences(lst[:-1], target)
    

print(count_occurrences([1, 2, 3, 4, 2, 2, 5], 2) )
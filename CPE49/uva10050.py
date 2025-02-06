def hartals(d: int, nums: list) -> int:
    hartal_days = set()
    
    for num in nums:
        count = num
        while count <= d:
            if count % 7 not in {6, 0}:  
                hartal_days.add(count)
            count += num
    
    return len(hartal_days)


t = int(input())  
for _ in range(t):
    d = int(input())  
    p = int(input())  
    nums = [int(input()) for _ in range(p)]  
    
    print(hartals(d, nums))  


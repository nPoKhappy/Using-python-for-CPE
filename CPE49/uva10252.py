def common(a: str, b: str):
    return sorted(set(a) & set(b))  # Find intersection of characters


while True:
    try:
        a: str = input()
        b: str = input()
        ans : set[str] = common(a, b)
        print("".join(ans))  # Print the sorted common characters as a single string
    except EOFError:
        break

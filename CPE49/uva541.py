row_sums = []
col_sums = []


while 1:
    n = input() # Size of matrix
    if n == 0:
        break

    matrix = []
    # Check if the matrix is parity
    # Read line into matrix
    for _ in range(n):
        row = map(int, input().split())
        matrix.append(row)
    # Sum the row and store into row_sums
    for i in range(n):
        row_sum = 0
        for j in range(n):
            row_sum += matrix[i][j]
        row_sums.append(row_sum)
    # Sum the col and store into col_sums
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        col_sums.append(row_sum)
    
    odd_rows = [i for i in range(n) if row_sums[i] % 2 != 0]
    odd_cols = [j for j in range(n) if col_sums[j] % 2 != 0]

    if len(odd_rows) == 0 and len(odd_cols) == 0:
        print("OK")
    elif len(odd_rows) == 1 and len(odd_cols) == 1:
        print(f"Change bit ({odd_rows[0] + 1},{odd_cols[0] + 1})")
    else:
        print("Corrupt")

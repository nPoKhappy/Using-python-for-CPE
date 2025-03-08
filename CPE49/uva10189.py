def mines(matrix: list[list], n: int, m: int) -> list[list]:
    ans: list[list] = [["0"] * m for _ in range(n)]
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    
    for row in range(n):
        for col in range(m):
            count: int = 0
            if (matrix[row][col] == "*"):
                ans[row][col] = "*"
            else:
                for p_n, p_m in directions:
                    m_n, m_m = p_n + row, p_m + col
                    if (0 <= m_n < n and 0 <= m_m < m and matrix[m_n][m_m] == "*"):
                        count += 1
                ans[row][col] = str(count)
    return ans

case: int = 0

while 1:
    case += 1
    lines_n, cols_m = map(int, input().split())
    if (lines_n == 0 and cols_m == 0):
        break
    if (case > 1):
        print()
    matrix: list[list] = [list(input()) for _ in range(lines_n)]        
    ans: list[list] = mines(matrix, lines_n, cols_m)
    print(f"Field #{case}:")
    for row in ans:
        print("".join(row))

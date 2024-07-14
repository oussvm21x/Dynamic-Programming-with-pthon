def up_2_Reccursion(grid, i, j):
    if not grid:
        return float('inf')
    if i>= len(grid) or j >= len(grid[0]):
        return 0
    if grid[i][j] == 1:
        return 0
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        return 1
    return up_2_Reccursion(grid, i + 1, j) + up_2_Reccursion(grid, i, j + 1)

def up2_Memo(grid , i , j , memo ) :
    if not grid:
        return float('inf')
    if i>= len(grid) or j >= len(grid[0]):
        return 0
    if grid[i][j] == 1:
        return 0
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        return 1
    if memo[i][j] != -1 :
        return memo[i][j]
    else :
        memo[i][j] = up2_Memo(grid, i + 1, j, memo) + up2_Memo(grid, i, j + 1, memo)
        return memo[i][j]

def up2_Dp(grid) :
    if not grid :
        return 0
    m = len(grid)
    n = len(grid[0])
    if grid[0][0] == 1:
        return 0
    if m == 1 and n == 1:
        return 1-grid[0][0]
    dp = [[0 for i in range(n)] for j in range(m)]
    dp[0][0] = 1
    for i in range(1, m):
        if grid[i][0] == 1:
            dp[i][0] = 0
        else :
            dp[i][0] = dp[i-1][0]
    for i in range(1, n):
        if grid[0][i] == 1:
            dp[0][i] = 0
        else :
            dp[0][i] = dp[0][i-1]
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
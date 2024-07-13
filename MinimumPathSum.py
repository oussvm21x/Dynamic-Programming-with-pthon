def mps_Reccursion(grid):
    if not grid:
        return 0
    if len(grid) == 1:
        return sum(grid[0])
    if len(grid[0]) == 1:
        return sum([row[0] for row in grid])
    else:
        return grid[0][0] + min(mps_Reccursion([row[1:] for row in grid]), mps_Reccursion(grid[1:]))


def mps_Memo(grid, i, j, memo):
    if not grid or i >= len(grid) or j >= len(grid[0]):
        return float('inf')
    if len(grid) == 1:
        return sum(grid[0])
    if len(grid[0]) == 1:
        return sum([row[0] for row in grid])
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        return grid[i][j]
    if memo[i][j] != -1:
        return memo[i][j]
    else:
        memo[i][j] = grid[i][j] + min(mps_Memo(grid, i, j + 1, memo), mps_Memo(grid, i + 1, j, memo))
        return memo[i][j]


def mpsDp(grid):
    if not grid :
        return float('inf')
    if len(grid) == 1:
        return sum(grid[0])
    if len(grid[0]) == 1:
        return sum([row[0] for row in grid])
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range (1 , m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range (1 , n) :
        dp[0][j] = dp[0][j-1]+grid[0][j]
    for i in range(1 , m) :
        for j in range(1 , n ) :
            dp[i ][j] = grid[i][j] + min(dp[i-1][j] , dp[i][j-1])

    return dp[m-1][n-1]
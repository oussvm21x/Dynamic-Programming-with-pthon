def uniquePathsReccursion(m , n) :
    if m == 1 or n == 1:
        return 1
    else :
        return uniquePathsReccursion(m-1, n) + uniquePathsReccursion(m, n-1)

def uniquePathsMemo(m , n , memo) :
    if m == 1 or n == 1 :
        return 1
    if memo[m][n] != -1 :
        return memo[m][n]
    else :
        memo[m][n] = uniquePathsMemo(m-1, n, memo) + uniquePathsMemo(m, n-1, memo)
        return memo[m][n]

def uniquePathsDp(m , n ) :
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1
    for i in range(1, m):
        for j in range(1,n) :
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]
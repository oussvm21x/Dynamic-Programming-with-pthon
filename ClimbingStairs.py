#reccurssive approach to solve the problem
def climbingsStaires(n) :
    if n == 1  : return 1
    if n == 2  : return 2
    else:
        return climbingsStaires(n-1) + climbingsStaires(n-2)

#reccurssive approach to solve the problem with memoization
def climbingsStaires_memo(n , memo ) :
    if n in memo : return memo[n]
    if n == 0 : return 0
    if n == 1:
        memo[n] = 1
        return memo[n]
    if n == 2:
        memo[n] = 2
        return memo[n]
    else:
        memo[n] = climbingsStaires_memo(n - 1 , memo) + climbingsStaires_memo(n - 2 , memo)
        return memo[n]

#dynamic programming approach to solve the problem

def climbingsStaires_DP(n) :
    data = [0]*(n+1)
    for i in range(1,n+1) :
        if i == 1: data[1] = 1
        elif i == 2: data[2] = 2
        else : data[i] = data[i-1] + data[i-2]
    return data[n]
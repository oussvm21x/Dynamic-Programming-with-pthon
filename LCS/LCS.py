def lcsRecursion(A, B, i, j):
    if i == len(A) or j == len(B):
        return 0
    elif A[i] == B[j]:
        return 1 + lcsRecursion(A, B, i + 1, j + 1)
    else:
        return max(lcsRecursion(A, B, i + 1, j), lcsRecursion(A, B, i, j + 1))


def lcsMemo(A, B, i, j, memo):
    if i == len(A) or j == len(B):
        return 0

    elif memo[i][j] != -1:
        return memo[i][j]
    else:
        if A[i] == B[j]:
            memo[i][j] = 1 + lcsMemo(A, B, i + 1, j + 1, memo)
            return memo[i][j]
        else:
            memo[i][j] = max(lcsMemo(A, B, i + 1, j, memo), lcsMemo(A, B, i, j + 1, memo))
            return memo[i][j]


def lcsDP(A, B):
    data = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
    for i in range(len(A)+1):
        for j in range(len(B)+1):
            if i == 0 or j == 0:
                data[i][j] = 0
            elif A[i-1] == B[j-1]:
                data[i][j] = 1 + data[i - 1][j - 1]
            else :
                data[i][j] = max(data[i - 1][j], data[i][j - 1])
    return data
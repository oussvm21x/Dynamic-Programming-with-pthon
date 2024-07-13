from LCS import lcsRecursion , lcsMemo , lcsDP
A = "AGGTAB"
B = "GXTXAYB"

result = lcsRecursion(A, B, 0, 0)
print("- Recursion - Length of LCS is", result)

result = lcsMemo(A, B, 0, 0, [[-1 for _ in range(len(B))] for _ in range(len(A))])
print("- Memoization - Length of LCS is", result)

result = lcsDP(A, B)
print("- Dynamic Programming - Length of LCS is", result[len(A)][len(B)])


# Matrix chaine multiplication problem
def mcmDP(p):
    n = len(p) - 1
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = 0;
    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i+1}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")
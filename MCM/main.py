from mcm import mcmDP , print_optimal_parens
p = [30, 35, 15, 5]
m, s = mcmDP(p)

print("Minimum number of multiplications is:", m[0][len(p) - 2])
print("Optimal parenthesization is:", end=" ")
print_optimal_parens(s, 0, len(p) - 2)

from MinimumPathSum import mps_Reccursion , mps_Memo , mpsDp
grid = [
    [3, 7, 9, 2],
    [2, 5, 1, 3],
    [0, 4, 6, 1],
    [2, 8, 2, 4]
]
memo = [[-1 for _ in range(4)] for _ in range(4)]
print(mps_Reccursion(grid)) # 7
print(mps_Memo(grid , 0 , 0 , memo)) # 7
print(mpsDp(grid))

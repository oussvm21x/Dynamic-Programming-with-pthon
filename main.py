from UniquePaths_II import up_2_Reccursion , up2_Memo , up2_Dp
from UniquePaths import uniquePathsDp
grid = [
    [1]]

print(up_2_Reccursion(grid, 0  ,0 ))
print(up2_Memo(grid, 0  ,0 , [[-1 for i in range(len(grid[0]))] for j in range(len(grid)) ]))
print(up2_Dp(grid))
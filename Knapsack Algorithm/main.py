# Test case 1
import time

from Knapsack import knapsack2Darray , outputSelectedItems , knapsackReccursion , knapsackMemo

n = 4
W = [8, 2, 6, 1]  # Added a dummy zero at the start for correct indexing
V = [50, 150, 210, 30]  # Added a dummy zero at the start for correct indexing
names = ["Laptop", "Headphones", "Notebook", "Phone"]
maxCapacity = 10


# Test case using Reccursion
start_time = time.time()
result = knapsackReccursion(n, W, V, maxCapacity)
end_time = time.time()
runtime_ms = (end_time - start_time) * 1000
print(f"Runtime of the function is {runtime_ms} ms")
print(f"-Reccursion -The optimal value is: {result}")


#Test case using Memoization
start_time = time.time()
result = knapsackMemo(n, W, V, maxCapacity, [[-1] * (maxCapacity + 1) for _ in range(n)], n, maxCapacity)
end_time = time.time()
runtime_ms = (end_time - start_time) * 1000
print(f"Runtime of the function is {runtime_ms} ms")
print(f"-Memoization -The optimal value is: {result}")


#Test case using Dynamic Programming
start_time = time.time()
result = knapsack2Darray(n, W, V, maxCapacity)
end_time = time.time()
runtime_ms = (end_time - start_time) * 1000
print(f"-Dynamic Programming -The optimal value is: {result[n-1][maxCapacity]}")
print(f"Runtime of the function is {runtime_ms} ms")
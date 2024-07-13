# This is the knapsack algorithm using dynamic programming
def knapsack2Darray(n, W, V, maxCapacity):
    data = [[0] * (maxCapacity + 1) for _ in range(n)]
    for item in range(n):
        for capacity in range(maxCapacity + 1):
            if (item == 0 or capacity == 0):
                data[item][capacity] = 0
            elif W[item] <= capacity:
                data[item][capacity] = (
                    max(
                        V[item] + data[item - 1][capacity - W[item]],
                        data[item - 1][capacity]
                    ))
            else:
                data[item][capacity] = data[item - 1][capacity]
    return data


# This is the knapsack algorithm using reccursion
def knapsackReccursion(n, W, V, capacity):
    if (n == 0 or capacity == 0):
        return 0
    if W[n - 1] <= capacity:
        return (
            max(
                V[n - 1] + knapsackReccursion(n - 1, W, V, capacity - W[n - 1]),
                knapsackReccursion(n - 1, W, V, capacity)
            ))
    else:
        return knapsackReccursion(n - 1, W, V, capacity)


# This is the knapsack algorithm using reccursion with memoization
def knapsackMemo(n, W, V, capacity, memo, i, j):
    if n == 0 or capacity == 0:
        return 0
    elif memo[n - 1][capacity - 1] != -1:
        return memo[i][j]
    else:
        if W[n - 1] <= capacity:
            memo[n - 1][capacity - 1] = (
                max(
                    V[n - 1] + knapsackReccursion(n - 1, W, V, capacity - W[n - 1]),
                    knapsackReccursion(n - 1, W, V, capacity)
                ))
            return memo[n - 1][capacity - 1]
        else:
            memo[n - 1][capacity - 1] = knapsackReccursion(n - 1, W, V, capacity)
            return memo[n - 1][capacity - 1]


# This function will output the selected items
def outputSelectedItems(n, W, V, maxCapacity, data, items):
    i = n
    j = maxCapacity
    while (i > 0 and j > 0):
        if (data[i][j] == data[i - 1][j]):
            print(items[i - 1] + " is not included")
        else:
            print(items[i - 1] + " is included")
            j = j - W[i];
        i = i - 1;

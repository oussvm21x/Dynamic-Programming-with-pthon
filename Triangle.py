def minPath(triangle) :
    data = [[0 for i in range(len(triangle))] for j in range(len(triangle))]
    for i in range(len(triangle)):
        data[0][i] = triangle[len(triangle)-1][i]
    for i in range(1,len(triangle)):
        for j in range(len(triangle[len(triangle)-i-1]))  :
            data[i][j] = triangle[len(triangle)-i-1][j] + min(data[i-1][j],data[i-1][j+1])
    return data[len(triangle)-1][0]
def matrixElementsSum(matrix):
    c=0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if(matrix[i][j]==0 and i + 1 < len(matrix)):
                matrix[i+1][j]=0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            c+= matrix[i][j]
    return c
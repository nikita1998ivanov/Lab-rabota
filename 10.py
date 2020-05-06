def func_1(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] ** 2


def func_2(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] % 2 == 0):
                matrix[i][j] = matrix[i][j] ** 2


def func_3(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] < 5):
                matrix[i][j] = matrix[i][j] ** 2


def func_4(matrix):
    for i in range(4):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] ** 2


matrix = [[1,2,3,4,5,6,7,8],
          [8,7,6,5,4,3,2,1],
          [2,3,4,5,6,7,8,9],
          [9,8,7,6,5,4,3,2],
          [1,3,5,7,9,7,5,3],
          [3,1,5,3,2,6,5,7],
          [1,7,5,9,7,3,1,5],
          [2,6,3,5,1,7,3,2]]
print(matrix)
func_1(matrix)
print(matrix)
func_2(matrix)
print(matrix)
func_3(matrix)
print(matrix)
func_4(matrix)
print(matrix)

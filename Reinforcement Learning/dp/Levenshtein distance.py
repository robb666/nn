import numpy as np


def L_matrix(str1, str2):
    matrix = [[0 for _ in range(len(str1) + 2)] for _ in range(len(str2) + 2)]
    for row in range(len(str1)):
        for column in range(len(str2)):
            matrix[0][2 + row] = str1[row]
            matrix[1][2 + row] = row + 1
            matrix[2 + column][0] = str2[column]
            matrix[2 + column][1] = column + 1

    return np.array(matrix)


def L_dist(str1, str2):
    matrix = L_matrix(str1, str2)
    for row in range(2, len(str2)+2):
        for column in range(2, len(str2)+2):
            print(matrix)
            print(row, column)
            if str1[row - 2] == str2[column - 2]:
                matrix[row][column] = matrix[row - 1][column - 1]
                print()
            elif str1[row - 2] != str2[column - 2]:
                matrix[row][column] = min(int(matrix[row][column - 1]),
                                          int(matrix[row - 1][column - 1]),
                                          int(matrix[row - 1][column])) + 1

    return matrix



str1 = 'abcdef'
str2 = 'azced'

print(L_dist(str1, str2))
# print(~1)
# print(min(1, 0, 3, 5))


















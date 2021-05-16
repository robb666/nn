import numpy as np


def L_matrix(str1, str2):
    matrix = [[0 for _ in range(len(str1) + 2)] for _ in range(len(str2) + 2)]
    for row in range(len(str1)):
        matrix[0][row + 2] = str1[row]
        matrix[1][row + 1] = row

    for column in range(len(str2)):
        matrix[column + 2][0] = str2[column]
        matrix[column + 1][1] = column

    return np.array(matrix)




def L_dist(str1, str2):
    matrix = L_matrix(str1, str2)
    for row in range(2, len(str1) + 2):
        for column in range(2, len(str2) + 2):
            pass
            # matrix[row - 1][1] = row
            # matrix[1][column] = row


            # print(str1[column-2], str2[column-2])
            # if str1[column - 2] == str2[column - 2]:
            #     matrix[row-1][column] = matrix[row-1][column-1]
            # else:
            #     pass

    return matrix













str1 = 'abcdef'
str2 = 'azced'

print(L_dist(str1, str2))
# print(~1)
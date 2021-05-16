import numpy as np


def L_matrix(str1, str2):
    matrix = [[0 for _ in range(len(str1) + 2)] for _ in range(len(str2) + 2)]
    for i in range(len(str1)):
        matrix[0][i + 2] = str1[i]

    for j in range(len(str2)):
        matrix[j + 2][0] = str2[j]

    return np.array(matrix)




def L_dist(str1, str2):
    matrix = L_matrix(str1, str2)
    for i in range(2, len(str2) + 2):
        for j in range(2, len(str1) + 2):
            matrix[1][i] = i - 1
            matrix[j][1] = j - 1


            print(str1[j-2], str2[i-2])
            if str1[i - 2] == str2[j - 2]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                pass

    return matrix













str1 = 'abcdef'
str2 = 'azced'

print(L_dist(str1, str2))
# print(~1)
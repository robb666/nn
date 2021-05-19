import numpy as np


def L_distance(X, Y):
    (m, n) = (len(X), len(Y))
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]

    for i in range(1, m + 1):
        T[i][0] = i

    for j in range(1, n + 1):
        T[0][j] = j

    for row in range(1, m + 1):
        for column in range(1, n + 1):

            if X[row - 1] == Y[column - 1]:
                cost = 0
            else:
                cost = 1
            T[row][column] = min(int(T[row - 1][column] + 1),
                                 int(T[row][column - 1] + 1),
                                 int(T[row - 1][column - 1]) + cost)
    return np.array(T)


X = 'Robert'
Y = 'Rafał'

print(L_distance(X, Y))


# Minimum Edit Distance
#####################################################
def minimum_edit_matrix(str1, str2):
    matrix = [[0 for _ in range(len(str1) + 2)] for _ in range(len(str1) + 2)]
    for row in range(len(str1)):
        for column in range(len(str2)):
            matrix[0][2 + row] = str1[row]
            matrix[1][2 + row] = row + 1
            matrix[2 + column][0] = str2[column]
            matrix[2 + column][1] = column + 1

    return np.array(matrix)


def minimum_edit_dist(str1, str2):
    matrix = minimum_edit_matrix(str1, str2)
    for row in range(2, len(str1)+2):
        for column in range(2, len(str1)+2):

            if str1[row - 2] == str2[column - 2]:
                matrix[row][column] = matrix[row - 1][column - 1]
                print()
            elif str1[row - 2] != str2[column - 2]:
                matrix[row][column] = min(int(matrix[row][column - 1]),
                                          int(matrix[row - 1][column - 1]),
                                          int(matrix[row - 1][column])) + 1

    for i in matrix:
        if i[0] == ' ':
            matrix = matrix[:np.where(matrix == ' ')[0][0]]

    return matrix


str1 = 'Robert'
str2 = 'Rafał '

print(minimum_edit_dist(str1, str2))
# print(~1)



















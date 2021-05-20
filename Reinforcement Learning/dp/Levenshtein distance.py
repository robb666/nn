import numpy as np


def L_distance(X, Y):
    X, Y = Y, X
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


X = 'kitten'
Y = 'sitting'

print(L_distance(X, Y))


#########################
# Minimum Edit Distance #
#########################
def minimum_edit_matrix(str1, str2):
    matrix = [[0 for _ in range(len(str1) + 2)] for _ in range(len(str2) + 2)]

    for row in range(len(str1)):
        matrix[0][row + 2] = str1[row]
        matrix[1][row + 2] = row + 1

    for column in range(len(str2)):
        matrix[column + 2][0] = str2[column]
        matrix[column + 2][1] = column + 1

    return matrix


def minimum_edit_dist(str1, str2):
    matrix = minimum_edit_matrix(str1, str2)
    for row in range(2, len(str2) + 2):
        for column in range(2, len(str1) + 2):

            if str1[column - 2] == str2[row - 2]:
                matrix[row][column] = matrix[row - 1][column - 1]
                print()
            else:
                matrix[row][column] = min(int(matrix[row][column - 1]),
                                          int(matrix[row - 1][column - 1]),
                                          int(matrix[row - 1][column])) + 1
    return np.array(matrix)


str1 = 'kitten'
str2 = 'sitting'

print(minimum_edit_dist(str1, str2))
# print(~1)



















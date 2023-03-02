"""0/1 Knapstack"""


def Knapsack(k, arr):
    matrix = [[0 for _ in range(k + 1)] for _ in range(len(arr) + 2)]
    # print(matrix)
    for i in range(k + 1):
        matrix[0][i] = i

    for row in range(2, len(arr) + 2):
        for column in range(1, k + 1):

            # if row == 1 or column == 0:
            #     matrix[row][column] = 0

            if arr[row - 2][0] > column:
                matrix[row][column] = matrix[row - 1][column]

            else:
                matrix[row][column] = max(arr[row - 2][1] + matrix[row - 1][column - arr[row - 2][0]],
                                              matrix[row - 1][column])
    print(matrix)
    return matrix[-1][-1]



# t = [3, 12] ???

# arr = [1, 6, 9]
# arr = [3, 4, 4, 4, 8]
# arr = [(1, 1), (3, 4), (4, 5), (5, 7)]
arr = [(5, 60), (3, 50), (4, 70), (2, 30)]  # Weight and value pairs
# k = 12
# k = 8
k = 5

print(Knapsack(k, arr))






"""???"""
def unboundedKnapsack(k, arr):
    l = []
    arr = list(reversed(arr))
    for i in range(len(arr)):

        if k % arr[i] == 0:
            while 0 < arr[i] <= k:
                k = k - arr[i]
                l.append(arr[i])
    return sum(l)











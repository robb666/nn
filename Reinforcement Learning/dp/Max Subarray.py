



def maxContSubarr(arr):

    print(arr)
    print(max(arr))
    arr2 = []
    # max_subsequence = 0
    for i in arr:
        if i > 0:
            arr2.append(i)

    if sum(arr2) > 0:
        max_subsequence = sum(arr2)
    else:

        max_subsequence = max(arr)


    s = 0
    dp_arr = []
    start = 0
    stop = 0
    for i in arr[:]:
        s += i
        mx = max(i, s)
        dp_arr.append(mx)
        stop = dp_arr.index(max(dp_arr)) + 1

    dp_arr1 = []
    s1 = 0
    for j in list(reversed(arr[start:stop])):
        s1 += j
        mx1 = max(j, s1)
        dp_arr1.append(mx1)

    start = len(arr[start:stop]) - dp_arr1.index(max(dp_arr1)) - 1
    print(arr[start:stop])
    return sum(arr[start:stop]), max_subsequence


arr = [-1, 2, 3, -4, 5, 10]
# arr = [1, 2, 3, 4]
# arr = [-2, -3, -1, -4, -6]
print(maxContSubarr(arr))







def maxSubarray(arr):
    matrix = [[0 for _ in range(len(arr))] for _ in range(len(arr) + 1)]
    for i, j in enumerate(arr):
        matrix[0][i] = j

    ref = sum(arr)
    max_arr = []
    # print(arr)
    for row in range(1, len(arr) + 1):
        for column in range(len(arr)):
            matrix[row][column] += matrix[row][column - 1] + arr[column]
            matrix[row][column - 1] = 0
            # matrix[row].insert(0, 0)
            # max_arr.append(i)

    print(matrix, '\n')
    # return max_arr





# print(maxSubarray(arr))























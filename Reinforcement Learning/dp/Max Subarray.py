



def maxContSubarr(arr):

    print(arr)

    s = 0
    dp_arr = []
    for i in arr[:]:
        s += i
        print(i, s)
        mx = max(i, s)
        print(mx)
        dp_arr.append(mx)
        # if mx == s:
        #     arr.remove(i)
        start = 0
        stop = dp_arr.index(max(dp_arr))
    print('max subarr: ', arr[start:stop + 1])

    return dp_arr  #, dp_arr[- 1]



arr = [-1, 2, 3, -4, 5, -2]
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






















# arr2 = []
# for i in arr:
#     if i > 0:
#         arr2.append(i)
# return sum(arr2)
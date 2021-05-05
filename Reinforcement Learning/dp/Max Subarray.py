

def maxContSubarr(arr):

    for _ in range(len(arr)):
        _, arr = arr, [int(n) for n in arr.split()]
        h = m = t = arr[0]
        for ind, n in enumerate(arr):
            if ind == 0: continue
            t = max(t, n, t + n)
            h = max(n, h + n)
            m = max(m, h)
        print(m, t)




with open('test_maxsubarr.txt') as arr:
    arr = arr.read()[9:]
    ma
    # for i in arr:
    print(maxContSubarr(arr))












def maxContSubarr(arr):

    arr2 = []
    for i in arr:
        if i > 0:
            arr2.append(i)
    if sum(arr2) > 0:
        max_subsequence = sum(arr2)
    else:
        max_subsequence = max(arr)

    dp_start = []
    s1 = 0
    for i in list(reversed(arr)):
        s1 += i
        mx1 = max(i, s1)
        dp_start.append(mx1)

    dp_stop = []
    s2 = 0
    for j in arr:
        s2 += j
        mx2 = max(j, s2)
        dp_stop.append(mx2)

    start = (len(arr) - 1) - dp_start.index(max(dp_start))
    stop = dp_stop.index(max(dp_stop)) + 1
    max_subarray = sum(arr[start:stop])

    return max_subarray, max_subsequence


# arr = [-1, 2, 3, -4, 5, 10]
# arr = [1, 2, 3, 4]
# arr = [-2, -3, -1, -4, -6]

# print(len(arr), arr.index(max(arr)), arr[len(arr) - arr.index(max(arr)):-1])

# with open('test_maxsubarr.txt') as arr:
#     arr = list(map(int, arr.read()[9:].split()))
#     # for i in arr:
#     print(maxContSubarr(arr))







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























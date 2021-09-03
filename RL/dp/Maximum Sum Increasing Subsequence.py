
import sys


def MaximumSumIncreasingSubsequence(arr):
    max_sub = arr.copy()
    ind_arr = [0 for _ in range(len(arr))]
    partial_values = []

    for i in range(1, len(arr)):
        for j in range(len(arr)):
            if arr[j] < arr[i] and max_sub[j] + arr[i] > max_sub[i] and j < i:
                max_sub[i] = max_sub[j] + arr[i]
                ind_arr[i] = j

    max_sum = max(max_sub)
    while max_sum > 0:
        m = max_sub.index(max_sum)
        max_sum = max_sum - arr[m]
        partial_values.append(arr[m])

    return max(max_sub), list(reversed(partial_values))


# arr = [4, 6, 1, 3, 8, 4, 6]
arr = [1, 101, 2, 3, 100, 4, 5]
# arr = [3, 2, 6, 4, 5, 1]
# arr = [10, 5, 4, 3]
# arr = [3, 4, 5, 10]
# arr = [3, 2, 6, 4, 5, 1]

print(MaximumSumIncreasingSubsequence(arr))
print()

###################################################
def constructMaxSumIS(arr, n):
    L = []
    index = 0
    for i in arr:
        L.append([i, index])
        index += 1

    L[0][1] = -1

    for i in range(1, n):  # można bez 1
        for j in range(i):
            if arr[i] > arr[j] and L[i][0] < arr[i] + L[j][0]:
                L[i][0] = arr[i] + L[j][0]
                L[i][1] = j
    print(L)
    maxi, currIndex, track = -sys.maxsize, 0, 0

    for p in L:
        if p[0] > maxi:
            maxi = p[0]
            currIndex = track

        track += 1

    result = []

    while currIndex >= 0:
        result.append(arr[currIndex])
        previousIndex = L[currIndex][1]

        if currIndex == previousIndex:
            break

        currIndex = previousIndex

    for i in range(len(result) -1, -1, -1):
        print(result[i], end=' ')


array = [1, 101, 2, 3, 100, 4, 5 ]
# array = [3, 2, 6, 4, 5, 1]
n = len(array)


constructMaxSumIS(array, len(array))
print()
print()


############################################
def findSum(arr):

    summ = 0
    for _ in arr:
        summ += 1
    return summ


def printMaxSumIS(arr, n):
    L = [[] for _ in range(n)]
    L[0].append(arr[0])

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and findSum(L[i]) < findSum(L[j]):
                for e in L[j]:
                    if e not in L[i]:
                        L[i].append(e)
        L[i].append(arr[i])

    res = L[0]
    for x in L:
        if findSum(x) > findSum(res):
            res = x

    for i in res:
        print(i, end=' ')

    return L


arr = [3, 2, 6, 4, 5, 1]

n = findSum(arr)
print(printMaxSumIS(arr, n))

import numpy as np


def MaximumSumIncreasingSubsequence(arr):
    max_sub = arr.copy()
    ind_arr = [0 for _ in range(len(arr))]

    for i in range(1, len(arr)):
        for j in range(len(arr)):
            if arr[j] < arr[i] and max_sub[j] + arr[i] > max_sub[i]:
                max_sub[i] = max_sub[j] + arr[i]
                ind_arr[i] = j



    return arr, max_sub, ind_arr

    # return arr, max_sub, ind_arr


arr = [4, 6, 1, 3, 8, 4, 6]
# print(MaximumSumIncreasingSubsequence(arr))
arr2 = []
print(MaximumSumIncreasingSubsequence(arr))







# ind_arr = []
# arr = [4, 6, 1, 3, 8, 4, 6]
# max_sub = [4, 10, 1, 4, 18, 8, 14]
# for i in range(1, len(max_sub)):
#     # for j in range(len(max_sub)):
#         if max_sub[i-1] < max_sub[i]:
#
#             ind_arr.append(max_sub.index(max_sub[i-1]))
#
#
# print(ind_arr)




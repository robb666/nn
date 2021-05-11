

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



arr = [4, 6, 1, 3, 8, 4, 6]
# arr = [1, 101, 2, 3, 100, 4, 5]

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




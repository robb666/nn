

def MaximumSumIncreasingSubsequence(arr):
    max_sub = arr.copy()
    ind_arr = [0, 1, 2, 3, 4, 5, 6]

    for i in range(1, len(arr)):
        for j in range(len(arr)):
            if arr[j] < arr[i] and j < i:
                max_sub[i] = max(max_sub[j] + arr[i], max_sub[i])
                ind_arr[i] = max_sub.index(max_sub[j])

    return arr, max_sub, ind_arr


arr = [4, 6, 1, 3, 8, 4, 6]
print(MaximumSumIncreasingSubsequence(arr))

































def MaximumSumIncreasingSubsequence(arr):
    max_sub = arr
    ind_arr = []
    # j = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == 0:
                continue
            if arr[j] < arr[i]:
                max_sub[i] = max(max_sub[i], max_sub[j] + arr[i])

    return max_sub


arr = [4, 6, 1, 3, 8, 4, 6]
print(MaximumSumIncreasingSubsequence(arr))






















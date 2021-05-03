


def maxSubarray(arr):
    arr_len = [0 for _ in range(len(arr))]

    ref = sum(arr)
    max_arr = []
    print(arr)
    for i in arr:
        # arr.pop(0)
        # arr.insert(0, 0)
        max_arr.append(i)
        print(arr, max_arr)

    # return max_arr










arr = [-1, 2, 3, -4, 5, 10]


print(maxSubarray(arr))






















# arr2 = []
# for i in arr:
#     if i > 0:
#         arr2.append(i)
# return sum(arr2)
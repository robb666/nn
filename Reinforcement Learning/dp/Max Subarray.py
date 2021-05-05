# importing the required module
import timeit





setup = '''
def maxContSubarr(arr):

    for _ in range(len(arr)):
        _, arr = arr, [int(n) for n in arr.split()]
        h = m = t = arr[0]
        for ind, n in enumerate(arr):
            if ind == 0: continue
            t = max(t, n, t + n)
            h = max(n, h + n)
            m = max(m, h)
        return m, t


with open('test_maxsubarr.txt') as arr:
    arr = arr.read()[9:]
    maxContSubarr(arr)
'''

times = timeit.repeat(setup = setup,
                          repeat = 100,
                          number = 10000)
print(sum(times))



setup2 = '''
def maxSubarr(arr):

    arr2 = []
    for _ in range(len(arr)):
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


with open('test_maxsubarr.txt') as arr:
    arr = list(map(int, arr.read()[9:].split()))

    maxSubarr(arr)
'''




times = timeit.repeat(setup = setup2,
                          repeat = 100,
                          number = 10000)
print(sum(times))



















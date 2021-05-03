import sys

sys.setrecursionlimit(100000000)

memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        f = fib_memo(n - 1) + fib_memo(n - 2)
        memo[n] = f
        return f


# print(fib_memo(1000))


def fibonacciModified(t1, t2, n):
    arr = [t1, t2]
    for _ in range(2, n):
        tn = arr[- 2] + arr[- 1] ** 2
        arr.append(arr[- 1])
        arr.append(tn)
        arr.pop(0)
        arr.pop(0)

    return arr[- 1]


t1 = 0
t2 = 1
n = 25

# print(fibonacciModified(t1, t2, n))


def f_bottom_up(n):
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[- 1] + arr[- 2])
        arr.pop(0)

    return arr[- 1]


# print(f_bottom_up(1000))


def f_rec(n):
    if n == 1 or n == 2:
        return 1
    return f_rec(n - 1) + f_rec(n - 2)


# print(f_rec(35))

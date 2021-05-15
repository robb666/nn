from operator import xor


def xorAndSum(a, b):
    # Write your code here

    sum_modulo = 10 ** 9 + 7

    x = int(str(a), 2)
    y = int(str(b), 2)
    p = 0
    for i in range(0, 314160):
        # p += x ^ (y << i)
        p += xor(x, y << i)
    return p % ((10 ** 9) + 7)





a = 10
b = 1010

print(xorAndSum(a, b))



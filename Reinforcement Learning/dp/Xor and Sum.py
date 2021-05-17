from operator import xor


def xorAndSum(a, b):

    sum_modulo = 10 ** 9 + 7

    a = int(str(a), 2)
    b = int(str(b), 2)

    sum_ab = 0
    for i in range(314160):
        sum_ab += xor(a, b << i)
        # sum_ab += a ^ (b << i)
    return sum_ab % sum_modulo



a = 10
b = 1010

print(xorAndSum(a, b))



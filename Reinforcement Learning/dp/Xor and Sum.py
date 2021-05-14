from operator import xor


def xorAndSum(a, b):
    # Write your code here

    sum_modulo = 10 ** 9 + 7


    sum_ab = 0
    for i in range(314159):
        sum_ab = xor(a, b << i)
        if sum_ab == sum_modulo:
            return sum_modulo, sum_ab


a = 10
b = 1010

print(xorAndSum(a, b))







def xorAndSum(a, b):
    # Write your code here

    sum_modulo = 10 ** 9 + 7
    # to_bin = format(a, 'b')
    bina = int(str(a), 2)
    binb = int(str(b), 2)

    # sum_ab = 0
    # for i in range(10):
    sum_ab = 5 % 5

    return sum_modulo, bina, binb, sum_ab


a = 10
b = 1010

print(xorAndSum(a, b))




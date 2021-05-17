from operator import xor


def xorAndSum(a, b):
    # Write your code here

    sum_modulo = 10 ** 9 + 7
<<<<<<< Updated upstream

    x = int(str(a), 2)
    y = int(str(b), 2)
    p = 0
    for i in range(0, 314160):
        # p += x ^ (y << i)
        p += xor(x, y << i)
    return p % ((10 ** 9) + 7)



=======
    a = int(str(a), 2)
    b = int(str(b), 2)

    sum_ab = 0
    for i in range(314160):
        sum_ab += xor(a, b << i)
        # sum_ab += a ^ (b << i)
    return sum_ab % sum_modulo
>>>>>>> Stashed changes


a = 10
b = 1010

print(xorAndSum(a, b))



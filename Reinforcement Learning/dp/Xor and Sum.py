
def xorAndSum(a, b):
    # Write your code here

    sum_modulo = 10 ** 9 + 7
    # to_bin = format(a, 'b')
    from_bina = int(str(a), 2)
    from_binb = int(str(b), 2)

    return sum_modulo, from_bina, from_binb


a = 10
b = 1010

print(xorAndSum(a, b))

import numpy as np
from fractions import Fraction

print()
print('5.11')
suma = - 2 - Fraction(3, 4) + - 3 - Fraction(1, 4)
różnica = 2 + Fraction(' 3/4 ') + - 3 - Fraction('1/4')

print(float(suma + różnica))


print()
print('5.12')
różnica = - (5 + Fraction(3, 5) - 2.5)
suma = - 5 - Fraction(3, 5) + (- 2.5)

print(różnica + suma)


print()
print('5.14')
suma = np.sum([6, -3.25, -1.5])
różnica = np.subtract([1], [Fraction(1, 4)])

print(suma - różnica)


print()
print('5.15')
oblicz = np.multiply([np.sum([- (-10 + (-18)) - (- (-2) - (-16)) + 10])], 0.2)

print(oblicz)


print()
print('6')
oblicz = np.prod([1, -1, 2, -2, 3, -3, 4, -4])

print(oblicz)



print()
print('6.2')
b3 = float(np.multiply([-1 - Fraction(1, 3)], [- Fraction(3, 8)]))
b4 = float(np.multiply([-5 - Fraction(5, 6)], [-2 - Fraction(4, 7)]))

print(b3)
print(b4)


print()
print('6.4')
g1 = np.prod([-4, -5])
g2 = np.prod([-2, -9])
g3 = np.prod([3, 5])
g = np.sum([g1, g2, g3])

print(g)

g = np.sum([-4 * -5] + [-2 * -9] + [3 * 5])
print(g)

g = np.sum([np.prod([-4, -5]), np.prod([-2, -9]), np.prod([3, 5])])
print(g)

print()
h = np.sum([-2, np.prod([3, 3]), np.prod([12, -5]), np.prod([-1, -20])])
print(h)


print()
print('6.5')
a = np.prod([-15, -8, -3, -5])
print(a)

print()
g = np.prod([5, -9, --4, -10, --2, 3])
print(g)

print()
h = np.sum([np.prod([-16, -4]), - np.prod([8, -7]), - np.prod([-6, 11])])
print(h)


print()
print('Zadanie 6.8')
a = np.sum([np.prod([-5, -7]), np.prod([-6, 9]), - np.prod([-5, -6])])
print(a)

print()
b = np.sum([np.prod([9, 8]), np.prod([-4, -7]), - np.prod([-10, -3])])
print(b)

print()
c = np.sum([np.prod([-5, -4]), -np.prod([-3, 8]), np.prod([-6, 7])])
print(c)

print()
d = np.sum([np.prod([-1, -2, -2]), np.prod([-4, 7, -3])])
print(d)

print()
e = np.sum([np.prod([-5, 5, -2]), -np.prod([-4, -2, -3])])
print(e)

print()
f = np.sum([np.prod([-2, 6, -1]), np.prod([-3, -5, -8, -4])])
print(f)

print()
g = np.sum([np.prod([-3, -4]), np.prod([-1, -5, -2]), - np.prod([9, -3])])
print(g)

print()
h = np.sum([np.prod([7, 6, -2]), -np.prod([-3, -1, -6]), np.prod([8, -10]), -np.prod([20, -7])])
print(h)




print()
print('Zad. 6.10')
sumka = float(Fraction(np.multiply(np.sum([-18, 28.4]), -4)).limit_denominator())
print(sumka)




print()
print('Zad. 6.11')
sumka = np.sum([np.prod([-1, 6]), np.prod([2, -4])])
print(sumka)



print()
print('Zad. 3')
dzielenie = np.divide([-18, 21], [6, -3])
print(dzielenie)



print()
print('Zad. 4')
dzielenie = np.divide([12, -1 - Fraction(3, 5), 15, -5], [float(Fraction(1, 3)), -.4, -3, float(Fraction(2, 3))])
print(dzielenie)



print()
print('Zad. 5')
dzielenie = np.divide([Fraction(-16, 1), -Fraction(12, 1), Fraction(3 - 7, 1)], [Fraction(-24, 1), 5, -5 + 8])
print(dzielenie)

"""cd jupyter"""















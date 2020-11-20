import numpy as np
import math


# Euler Expotentiation and Normalization in raw p
li = [[1, 2, 3]]
inputs = np.array([[4.8, 1.21, 2.385],
                   [8.9, -1.81, 0.2],
                   [1.41, 1.051, 0.026]])

ex = np.exp(li - np.max(li, axis=1, keepdims=True))
pro = ex / np.sum(ex, axis=1, keepdims=True)
print(pro)


li1 = [1, 2, 3]
l = []
l1 = []
for i in li1:
    exp1 = math.e ** (i - max(li1))
    l.append(exp1)

for j in l:
    l1.append(j / sum(l))
print(l1)








# """
# You have a million grams of a radioactive element with a half-life of one minute. This means that, every minute,
# the mass of the element halves. Of the following options,
# which is the shortest time after which you have less than a gram?
# """
#
#
# i = 1_000_000
# l = []
# while (n := i * 0.5) > 1:
#     i = n
#     l.append(i)
#
# for i, v in enumerate(l, start=1):
#     print(i, v)
#
#
#
#
# """
# Someone gives the choice between giving you one dollar today, two tomorrow, four the next day, and so forth,
# with the amount doubling each day for a month (31 days), or giving you a million dollars today.
# Which one will net you the most money?
# """
#
# i = 1
# l = []
# while (n := i*2) < 2_000_000_000:
#     i = n
#     l.append(i)
#
# for i, v in enumerate(l, start=2):
#     print(i, v)








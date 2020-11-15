"""
You have a million grams of a radioactive element with a half-life of one minute. This means that, every minute,
the mass of the element halves. Of the following options,
which is the shortest time after which you have less than a gram?
"""


i = 1_000_000
l = []
while (n := i * 0.5) > 1:
    i = n
    l.append(i)

for i, v in enumerate(l, start=1):
    print(i, v)




"""
Someone gives the choice between giving you one dollar today, two tomorrow, four the next day, and so forth,
with the amount doubling each day for a month (31 days), or giving you a million dollars today.
Which one will net you the most money?
"""

i = 1
l = []
while (n := i*2) < 2_000_000_000:
    i = n
    l.append(i)

for i, v in enumerate(l, start=2):
    print(i, v)































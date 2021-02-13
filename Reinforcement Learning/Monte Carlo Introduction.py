import random

def rollCoin():
    roll = random.randint(1, 2)
    return roll



def inform_winner():
    reszka = 0
    orzeł = 0

    # reszka_won = []
    # orzeł_won = []

    while orzeł < 1000 or reszka < 1000:
        roll = rollCoin()
        if roll == 1:
            reszka += 1
            # reszka_won.append(reszka)
        else:
            orzeł += 1
            # orzeł_won.append(orzeł)

    if reszka > orzeł:
        return 'R', reszka
    else:
        return 'O', orzeł


r, o = 1, 1
for f in range(1, 4001):

    if inform_winner()[0] == 'R':
        r += inform_winner()[1]
    else:
        o += inform_winner()[1]


    print(f'Reszka wygrała {r/o}x, orzel wygrał {o/r}x')
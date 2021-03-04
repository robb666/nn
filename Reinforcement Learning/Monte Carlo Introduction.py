import random

def rollCoin():
    roll = random.randint(1, 2)
    return roll



def inform_winner():
    """Parzysty zazwyczaj wygrywa..???"""
    reszka = 0
    orzeł = 0

    # reszka_won = []
    # orzeł_won = []

    while orzeł < 1000 or reszka < 1000:
        roll = rollCoin()
        if roll == 1:
            orzeł += 1
            # reszka_won.append(reszka)
        if roll == 2:
            reszka += 1
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

<<<<<<< HEAD
    print(f'Reszka wygrała {r/o}x, orzel wygrał {o/r}x')
=======

    print(f' orzel wygrała {r}x, Reszka wygrał {o}x')
>>>>>>> e76a26b4dec2efe74bb865a616e3ae1944f9c002

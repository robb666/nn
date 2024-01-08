import numpy as np


"""Get minimum coins + coins value"""


def np_get_min_coins(amount, coins):
    matrix = np.zeros((len(coins) + 1, amount + 1), dtype=int)
    matrix[0] = range(amount + 1)
    coin_idx = 1
    for coin in coins:
        for total in range(amount + 1):
            matrix[coin_idx][total] = matrix[coin_idx - 1][total]
            if total >= coin:
                matrix[coin_idx][total] = np.min((matrix[coin_idx - 1][total],
                                                  matrix[coin_idx][total - coin] + 1), axis=0)
        coin_idx += 1
    return matrix


def np_get_coins_value(amount, coins, matrix):
    coin_idx = len(coins)
    coins_value = []
    for coin in reversed(coins):
        for col in range(amount, -1, -1):
            if sum(coins_value) == amount:
                return f'\nYou need minimum {matrix[-1][-1]} coins of {coins_value} to get {amount}'
            if matrix[coin_idx][col - coin] + 1 > matrix[coin_idx][col] == matrix[coin_idx - 1][col]:
                if matrix[coin_idx - 1][col - coins[coins.index(coin) - 1]] == 1:
                    coins_value.append(coins[coins.index(coin) - 1])
                    coin_idx -= 1
                    break
            else:
                coins_value.append(coins[coins.index(coin) - 1])
            coin_idx -= 1


# amount = 4
# coins = [1, 2, 3]

amount = 11
coins = [1, 5, 6, 8]

matrix = np_get_min_coins(amount, coins)
print(matrix)
print(np_get_coins_value(amount, coins, matrix))

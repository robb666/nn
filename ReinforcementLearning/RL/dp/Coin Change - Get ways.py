import numpy as np

"""Get ways"""


def getWays(amount, coins):
    sorted_coins = sorted(coins)
    matrix = [[0 for _ in range(amount + 1)] for _ in range(len(sorted_coins) + 2)]
    for row in range(len(sorted_coins) + 2):
        for column in range(amount + 1):
            matrix[row][0] = 1
            matrix[0][column] = column

    for row in range(2, len(sorted_coins) + 2):
        for column in range(1, amount + 1):

            if sorted_coins[row - 2] > column:
                matrix[row][column] = matrix[row - 1][column]

            elif sorted_coins[row - 2] <= column:
                matrix[row][column] = matrix[row - 1][column] + matrix[row][column - sorted_coins[row-2]]

    return matrix[- 1][- 1]


"""Get minimum coins"""


def np_get_min_coins(amount, coins):
    matrix = np.zeros((len(coins) + 1, amount + 1), dtype=int)
    matrix[0] = range(amount + 1)
    coin_idx = 1
    coins_value = []
    for coin in coins:
        for total in range(amount + 1):
            matrix[coin_idx][total] = matrix[coin_idx - 1][total]
            if total >= coin:
                matrix[coin_idx][total] = np.min((matrix[coin_idx - 1][total],
                                                 matrix[coin_idx][total - coin] + 1), axis=0)
                # if coin == matrix[coin_idx - 1][total]:
                #     coins_value.append(coin)
        coin_idx += 1

    minimum_coins = matrix[-1][-1]

    # return f'You need minimum of {minimum_coins} coins of {coins_value}'
    return matrix


amount = 11
coins = [1, 5, 6, 8]

# amount = 4
# coins = [1, 2, 3]

# print(getWays(amount, coins))

print(np_get_min_coins(amount, coins))
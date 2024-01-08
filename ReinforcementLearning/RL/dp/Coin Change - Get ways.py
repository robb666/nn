

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


# amount = 4
# coins = [1, 2, 3]

amount = 11
coins = [1, 5, 6, 8]

print(getWays(amount, coins))

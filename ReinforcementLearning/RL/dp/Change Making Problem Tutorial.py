"""Change Making Problem Tutorial"""


def _change_matrix(coin_set, change_amount):
    matrix = [[0 for m in range(change_amount + 1)] for m in range(len(coin_set) + 1)]
    for i in range(change_amount + 1):
        matrix[0][i] = i
    return matrix


def change_making(coins, change):
    matrix = _change_matrix(coins, change)
    for r in range(1, len(coins) + 1):
        for c in range(1, change + 1):

            if coins[r - 1] == c:
                matrix[r][c] = 1

            elif coins[r - 1] > c:
                matrix[r][c] = matrix[r - 1][c]

            elif coins[r - 1] < c:
                # print(matrix[r][c - coins[r - 1]])
                matrix[r][c] = min(matrix[r - 1][c], 1 + matrix[r][c - coins[r - 1]])

    print(matrix)
    return matrix[-1][-1]


# x = round((2 % 1.89) * 100)
# print(x)
# print(change_making([1, 2, 5, 10], x))


# coins = [1, 2, 5, 10, 20, 50]
# for c in range(1, len(coins) + 1):
#     print(3 - coins[c - 1])


change = 11
coins = [1, 5, 6, 8]

print(change_making(coins, change))


"""greedy approach"""
def num_coins(cents):
    coins = [25, 10, 5, 1]
    count = 0
    for coin in coins:
        while cents >= coin:
            # print(coin)
            cents = cents - coin
            count = count + 1
    return count


# print(num_coins(125))
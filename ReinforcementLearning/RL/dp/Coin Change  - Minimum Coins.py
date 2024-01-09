import numpy as np


"""Get minimum coins + coins value"""


class MinCoin:
    def __init__(self, amount, coins):
        self.amount = amount
        self.coins = coins
        self.matrix = np.zeros((len(coins) + 1, amount + 1), dtype=int)
        self.matrix[0] = range(amount + 1)
        self.coin_idx = 1
        self.coins_value = []

    def get_min(self):
        for coin in self.coins:
            for total in range(self.amount + 1):
                self.matrix[self.coin_idx][total] = self.matrix[self.coin_idx - 1][total]
                if total >= coin:
                    self.matrix[self.coin_idx][total] = np.min((self.matrix[self.coin_idx - 1][total],
                                                                self.matrix[self.coin_idx][total - coin] + 1),
                                                               axis=0)
            self.coin_idx += 1
        return self.matrix

    def get_val(self):
        max_idx = len(self.coins)
        for coin in reversed(self.coins):
            for col in range(self.amount, -1, -1):
                if sum(self.coins_value) == self.amount:
                    return f'\nYou need minimum {self.matrix[-1][-1]} coin(s) of {self.coins_value} to get {self.amount}'

                if self.matrix[max_idx][col - coin] + 1 > self.matrix[max_idx][col] == self.matrix[max_idx - 1][col]:
                    if self.matrix[max_idx - 1][col - self.coins[self.coins.index(coin) - 1]] == 1:
                        self.coins_value.append(self.coins[self.coins.index(coin) - 1])
                        max_idx -= 1
                        col -= coin
                        break
                else:
                    self.coins_value.append(self.coins[self.coins.index(coin) - 1])

    def get_val_II(self):
        col = self.amount
        for max_idx in range(len(coins), 0, -1):
            coin = self.coins[max_idx - 1]
            while col >= coin and self.matrix[max_idx][col] == self.matrix[max_idx - 1][col - coin] + 1:
                self.coins_value.append(coin)
                col -= coin
        if sum(self.coins_value) == self.amount:
            return f'\nYou need minimum {self.matrix[-1][-1]} coins of {self.coins_value} to get {self.amount}'
        else:
            return 'No solution found with the given coin denominations.'



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


amount = 4 # 3
coins = [1, 2, 3]

# amount = 11
# coins = [1, 5, 6, 8]

change = MinCoin(amount, coins)

print(change.get_min())
print(change.get_val())
# print(change.get_val_II())


# matrix = np_get_min_coins(amount, coins)
# print(matrix)
# print(np_get_coins_value(amount, coins, matrix))

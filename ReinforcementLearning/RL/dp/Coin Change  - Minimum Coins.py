import numpy as np


"""Get Minimum Coins + Coins Value"""


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
        return self.matrix[-1][-1]

    def get_val(self):
        col = self.amount
        for row in range(len(self.coins), 0, -1):
            for coin in reversed(self.coins):
                while self.matrix[row][col] == self.matrix[row][col - coin] + 1:
                    self.coins_value.append(coin)
                    col -= coin
                if col >= coin and self.matrix[row][col] == self.matrix[row - 1][col - coin] + 1:
                    self.coins_value.append(coin)
                    col -= coin
        if sum(self.coins_value) == self.amount:
            return f'\nYou need minimum {self.matrix[-1][-1]} coin(s) of {self.coins_value} to get {self.amount}'
        else:
            return 'No solution found with the given coin denominations.'

    def get_val_II(self):
        col = self.amount
        for max_idx in range(len(coins), 0, -1):
            coin = self.coins[max_idx - 1]
            while self.matrix[max_idx][col] == self.matrix[max_idx][col - coin] + 1:
                self.coins_value.append(coin)
                col -= coin
            if col >= coin and self.matrix[max_idx][col] == self.matrix[max_idx - 1][col - coin] + 1:
                self.coins_value.append(coin)
                col -= coin
        if sum(self.coins_value) == self.amount:
            return f'\nYou need minimum {self.matrix[-1][-1]} coin(s) of {self.coins_value} to get {self.amount}'
        else:
            return 'No solution found with the given coin denominations.'


# amount = 8
# coins = [1, 2, 3]

amount = 11
coins = [1, 5, 6, 8]

change = MinCoin(amount, coins)
change.get_min()

print(change.get_val())
# print(change.get_val_II())

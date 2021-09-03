print()

amount = 4
coins = [1, 2, 3, 4]


# print(coins[-5])

matrix = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 2)]
matrix[2][0] = 1
# matrix[2][1] = 1
matrix[3][4] = 3
matrix[4][0] = 9
matrix[4][1] = 2

# print(matrix)
# #
# for row in range(2, len(coins) + 2):
#     for column in range(1, amount + 1):
#         # print(coins[row - 2])
#         # if coins[row - 2] <= column:
#         print(matrix[row][column - coins[row - 2]])
#         matrix[row][column] = matrix[row][column - coins[row - 2]]
#     print()
# print(matrix)







"""0/1 Kapstack"""


def Knapsack(k, arr):
    matrix = [[0 for _ in range(k + 1)] for _ in range(len(arr) + 2)]
    # print(matrix)
    for i in range(k + 1):
        matrix[0][i] = i

    for row in range(2, len(arr) + 2):
        for column in range(1, k + 1):

            # if row == 1 or column == 0:
            #     matrix[row][column] = 0

            if arr[row - 2][0] > column:
                matrix[row][column] = matrix[row - 1][column]

            else:
                matrix[row][column] = max(arr[row - 2][1] + matrix[row - 1][column - arr[row - 2][0]],
                                              matrix[row - 1][column])
    print(matrix)
    return matrix[-1][-1]



# t = [3, 12] ???

# arr = [1, 6, 9]
# arr = [3, 4, 4, 4, 8]
# arr = [(1, 1), (3, 4), (4, 5), (5, 7)]
arr = [(5, 60), (3, 50), (4, 70), (2, 30)]
# k = 12
# k = 8
k = 5

# print(Knapsack(k, arr))




"""OK?"""
def unboundedKnapsack(k, arr):
    l = []
    arr = list(reversed(arr))
    for i in range(len(arr)):

        if k % arr[i] == 0:
            while 0 < arr[i] <= k:
                k = k - arr[i]
                l.append(arr[i])
    return sum(l)
























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


amount = 4
coins = [1, 2, 3]

# print(getWays(amount, coins))





























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
                print(matrix[r][c - coins[r - 1]])
                matrix[r][c] = min(matrix[r - 1][c], 1 + matrix[r][c - coins[r - 1]])

        print(matrix)
    return matrix[-1][-1]


x = round((2 % 1.89) * 100)
# print(x)
print(change_making([1, 2, 5, 10], x))


# coins = [1, 2, 5, 10, 20, 50]
# for c in range(1, len(coins) + 1):
#     print(3 - coins[c - 1])


"""greedy approach"""
def num_coins(cents):
    coins = [25, 10, 5, 1]
    count = 0
    for coin in coins:
        while cents >= coin:
            print(coin)
            cents = cents - coin
            count = count + 1
    return count


# print(num_coins(125))



























"""Sum combination"""
# def combinationSum(arr):
#     dp = [1, 0, 0, 0, 0]
#     for r in range(0, len(arr) - 1):
#         print(r)
#         for x in arr:
#             print(x)
#             dp[r+x] += dp[r]
#
#     return dp
#
#
#
# arr = [1, 2, 3]
#
# print(combinationSum(arr))






























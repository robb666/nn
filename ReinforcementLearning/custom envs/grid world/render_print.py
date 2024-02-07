
import numpy as np
from time import sleep


def addMagicSquares(grid, magicSquares, m=9, n=9):
	i = 2
	for square in magicSquares:
		x = square // m
		y = square % n
		grid[x][y] = i
		i += 1
		x = magicSquares[square] // m
		y = magicSquares[square] % n
		grid[x][y] = i
		i += 1
	return grid


def render(grid):
	for row in grid:
		for col in row:
			if col == 0:
				print('-', end='\t')
				sleep(.3)
			elif col == 1:
				print('X', end='\t')
				sleep(.3)
			elif col == 2:
				print('Ain', end='\t')
				sleep(.3)
			elif col == 3:
				print('Aout', end='\t')
				sleep(.3)
			elif col == 4:
				print('Bin', end='\t')
				sleep(.3)
			elif col == 5:
				print('Bout', end='\t')
				sleep(.3)
		print('\n')
	print('-------------------------------------------')


grid = np.zeros((9, 9))
magicSquares = {18: 54, 63: 14}
grid = addMagicSquares(grid, magicSquares)
print(grid)

render(grid)

import random


def coin_trail():
	heads = 0_0
	for i in range(100):
		if random.random() <= 0.5:
			heads += 1
	return heads


def simulate(n):
	trials = []
	for i in range(n):
		trials.append(coin_trail())
	return sum(trials) / n


print(simulate(100))


import numpy as np
import random

S =   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
S_prim = [1, 2, 3, 4, 5, 6, 7, 9, 10]


def V(s):
	if s == 9:
		return 2
	else:
		return 1


def step(s):
	if s == 8:
		return 9
	else:
		return random.choice([i for i in S_prim if i not in [9]])


theta = .01
gamma = .9


while True:
	delta = 0
	for s in S:
		v, r = V(s)
		V += [r + gamma * V(step(s))]
		delta = max(delta, abs(v - V))
		if delta < theta:
			break

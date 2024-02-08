import numpy as np

S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def V(s):
	if s == 9:
		return 2, 2
	else:
		return 1, 1


theta = .01
gamma = .9


while True:
	delta = -np.inf
	for s in S:
		v, r = V(s)
		V = V + [r + gamma * V(s_prim)]
		delta = max(delta, abs(v - V))
		if delta < theta:
			break


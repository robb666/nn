import random


class ValueIteration:
	def __init__(self, S, policy, gamma, theta):
		self.S = S
		self.policy = policy
		self.gamma = gamma
		self.theta = theta
		self.value_dict = {s: .0 for s in self.S}
		self.action_def = {'L': -1, 'R': 1}
		self.actions = ['L', 'R']

	def step(self, s, a):
		next_state = (self.S.index(s) + self.action_def[a]) % len(self.S)
		return self.S[next_state]

	def reward(self, s, a, s_prime):
		if s == 8 and a == 'R' and s_prime == 9:
			return 3
		if s == 6 and a == 'L' and s_prime == 5:
			return 2
		else:
			return 1

	def iteration(self):
		# while True:
		delta = 0
		for s in self.S:
			for a in self.actions:
				v = self.value_dict[s]
				# a = self.policy[s]
				s_prime = self.step(s, a)
				r = self.reward(s, a, s_prime)
				self.value_dict[s] = max({s: r + self.gamma * self.value_dict[s_prime] for s in self.S}, key=self.value_dict.get)
				delta = max(delta, abs(v - self.value_dict[s]))
		return self.value_dict
			# if delta < self.theta:
			# 	break


S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
policy = {move: random.choice(['L', 'R']) for move in S}
theta = .01
gamma = .9

value_iteration = ValueIteration(S, policy, gamma, theta)

it = value_iteration.iteration()

print(it)
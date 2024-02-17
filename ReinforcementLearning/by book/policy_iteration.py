import numpy as np
import random
from typing import Dict
from icecream import ic


class PolicyIter:

	def __init__(self, policy, S, S_prime, theta, gamma):
		self.policy = policy
		self.S = S
		self.S_prime = S_prime
		self.theta = theta
		self.gamma = gamma
		self.value_dict: Dict[int, float] = {s: 0.0 for s in S}
		self.action_def = {'L': -1, 'R': 1}
		self.actions = ['L', 'R']

	def reward(self, s, a):
		if s == 8 and a == 'R':
			return 3
		elif s == 6 and a == 'L':
			return 2
		else:
			return 1

	# def action(self, s):
	# 	if random.choice(self.S) not in {2}:
	# 		max_a = max([s for s in S])
	# 		return max(self.action_def[s])
	# 	else:
	# 		return random.choice(self.actions)

	def step(self, s, a):
		next_s_idx = (self.S.index(s) + self.action_def[a]) % len(self.S)
		return self.S[next_s_idx]

		# if s == 8:
		# 	return 9
		# elif s == 6:
		# 	return 5
		# else:
		# 	return random.choice(self.policy[s])

	def policy_evaluation(self):
		# self.value_dict: Dict[int, float] = {s: 0.0 for s in S}
		while True:
			delta = 0
			for s in self.S:
				v = self.value_dict[s]

				a = self.policy[s]
				# a = self.action(s)

				s_prime = self.step(s, a)
				# s_prim = self.step(s)

				self.value_dict[s] = self.reward(s, a) + self.gamma * self.value_dict[s_prime]
				delta = max(delta, abs(v - self.value_dict[s]))
				# print(delta)
			if delta < theta:
				break
		return self.value_dict
		# return self.policy

	def policy_improvement(self):
		for s in S:
			old_action = self.policy[s]
			s_prime = self.step(s, old_action)
			r = self.reward(s, old_action)
			self.policy[s] = max(r + gamma * self.value_dict[s_prime])
			if old_action >= policy[s]:
				return policy
			else:
				self.policy_evaluation()


S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
S_prim = [1, 2, 3, 4, 5, 6, 7, 9, 10]
policy = {move: random.choice(['L', 'R']) for move in S}
# print(policy)

theta = .01
gamma = .9

policy_iter = PolicyIter(policy, S, S_prim, theta, gamma)
value_dict = policy_iter.policy_evaluation()

ic(value_dict)
# print(value_dict)























# Leszek Józwik
# Ja miałem fajną sytuację: Kurator podzielił przedmioty, ja miałem odrabiać lekcje z 3 przedmiotów, żona pozostałe.
# Dzieci miały lepsze wyniki z moich przedmiotów (geografia, historia itd) żona miała gorsze mimo, że jest nauczycielem matematyki,
# biologii. I teraz najlepsze: Sąd stwierdził, że nie dostanę kontaktów w tygodniu, dlatego że ...... ram pam pam .....
# nie odrabiam lekcji z dziećmi w tygodniu. 🤣🤣🤣 Cyrk. Kurtyna


import random
from typing import Dict
from icecream import ic


class PolicyIter:
	def __init__(self, policy, S, theta, gamma):
		self.policy = policy
		self.S = S
		# self.S_prime = S_prime
		self.theta = theta
		self.gamma = gamma
		self.value_dict: Dict[int, float] = {s: 0.0 for s in S}
		# self.value_dict = {s: 0.0 for s in S}
		self.action_def = {'L': -1, 'R': 1}
		self.actions = ['L', 'R']

	def reward(self, s, a, s_prime):
		if s == 8 and a == 'R' and s_prime == 9:
			return 3
		elif s == 6 and a == 'L' and s_prime == 5:
			return 2
		else:
			return random.uniform(0.98, 1.02)

	# def action(self, s):
	# 	if random.choice(self.S) not in {2}:
	# 		max_a = max([s for s in S])
	# 		return max(self.action_def[s])
	# 	else:
	# 		return random.choice(self.actions)

	def step(self, s, a):
		next_s_idx = (self.S.index(s) + self.action_def[a]) % len(self.S)
		return self.S[next_s_idx]

	def policy_evaluation(self):
		while True:
			delta = 0
			for s in self.S:
				v = self.value_dict[s]
				a = self.policy[s]
				s_prime = self.step(s, a)
				self.value_dict[s] = self.reward(s, a, s_prime) + self.gamma * self.value_dict[s_prime]
				delta = max(delta, abs(v - self.value_dict[s]))
			if delta < self.theta:
				break
		return self.value_dict

	def policy_improvement(self):
		for s in self.S:
			action_values = {}
			old_action = self.policy[s]
			for a in self.actions:
				s_prime = self.step(s, a)
				r = self.reward(s, a, s_prime)
				action_value = r + self.gamma * self.value_dict[s_prime]
				action_values[a] = action_value
			self.policy[s] = max(action_values, key=action_values.get)  # policy extraction
			if self.policy[s] != old_action:
				self.policy_evaluation()
				self.policy_improvement()
		return self.policy


S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# S_prim = [1, 2, 3, 4, 5, 6, 7, 9, 10]
policy = {move: random.choice(['L', 'R']) for move in S}

# ic(policy)

theta = .01
gamma = .9

policy_iter = PolicyIter(policy, S, theta, gamma)

value_dict = policy_iter.policy_evaluation()
improved_policy = policy_iter.policy_improvement()

ic(improved_policy, value_dict)
















# Leszek Józwik
# Ja miałem fajną sytuację: Kurator podzielił przedmioty, ja miałem odrabiać lekcje z 3 przedmiotów, żona pozostałe.
# Dzieci miały lepsze wyniki z moich przedmiotów (geografia, historia itd) żona miała gorsze mimo, że jest nauczycielem matematyki,
# biologii. I teraz najlepsze: Sąd stwierdził, że nie dostanę kontaktów w tygodniu, dlatego że ...... ram pam pam .....
# nie odrabiam lekcji z dziećmi w tygodniu. 🤣🤣🤣 Cyrk. Kurtyna

import numpy as np
import icecream as ic


class PolicyIterationNp:
	def __init__(self, policy, S, theta, gamma):
		self.policy = policy
		self.S = S
		self.theta = theta
		self.gamma = gamma
		self.value_dict = {state: .0 for state in S}
		self.action_def = {'L': -1, 'R': 1}
		self.actions = np.array(['L', 'R'])

	def reward(self, s, a, s_prime):
		if s == 8 and a == 'R' and s_prime == 9:
			return 3
		elif s == 6 and a == 'L' and s_prime == 5:
			return 2
		else:
			return 1

	def step(self, s, a):
		new_state = (np.where(self.S == s)[0] + self.action_def[a]) % len(self.S)
		return self.S[new_state][0]

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
			old_action = self.policy[s]
			action_values = {}
			for a in self.actions:
				s_prime = self.step(s, a)
				r = self.reward(s, a, s_prime)
				action = r + self.gamma * self.value_dict[s_prime]
				action_values[a] = action
			self.policy[s] = max(action_values, key=action_values.get)
			if old_action != self.policy[s]:
				self.policy_evaluation()
				self.policy_improvement()
		return self.policy


S = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(S)
policy = {move: 'L' for move in S}

policy_iteration_np = PolicyIterationNp(policy, S, .01, .9)

policy_iteration_np.policy_evaluation()
optimized_policy = policy_iteration_np.policy_improvement()

print(optimized_policy)


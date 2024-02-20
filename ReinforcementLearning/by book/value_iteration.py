

class ValueIteration:
	def __init__(self, S, gamma, theta):
		self.S = S
		self.gamma = gamma
		self.theta = theta
		self.value_dict = {s: .0 for s in self.S}
		self.action_def = {'L': -1, 'R': 1}
		self.actions = ['L', 'R']

	def iteration(self):
		while True:
			delta = 0
			for s in self.S:






















S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
theta = .01
gamma = .9
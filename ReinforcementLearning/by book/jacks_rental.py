import numpy as np
from icecream import ic
import sys
from typing import Dict
from time import sleep
import random


np.set_printoptions(linewidth=200)


# 6marca
class RentalBusiness:
	def __init__(self, S, policy, theta=.1, gamma=.9, cars_num_1=10, cars_num_2=10):
		self.S = S
		self.policy = policy
		# ic(self.policy)
		self.THETA = theta
		self.GAMMA = gamma
		self.day = 1
		self.location1 = cars_num_1
		self.location2 = cars_num_2
		self.value_dict: Dict[int, float] = {s + row: 0. for s in range(1, 21) for row in range(381)}
		# ic(self.value_dict)
		# self.moved = 0
		self.amount = 0
		self.available: int = 0
		# self.actions_def = {'1': self.move_cars_1, '2': self.move_cars_2}
		self.actions = [*range(-5, 6)]

	def timestep(self):
		sleep(.5)
		self.day += 1
		return self.day

	def max_cars(self, max_cars):
		# ic(max_cars if max_cars <= 20 else 20, max_cars)
		return max_cars if max_cars <= 20 else 20  # max 20 cars at each location

	def check_availability(self, cars_at_location, demand):
		if demand > self.location1 or demand > self.location2:
			ic('sys.exit: 0 cars at location')
			# return False
			sys.exit()
		return demand if demand < cars_at_location else cars_at_location

	def requests(self):
		available_at_1 = self.check_availability(self.location1, np.random.poisson(lam=3.0))
		# ic(available_at_1)
		self.location1 -= available_at_1
		self.total(rented_cars=available_at_1)

		available_at_2 = self.check_availability(self.location2, np.random.poisson(lam=4.0))
		# ic(available_at_2)
		self.location2 -= available_at_2
		self.total(rented_cars=available_at_2)

	def returns(self):
		self.timestep()
		returned_at_1 = np.random.poisson(lam=3.0)
		self.location1 += returned_at_1
		self.location1 = self.max_cars(self.location1)

		returned_at_2 = np.random.poisson(lam=2.0)
		self.location2 += returned_at_2
		self.location2 = self.max_cars(self.location2)

	def step(self, state: int, action: int):

		if self.location1 >= 15 and self.location2 <= 5:
			self.location1 -= 5
			self.location2 += 5
			self.total(moved_cars=action)
			return self.location1, 2

		elif self.location1 >= 10 and self.location2 <= 5:
			self.location1 -= 4
			self.location2 += 4
			self.total(moved_cars=action)
			return self.location1, 1

		elif self.location1 >= 8 and self.location2 <= 3:
			self.location1 -= 3
			self.location2 += 3
			self.total(moved_cars=action)
			return self.location1, .5
		else:
			return self.location1, -1

	def total(self, rented_cars=0, moved_cars=0):
		if rented_cars:
			self.amount += rented_cars * 10  # commission
		if moved_cars:
			self.amount -= moved_cars * 2  # cost
		return self.amount

	def policy_evaluation(self):

		while True:
			delta = 0
			for s in self.S[:-1, 0]:
				# print(s)
				v = self.value_dict[s]
				a = self.policy[s]
				s_prime, r = self.step(s, a)
				# print(s, s_prime)
				self.value_dict[s] = r + self.GAMMA * self.value_dict[s_prime]
				delta = max(delta, abs(v - self.value_dict[s]))
				if delta < self.THETA:
					break
			# print(self.value_dict)
			return self.value_dict

	def policy_improvement(self):
		for row in range(len(self.S[0])):
			for s in range(1, row):
				action_values = {}
				old_action = self.policy[s]
				for a in self.actions:
					s_prime, r = self.step(s, a)
					action_value = r + self.GAMMA * self.value_dict[s_prime]
					action_values[a] = action_value
				# ic(action_values[a])
				self.policy[s] = max(action_values, key=action_values.get)  # policy extraction
				self.S[row, s] = self.policy[s]
				# print(self.S)
				if self.policy[s] != old_action:
					self.policy_evaluation()
					self.policy_improvement()
		return self.policy


policy = {s + row: random.choice([* range(-5, 6)]) for s in range(1, 21) for row in range(381)}
print(policy)
S = np.zeros((21, 21), dtype=int)
idx = 20
for i in range(S.shape[1]):
	S[i, 0] = idx
	S[-1, i] = i
	idx -= 1

p = 1
for i in range(S.shape[1]):
	for j in range(1, 400 + 1):
		S[i:-1, 1:j + 1] = policy[j]
		# p += 1


# for row in S[:-1, 1:]:
# 	for s in row:
# 		for p in policy:
# 			S[idx:-1, 1:] = p

ic(S)

RB = RentalBusiness(S, policy)


ic(RB.location1)
ic(RB.location2)


while True:
	ic(RB.day)
	ic(RB.amount)
	ic('requests')
	RB.requests()
	ic(RB.location1)
	ic(RB.location2)

	ic('returns')
	RB.returns()  # changes day/state
	ic(RB.location1)
	ic(RB.location2)

	ic('moves')
	# move cars
	RB.policy_evaluation()
	RB.policy_improvement()


	# on the next day
	# RB.move_cars('first', 'second', quantity)
	# RB.move_cars('second', 'first', quantity)
	ic(RB.location1)
	ic(RB.location2)

	ic('FINITO')



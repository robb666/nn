import numpy as np
from icecream import ic
import sys
from typing import Dict
from time import sleep
import random


np.set_printoptions(linewidth=200)


class RentalBusiness:
	def __init__(self, S, policy, theta=.01, gamma=.9, cars_num_1=10, cars_num_2=10):
		self.S = S
		self.policy = policy
		# print(self.policy)
		self.THETA = theta
		self.GAMMA = gamma
		self.day = 1
		self.location1 = cars_num_1
		self.location2 = cars_num_2
		self.value_dict: Dict[int, float] = {s + row: 0. for s in range(1, 21) for row in range(381)}
		# print(self.value_dict)
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
		# print(max_cars if max_cars <= 20 else 20, max_cars)
		return max_cars if max_cars <= 20 else 20  # max 20 cars at each location

	def check_availability(self, cars_at_location, demand):
		# if demand > self.location1 or demand > self.location2:
		if demand > cars_at_location:
			print('sys.exit: 0 cars at location')
			sys.exit()
		return demand if demand < cars_at_location else cars_at_location

	def requests(self):
		available_at_1 = self.check_availability(self.location1, np.random.poisson(lam=3.0))
		# print(available_at_1)
		self.location1 -= available_at_1
		self.total(rented_cars=available_at_1)

		available_at_2 = self.check_availability(self.location2, np.random.poisson(lam=4.0))
		# print(available_at_2)
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

	def step(self, state: tuple, action: int):
		# print('state: ', state)
		loc_1 = self.S[state[0], 0]
		loc_2 = state[1]
		# print((loc_1, loc_2), self.S[state[0], state[1]], action)

		if loc_1 - action > 0:
			loc_1 -= action
			loc_1 = self.max_cars(loc_1)
		else:
			next_state = self.S[-loc_1 - 1][loc_2]
			return next_state, 0

		if loc_2 + action > 0:
			loc_2 += action
			loc_2 = self.max_cars(loc_2)
		else:
			next_state = self.S[-loc_1 - 1][loc_2]
			return next_state, 0

		next_state = self.S[-loc_1 - 1][loc_2]
		self.total(moved_cars=action)

		if loc_1 == loc_2:
			return next_state, .6

		else:
			return next_state, .4

	def total(self, rented_cars=0, moved_cars=0):
		if rented_cars:
			self.amount += rented_cars * 10  # commission
		if moved_cars:
			self.amount -= moved_cars * 2  # cost
		return self.amount

	def policy_evaluation(self):
		while True:
			delta = 0
			for row_idx, row in enumerate(self.S[:-1, 1:]):
				for col_idx, s in enumerate(row, start=1):
					# print('--->', row_idx, col_idx)
					v = self.value_dict[s]
					a = self.policy[s]
					s_prime, r = self.step((row_idx, col_idx), a)
					# print(s, a, s_prime)
					self.value_dict[s] = r + self.GAMMA * self.value_dict[s_prime]
					delta = max(delta, abs(v - self.value_dict[s]))
			if delta < self.THETA:
				break
		# print(self.value_dict)
		return self.value_dict

	def policy_improvement(self):
		new_S = self.S.copy()
		for row_idx, row in enumerate(self.S[:-1, 1:]):
			for col_idx, s in enumerate(row, start=1):
				action_values = {}
				old_action = self.policy[s]
				for a in self.actions:
					s_prime, r = self.step((row_idx, col_idx), a)
					action_value = r + self.GAMMA * self.value_dict[s_prime]
					action_values[a] = action_value
				# print(action_values[a])
				self.policy[s] = max(action_values, key=action_values.get)  # policy extraction

				new_S[row_idx, col_idx] = self.policy[s]
				print(new_S)

				if self.policy[s] != old_action:
					self.policy_evaluation()
					self.policy_improvement()
		# print(self.policy)
		return self.policy


policy = {s + row: random.choice([*range(-5, 6)]) for s in range(1, 21) for row in range(381)}
print(policy)
S = np.zeros((21, 21), dtype=int)
idx = 20
for i in range(S.shape[1]):
	S[i, 0] = idx
	S[-1, i] = i
	idx -= 1

i = 1
for row_idx, row in enumerate(S[:-1, 1:], start=0):
	for col_idx, _ in enumerate(row, start=1):
		S[row_idx, col_idx] = i
		i += 1

S[:-1, 1:] = S[:-1, 1:][::-1]

print(S)

RB = RentalBusiness(S, policy)


print(RB.location1)
print(RB.location2)


while True:
	print(RB.day)
	print(RB.amount)
	print('requests')
	RB.requests()
	print(RB.location1)
	print(RB.location2)

	print('returns')
	RB.returns()  # changes day/state
	print(RB.location1)
	print(RB.location2)

	print('moves')
	# move cars
	RB.policy_evaluation()
	RB.policy_improvement()


	# on the next day
	# RB.move_cars('first', 'second', quantity)
	# RB.move_cars('second', 'first', quantity)
	print(RB.location1)
	print(RB.location2)

	print('FINITO')



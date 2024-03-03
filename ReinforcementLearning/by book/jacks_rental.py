import numpy as np
from icecream import ic
import sys
from typing import Dict
from time import sleep
import random
import numpy as np


np.set_printoptions(linewidth=100)


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
		# ic(self.value_dict)/
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
		# cars_num = action if action <= 5 else 5
		# self.available = self.check_availability(state, action)

		# if self.available == 0:
		# 	return state, -1
		# else:
		# self.location1 -= self.available
		# self.location2 += self.available
		# self.total(moved_cars=abs(self.available))
		# self.location1 = self.max_cars(self.location1)
		# self.location2 = self.max_cars(self.location2)
		# return self.location1, 1

		if self.location1 > 10 and self.location2 < 6:
			state -= action
			self.location1 -= action
			self.location2 += action
			self.total(moved_cars=action)
			return self.location1, 1

		else:
			return self.location1, 0


	def total(self, rented_cars=0, moved_cars=0):
		if rented_cars:
			self.amount += rented_cars * 10  # commission
		if moved_cars:
			self.amount -= moved_cars * 2  # cost
		return self.amount

	# def move_cars_2(self, quantity: int = 2):
	# 	cars_num = quantity if quantity <= 5 else 5
	# 	self.available = self.check_availability(self.location2, cars_num)
	# 	self.location2 -= self.available
	# 	self.location1 += self.available
	# 	self.location1 = self.max_cars(self.location1)
	# 	self.total(moved_cars=self.available)


	# def reward(self, s, a, s_prime):
	# 	if s + a and a == move_1_2(1):
	# 		return -1

	def policy_evaluation(self):
		while True:
			delta = 0
			for row in self.S:
				for s in row:
					s = s
					v = self.value_dict[s]
					a = self.policy[s]
					s_prime, r = self.step(s, a)
					print(s_prime)
					self.value_dict[s] = r + self.GAMMA * self.value_dict[s_prime]
					delta = max(delta, abs(v - self.value_dict[s]))
				if delta < self.THETA:
					break
			# print(self.value_dict)
			return self.value_dict

	def policy_improvement(self):
		for row in self.S:
			for s in row:
				s = s
				action_values = {}
				old_action = self.policy[s]
				for a in self.actions:
					s_prime, r = self.step(s, a)
					# r = self.reward(s, a, s_prime)
					action_value = r + self.GAMMA * self.value_dict[s_prime]
					action_values[a] = action_value
				# ic(action_values[a])
				self.policy[s] = max(action_values, key=action_values.get)  # policy extraction
				if self.policy[s] != old_action:
					self.policy_evaluation()
					self.policy_improvement()
		return self.policy


# policy = {s: random.choice([*range(-5, 6)]) for s in range(1, 21)}

# policy = np.zeros((20, 20))
policy = {s + row: random.choice([* range(-5, 6)]) for s in range(1, 21) for row in range(381)}
print(policy)
S = np.zeros((20, 20), dtype=int)
ic(S)
# THETA = .01
# GAMMA = .9
#
# cars_loc_1, cars_loc_2 = 10, 10

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


value_dict = RB.policy_evaluation()
improved_policy = RB.policy_improvement()

ic(improved_policy, value_dict)

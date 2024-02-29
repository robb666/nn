import numpy as np
from icecream import ic
import sys
from time import sleep


# 6marca
class RentalBusiness:
	def __init__(self, policy, theta, gamma):
		self.policy = policy
		self.THETA = theta
		self.GAMMA = gamma
		self.day = 1
		self.location1 = 10
		self.location2 = 10
		self.moved = 0
		self.amount = 0
		self.available: int = 0
		self.actions_def = {
			'1': self.move_cars_1,
			'2': self.move_cars_2
		}
		self.actions = ['1', '2']

	def timestep(self):
		# sleep(.5)
		self.day += 1
		return self.day

	def max_cars(self, max_cars):
		ic(max_cars if max_cars <= 20 else 20, max_cars)
		return max_cars if max_cars <= 20 else 20  # max 20 cars at each location

	def check_availability(self, cars_at_location, demand):
		if demand > self.location1 or demand > self.location2:
			ic('sys.exit')
			sys.exit()
		return demand if demand < cars_at_location else cars_at_location

	def requests(self):
		available_at_1 = self.check_availability(self.location1, np.random.poisson(lam=3.0))
		ic(available_at_1)
		self.location1 -= available_at_1
		self.total(rented_cars=available_at_1)

		available_at_2 = self.check_availability(self.location2, np.random.poisson(lam=4.0))
		ic(available_at_2)
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

	def move_cars_1(self, quantity: int = 1):
		cars_num = quantity if quantity <= 5 else 5
		self.available = self.check_availability(self.location1, cars_num)
		self.location1 -= self.available
		self.location2 += self.available
		self.location2 = self.max_cars(self.location2)
		self.total(moved_cars=self.available)

	def move_cars_2(self, quantity: int = 1):
		cars_num = quantity if quantity <= 5 else 5
		self.available = self.check_availability(self.location2, cars_num)
		self.location2 -= self.available
		self.location1 += self.available
		self.location1 = self.max_cars(self.location1)
		self.total(moved_cars=self.available)

	def policy_action(self):
		if self.location1 > self.location2:
			# ic(self.policy['2'])
			self.actions_def['1']()
		if self.location1 < self.location2:
			# ic(self.policy['2'])
			self.actions_def['2']()

	# def policy_evaluation(self):
	# 	while True:
	# 		delta = 0
	# 		for s in self.S:
	# 			v = self.value_dict[s]
	# 			a = self.policy[s]
	# 			s_prime = self.step(s, a)
	# 			self.value_dict[s] = self.reward(s, a, s_prime) + self.gamma * self.value_dict[s_prime]
	# 			delta = max(delta, abs(v - self.value_dict[s]))
	# 		if delta < self.theta:
	# 			break
	# 	return self.value_dict

	def total(self, rented_cars=0, moved_cars=0):
		if rented_cars:
			self.amount += rented_cars * 10  # commission
		if moved_cars:
			self.amount -= moved_cars * 2  # cost
		return self.amount


policy = {'1': 1,  '2': 0}

THETA = .01
GAMMA = .9


RB = RentalBusiness(policy, GAMMA, THETA)

ic(RB.location1)
ic(RB.location2)


for _ in range(10):
	ic(RB.day)
	ic('requests')
	RB.requests()
	ic(RB.location1)
	ic(RB.location2)

	# on the next day
	ic('returns')
	RB.returns()  # changes day/state
	ic(RB.location1)
	ic(RB.location2)

	ic('moves')
	# move cars
	RB.policy_action()
	# RB.move_cars('first', 'second', quantity)
	# RB.move_cars('second', 'first', quantity)
	ic(RB.location1)
	ic(RB.location2)

ic()
ic(RB.location1)
ic(RB.location2)
ic(RB.actions_def['1']())
# ic(RB.actions_def['2'])
ic(RB.total())
ic(RB.day)
ic(RB.location1, RB.location2)


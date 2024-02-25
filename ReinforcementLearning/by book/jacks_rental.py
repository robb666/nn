import numpy as np
from icecream import ic


class Locations:
	loc_1 = 1
	loc_1 = loc_1 if loc_1 <= 20 else 20  # max 20 cars at each location
	loc_2 = 0
	loc_2 = loc_2 if loc_2 <= 20 else 20  # max 20 cars at each location


class RequestsPerDay:
	# loc_1 = np.random.poisson(lam=3.0)
	loc_1 = 0
	# loc_2 = np.random.poisson(lam=4.0)
	loc_2 = 1


class ReturnsPerDay:
	loc_1 = np.random.poisson(lam=3.0)
	loc_2 = np.random.poisson(lam=2.0)


class RentalBusiness:
	def __init__(self):
		self.available_at_1 = self.check_availability(Locations.loc_1, RequestsPerDay.loc_1)
		self.available_at_2 = self.check_availability(Locations.loc_2, RequestsPerDay.loc_2)
		print(self.available_at_1)
		self.actions_def = {
			'1': self.move_cars('first', 'second', self.available_at_2),
			'2': self.move_cars('second', 'first', self.available_at_1)
		}
		self.actions = ['1', '2']

	def timestep(self):
		day = 1
		return day

	def check_availability(self, cars_at_location, cars_num):
		return cars_num if cars_num < cars_at_location else cars_at_location

	def requests(self):
		Locations.loc_1 -= self.available_at_1
		Locations.loc_2 -= self.available_at_2

	def returns(self):
		Locations.loc_1 += ReturnsPerDay.loc_1
		Locations.loc_2 += ReturnsPerDay.loc_2

	def move_cars(self, from_: str, to_: str, quantity: int) -> int:
		cost = 2
		cars_num = quantity if quantity <= 5 else 5
		if from_ == 'first' and to_ == 'second':
		# if self.available_at_1 > self.available_at_2:
			available = self.check_availability(Locations.loc_1, cars_num)
			Locations.loc_1 -= available
			Locations.loc_2 += available
			return available * cost

		elif from_ == 'second' and to_ == 'first':
			available = self.check_availability(Locations.loc_2, cars_num)
			Locations.loc_2 -= available
			Locations.loc_1 += available
			return available * cost

	def commission(self):
		return (self.available_at_1 + self.available_at_2) * 10

	def total(self):
		amount = 0
		amount += self.commission()
		amount -= self.available_at_1 * 2
		amount -= self.available_at_2 * 2
		return amount


ic(Locations.loc_1)
ic(Locations.loc_2)

RB = RentalBusiness()

# ic(RB.move_cars(from_='first', to_='second', quantity=8))

RB.requests()
# RB.returns()
ic()
ic(Locations.loc_1)
ic(Locations.loc_2)

ic(RB.commission())
ic(RB.total())

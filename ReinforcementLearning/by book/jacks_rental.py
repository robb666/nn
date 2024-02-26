import numpy as np
from icecream import ic


class Locations:
	loc_1 = 1
	loc_1 = loc_1 if loc_1 <= 20 else 20  # max 20 cars at each location
	loc_2 = 1
	loc_2 = loc_2 if loc_2 <= 20 else 20  # max 20 cars at each location


class RequestsPerDay:
	# loc_1 = np.random.poisson(lam=3.0)
	loc_1 = 1
	# loc_2 = np.random.poisson(lam=4.0)
	loc_2 = 0


class ReturnsPerDay:
	loc_1 = np.random.poisson(lam=3.0)
	loc_2 = np.random.poisson(lam=2.0)


class RentalBusiness:
	def __init__(self):
		self.day = 1
		self.returned_at_1 = ReturnsPerDay.loc_1
		self.returned_at_2 = ReturnsPerDay.loc_2
		self.moved = 0
		self.rent_at_1 = self.check_availability(Locations.loc_1, RequestsPerDay.loc_1)
		self.rent_at_2 = self.check_availability(Locations.loc_2, RequestsPerDay.loc_2)
		self.available: int = 0

		print('rented_at_1: ', self.rent_at_1)
		self.actions_def = {
			# '1': self.move_cars('first', 'second', self.rent_at_2),
			# '2': self.move_cars('second', 'first', self.rent_at_1)
		}
		self.actions = ['1', '2']

	def timestep(self):
		self.day += 1
		return self.day

	def check_availability(self, cars_at_location, cars_num):
		if cars_at_location and self.day:  # available immediately
			cars_num = cars_num if cars_num < cars_at_location else cars_at_location
		if self.day > 1:  # available the next day
			# self.returned_at_1_list.append(ReturnsPerDay.loc_1)
			# self.returned.append(self.move_cars('second', 'first', self.rent_at_1))

			print('returned + moved', self.returned_at_1, self.moved)
			return cars_num + self.returned_at_1 + self.moved
		# self.timestep()
		return cars_num

	def requests(self):
		Locations.loc_1 -= self.rent_at_1
		Locations.loc_2 -= self.rent_at_2

	def returns(self):
		Locations.loc_1 += self.returned_at_1
		Locations.loc_2 += self.returned_at_2

	def move_cars(self, from_: str, to_: str, quantity: int) -> int:
		cost = 2
		cars_num = quantity if quantity <= 5 else 5
		if from_ == 'first' and to_ == 'second':
			self.available = self.check_availability(Locations.loc_1, cars_num)
			Locations.loc_1 -= self.available
			Locations.loc_2 += self.available
			return self.available * cost

		elif from_ == 'second' and to_ == 'first':
			self.available = self.check_availability(Locations.loc_2, cars_num)
			Locations.loc_2 -= self.available
			Locations.loc_1 += self.available
			return self.available * cost

	def commission(self):
		return (self.rent_at_1 + self.rent_at_2) * 10

	def total(self):
		amount = 0
		amount += self.commission()
		amount -= self.available * 2
		return amount


ic(Locations.loc_1)
ic(Locations.loc_2)

RB = RentalBusiness()

# ic(RB.move_cars(from_='first', to_='second', quantity=8))

RB.requests()
RB.returns()

print(RB.day)
ic()
ic(Locations.loc_1)
ic(Locations.loc_2)

ic(RB.commission())
ic(RB.total())
print(RB.timestep())

import numpy as np
from icecream import ic


class Locations:
	loc_1 = 6
	loc_1 = loc_1 if loc_1 <= 20 else 20  # max 20 cars at each location
	loc_2 = 0
	loc_2 = loc_2 if loc_2 <= 20 else 20  # max 20 cars at each location


def move_cars(from_: str, to_: str, num: int):
	cars_num = num if num <= 5 else 5

	if from_ == 'first' and to_ == 'second':
		available = cars_num if cars_num < Locations.loc_1 else Locations.loc_1
		Locations.loc_1 -= available
		Locations.loc_2 += available

	elif from_ == 'second' and to_ == 'first':
		available = cars_num if cars_num < Locations.loc_2 else Locations.loc_2
		Locations.loc_2 -= available
		Locations.loc_1 += available


class RequestsPerDay:
	loc_1 = np.random.poisson(lam=3.0)
	loc_2 = np.random.poisson(lam=4.0)


class ReturnsPerDay:
	loc_1 = np.random.poisson(lam=3.0)
	loc_2 = np.random.poisson(lam=2.0)


class RentalBusiness:
	def __init__(self, location1, location2):
		pass


ic(Locations.loc_1)
ic(Locations.loc_2)

move_cars(from_='first', to_='second', num=6)
# ic()
ic(Locations.loc_1)
ic(Locations.loc_2)

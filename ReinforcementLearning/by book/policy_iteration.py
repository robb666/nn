import numpy as np
import random
from typing import Dict
from icecream import ic


S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
S_prim = [1, 2, 3, 4, 5, 6, 7, 9, 10]


def reward(s, s_prim):
	if s == 8 and s_prim == 9:
		return 3
	elif s == 7 and s_prim == 9:
		return 2
	else:
		return 1


def step(s):
	if s == 8:
		return 9
	elif s == 7:
		return 9
	else:
		return random.choice(S_prim)


def policy_evaluation(theta, gamma):
	value_dict: Dict[int, float] = {s: 0.0 for s in S}
	while True:
		delta = 0
		for s in S:
			v = value_dict[s]
			s_prim = step(s)
			r = reward(s, s_prim)
			value_dict[s] = r + gamma * value_dict[s_prim]
			delta = max(delta, abs(v - value_dict[s]))
			# print(delta)
		if delta < theta:
			break
	return value_dict


def policy_improvement(S, policy):
	for s in S:
		old_action = policy[s]
		s_prim = step(s)
		r = reward(s, s_prim)
		policy[s] = max(r + gamma * policy[s_prim])
		if old_action >= policy[s]:
			return policy
		else:
			policy_evaluation(theta, gamma)


theta = .001
gamma = .9

policy = policy_evaluation(theta, gamma)
# policy_improvement(S, policy)

ic(policy)























# Leszek Józwik
# Ja miałem fajną sytuację: Kurator podzielił przedmioty, ja miałem odrabiać lekcje z 3 przedmiotów, żona pozostałe.
# Dzieci miały lepsze wyniki z moich przedmiotów (geografia, historia itd) żona miała gorsze mimo, że jest nauczycielem matematyki,
# biologii. I teraz najlepsze: Sąd stwierdził, że nie dostanę kontaktów w tygodniu, dlatego że ...... ram pam pam .....
# nie odrabiam lekcji z dziećmi w tygodniu. 🤣🤣🤣 Cyrk. Kurtyna

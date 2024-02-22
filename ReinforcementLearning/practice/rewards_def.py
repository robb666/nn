import numpy as np


def stochastic_reward(state, action):
	# Define mean rewards based on state-action pairs
	mean_rewards = {
		('state1', 'action1'): 5,
		('state1', 'action2'): 3,
		('state2', 'action1'): 2,
		('state2', 'action2'): 4,
	}
	# Define variability (standard deviation) for each state-action pair
	reward_variability = {
		('state1', 'action1'): 1,
		('state1', 'action2'): 0.1,
		('state2', 'action1'): 1.5,
		('state2', 'action2'): 1,
	}

	# Get mean reward and variability for the current state-action pair
	mean = mean_rewards.get((state, action), 0)  # Default to 0 if not defined
	variability = reward_variability.get((state, action), 0.1)  # Minimal variability by default

	# Sample from a normal distribution
	reward = np.random.normal(mean, variability)
	return reward

print(stochastic_reward('state1', 'action2'))

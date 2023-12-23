import random
import time

import matplotlib.pyplot as plt
import seaborn as sns
from icecream import ic
import numpy as np


def epsilon_greedy(Q, state, epsilon):
    # If a random number is less than epsilon, choose a random action (explore)
    if np.random.random() < epsilon:
        return np.random.choice(len(Q[state]))
    # Otherwise, choose the best action for the current state (exploit)
    else:
        return np.argmax(Q[state])


# Suppose we have 5 states and 3 actions, and we're currently in state 2
Q_example = np.random.rand(5, 3)  # Random Q-table for demonstration

current_state = 2
epsilon_example = 0.5  # 10% chance to explore
chosen_action = epsilon_greedy(Q_example, current_state, epsilon_example)








num_of_games = 11
num_of_actions = 10
epsilon = .90
lambda_ = .99


mean, variance = 0, 1  # mean and standard deviation

action_chosen = []

true_values = np.random.normal(mean, variance, num_of_actions)

ic(true_values)

rewards = []
# print(rewards_distribution)


for action, true_value in enumerate(true_values, 1):

    rewards_distribution = np.random.normal(true_value, variance, 10)
    rewards.append(rewards_distribution)
ic(rewards)


#     print(rewards)
#     if np.random.random() > epsilon:
#         action = np.random.choice(rewards)
#         action_chosen.append(actions[action])
#     else:
#         action = np.argmax(rewards)
#         action_chosen.append(actions[action])
#
#
# time.sleep(.3)
# ic(action_chosen)

print(len(true_values))
print(len(rewards))


fig, ax = plt.subplots(figsize=(10, 6))
plt.violinplot(rewards, positions=true_values)



ax.xaxis.grid(True)
ax.set_xticks(true_values)

# sns.set_theme()
# sns.relplot(
#     data=rewards_distribution,
#     x=[i for i in range(10)],
#     y=rewards_distribution,
# )

plt.show()

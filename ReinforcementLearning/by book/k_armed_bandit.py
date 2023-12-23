import os
import time

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)


class Environment:
    def __init__(self, probs):
        self.probs = probs

    def step(self, action):
        return 1 if (np.random.random() < self.probs[action]) else 0


class Agent:
    def __init__(self, nActions, eps):
        self.nActions = nActions
        self.eps = eps
        self.n = np.zeros(nActions, dtype=int)
        self.Q = np.zeros(nActions, dtype=float)

    def update_Q(self, action, reward, i):
        self.n[action] += 1
        self.Q[action] += (1.0 / self.n[action]) * (reward - self.Q[action])
        if i / 499 == 1:
            time.sleep(2.8)
            print()
            print(self.Q)

    def get_action(self):
        if np.random.random() < self.eps:
            return np.random.randint(self.nActions)
        else:
            return np.random.choice(np.flatnonzero(self.Q == self.Q.max()))


def experiment(probs, N_episodes):
    env = Environment(probs)
    agent = Agent(len(env.probs), eps)
    actions, rewards = [], []

    for episode in range(N_episodes):
        action = agent.get_action()
        reward = env.step(action)
        agent.update_Q(action, reward, episode)
        actions.append(action)
        rewards.append(reward)
    return np.array(actions), np.array(rewards)


# Settings
probs = [.10, .50, .60, .80, .10, .25, .60, .45, .75, .65]

N_steps = 500
N_experiments = 10_000
eps = 0.115
save_fig = True
output_dir = os.path.join(os.getcwd(), 'output')

# Run experiments
print('running multi-armed bandits with nActions = {}, eps = {}'.format(len(probs), eps))
R = np.zeros((N_steps,))  # reward history sum. 500 x 1
A = np.zeros((N_steps, len(probs)))  # action history sum 500 x 10

for i in range(N_experiments):
    actions, rewards = experiment(probs, N_steps)  # perform
    if (i + 1) % (N_experiments / 100) == 0:
        print('[Experiment {}/{}] '.format(i + 1, N_experiments) +
              'n_steps = {}, '.format(N_steps) +
              'reward_avg = {}'.format(np.sum(rewards) / len(rewards)))
        print('sum rewards; ', np.sum(rewards), 'len rewards; ', len(rewards))
    R += rewards  # Adding rewards for every time step across all experiments: 500x1
    for j, a in enumerate(actions):
        A[j][a] += 1

# Plot reward results
R_avg = R / np.float32(N_experiments)
plt.plot(R_avg, '.')
plt.xlabel('Step')
plt.ylabel('Average Reward')
plt.grid()
ax = plt.gca()
plt.xlim([1, N_steps])
if save_fig:
    if not os.path.exists(output_dir): os.mkdir(output_dir)
    plt.savefig(os.path.join(output_dir, 'rewards.png'), bbox_inches='tight')
else:
    plt.show()
plt.close()

# Plot action results
for i in range(len(probs)):
    A_pct = 100 * A[:, i] / N_experiments
    # Each cell is number of times the action i was selected for time step j across all experiments
    steps = list(np.array(range(len(A_pct))) + 1)
    # Plotting line chart for one action at a time.
    plt.plot(steps, A_pct, '-',
              linewidth=4,
              label='Arm {} ({:.0f}%)'.format(i + 1, 100 * probs[i]))  # Incrementing Arm + 1 as they start with 0 index
    # We should ideally see as timesteps go on, the slot with the largest probability of success is chosen the most.
    # actions.png
plt.xlabel('Step')
plt.ylabel('Count Percentage (%)')
leg = plt.legend(loc='upper left', shadow=True)
plt.xlim([1, 100])
for legobj in leg.legendHandles:
    legobj.set_linewidth(4.0)
if save_fig:
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    plt.savefig(os.path.join(output_dir, 'actions.png'), bbox_inches='tight')
else:
    plt.show()
plt.close()

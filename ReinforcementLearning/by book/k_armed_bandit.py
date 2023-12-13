import os
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
        self.n = np.zeros(nActions, dtype=np.int)
        self.Q = np.zeros(nActions, dtype=np.float)

    def update_Q(self, action, reward):
        self.n[action] += 1
        self.Q[action] += (1.0 / self.n[action]) * (reward - self.Q[action])

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
        agent.update_Q(action, reward)
        actions.append(action)
        rewards.append(reward)
    return np.array(actions), np.array(rewards)


# Settings
probs = [.10, .50, .60, .80, .10, .25, .60, .45, .75, .65]
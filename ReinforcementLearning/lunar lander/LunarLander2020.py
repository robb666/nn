# import gym
import gymnasium as gym
from simple_dqn_torch_2020 import Agent
from ReinforcementLearning.util import plot_learning_curve
import numpy as np
from icecream import ic


if __name__ == '__main__':
    env = gym.make('LunarLander-v2', render_mode="human")
    print(env.)
    agent = Agent(gamma=0.99, epsilon=1.0, batch_size=64, n_actions=4,
                  eps_end=0.01, input_dims=[8, 8], lr=0.003)
    scores, eps_history = [], []
    n_games = 100
    for i in range(n_games):

        score = 0
        done = False
        observation = env.reset()
        while not done:
            env.render()
            action = agent.choose_action(observation[0])
            observation_, reward, done, _, info = env.step(action)
            ic(observation_, reward, done, _, info)
            score += reward
            agent.store_transition(observation[0], action, reward,
                                   observation_, done)
            agent.learn()
            observation = observation_
        scores.append(score)
        eps_history.append(agent.epsilon)

        avg_score = np.mean(scores[-100:])

        print('episode ', i, 'score %.2f' % score,
              'average score %.2f' % avg_score,
              'epsilon %.2f' % agent.epsilon)
    x = [i + 1 for i in range(n_games)]
    filename = 'lunar_lander_2020.png'
    plot_learning_curve(x, scores, eps_history, filename)
    #plotLearning

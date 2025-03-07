# import gym
import gymnasium as gym
from simple_dqn_torch_2020 import Agent
from util import plot_learning_curve
import numpy as np
from icecream import ic
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
print(gym.__version__)


if __name__ == '__main__':
    env = gym.make('LunarLander-v2', render_mode="human")
    # ic(env.action_space)
    load_checkpoint = True
    
    agent = Agent(gamma=0.99, epsilon=1.0, batch_size=64, n_actions=4,
                  eps_end=0.001, input_dims=[8], lr=0.0002)
    
    if load_checkpoint:
        agent.load_model()
    scores, eps_history = [], []
    n_games = 15000  # 30000 used to be for gymnasium
    
    for i in range(n_games):
        score = 0
        done = False
        observation, info = env.reset()  # gymnasium
        # observation = env.reset()
        # ic(observation, info)

        while not done:
            # env.render()
            action = agent.choose_action(observation)
            observation_, reward, terminated, truncated, info = env.step(action)  # gymnasium
            ic(observation, observation_, reward)
            # observation_, reward, done, info = env.step(action)
            done = terminated or truncated  # gymnasium

            score += reward
            agent.store_transition(observation, action, reward,
                                   observation_, done)
            agent.learn()
            observation = observation_
        scores.append(score)
        eps_history.append(agent.epsilon)

        avg_score = np.mean(scores[-100:])

        if i % 100 == 0 and i > 0:
            print('episode ', i, 'score %.2f' % score,
                  'average score %.2f' % avg_score,
                  'epsilon %.2f' % agent.epsilon)
            # agent.save_model()

    x = [i + 1 for i in range(n_games)]
    filename = 'plots/lunar_lander_gymnasium_last_500_lr_0005_eps_dec_5e-5.png'
    plot_learning_curve(x, scores, eps_history, filename)

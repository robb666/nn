import gymnasium as gym
from model import DeepQNetwork, Agent
# from ReinforcementLearning.util import plot_learning_curve
import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt

print(np.__version__)

# np.set_printoptions(threshold=np.inf, linewidth=np.inf)
np.set_printoptions(threshold=sys.maxsize)




if __name__ == '__main__':
    env = gym.make('ALE/SpaceInvaders-v5') #, render_mode='human')
    brain = Agent(gamma=0.95, epsilon=1.0,
                  alpha=0.003, maxMemorySize=5000, replace=None)

    # while brain.memCntr < brain.memSize:
    #     observation, info = env.reset()
    #     print(observation.shape)
    #     done = False
    #     while not done:
    #         # 0 no action, 1 fire, 2 move right, 3 move left, 4 move right fire, 5 move left fire
    #         action = env.action_space.sample()
    #         observation_, reward, terminated, truncated, info = env.step(action)
    #         # print(info)
    #         done = terminated or truncated
    #         if done and info['lives'] == 0:
    #             reward = -100
    #         brain.storeTransition(np.mean(observation[15:200, 30:126], axis=2), action, reward,
    #                               np.mean(observation_[15:200, 30:126], axis=2))
    #         observation = observation_
    # print('done initializing memory')

    scores = []
    epsHistory = []
    numGames = 50
    batch_size = 32

    for i in range(numGames):
        print('starting game ', i + 1, 'epsilon: %.4f' % brain.EPSILON)
        done = False
        observation, info = env.reset()
        # print(np.array2string(observation))
        # print(observation)

        # print('OBSERVATION LEN: \n', observation)
        frames = [np.sum(observation[15:200, 30:125], axis=2)]
        score = 0
        lastAction = 0

        while not done:
            if len(frames) == 3:
                action = brain.chooseAction(frames)
                frames = []
            else:
                action = lastAction

            observation_, reward, terminated, truncated, info = env.step(action)
            print(info)
            done = terminated or truncated
            score += reward
            frames.append(np.sum(observation_[15:200, 30:125], axis=2))

            scale_factor = 3 # You can adjust this value to make it larger or smaller
            resized_image = cv2.resize(observation_[15:200, 30:125], None, fx=scale_factor, fy=scale_factor)
            cv2.imshow('observation', resized_image)
            cv2.waitKey(0)

            if done and info['lives'] == 0:
                reward = -100
            brain.storeTransition(np.mean(observation[15:200, 30:125], axis=2), action, reward,
                                  np.mean(observation_[15:200, 30:125], axis=2))
            observation = observation_
            brain.learn(batch_size)
            lastAction = action
            # env.render()

        scores.append(score)
        print('score: ', score)

    x = [i + 1 for i in range(numGames)]
    fileName = str(numGames) + 'Games' + 'Gamma' + str(brain.GAMMA) + \
               'Alpha' + str(brain.ALPHA) + 'Memory' + str(brain.memSize) + '.png'
    plot_learning_curve(x, scores, epsHistory, fileName)

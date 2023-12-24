import gymnasium as gym
from breakout_torch import DeepQNetwork, Agent
import numpy as np
from ReinforcementLearning.util import plot_learning_curve
# from gym import wrappers
from icecream import ic


def preprocess(observation):
    # observation = observation / 255
    return np.mean(observation[30:, :], axis=2).reshape(180, 160, 1)


def stack_frames(stacked_frames, frame, buffer_size):
    # print(stacked_frames, frame.shape, buffer_size)
    if stacked_frames is None:
        stacked_frames = np.zeros((buffer_size, *frame.shape))
        for idx, _ in enumerate(stacked_frames):
            stacked_frames[idx, :] = frame
    else:
        stacked_frames[0:buffer_size-1, :] = stacked_frames[1:, :]
        stacked_frames[buffer_size-1, :] = frame

    stacked_frames = stacked_frames.reshape(1, *frame.shape[0:2], buffer_size)
    # print(stacked_frames.shape, type(stacked_frames))
    return stacked_frames


if __name__ == '__main__':
    env = gym.make('ALE/Breakout-v5', render_mode='human')
    ic(env)
    load_checkpoint = False
    agent = Agent(gamma=0.99, epsilon=1.0, lr=0.00025, input_dims=(180, 160, 4),
                  n_actions=3, batch_size=1)
    if load_checkpoint:
        agent.load_models()
    scores = []
    eps_history = []
    numGames = 200
    stack_size = 4
    score = 0

    while agent.mem_cntr < 12500:
        done = False
        observation, info = env.reset()
        observation = preprocess(observation)
        stacked_frames = None
        observation = stack_frames(stacked_frames, observation, stack_size)
        while not done:
            action = np.random.choice([0, 1, 2])
            action += 1
            observation_, reward, terminated, truncated, info = env.step(action)
            observation_ = stack_frames(stacked_frames, preprocess(observation_),
                                        stack_size)
            action -= 1
            agent.store_transition(observation, action, reward,
                                   observation_, int(done))
            observation = observation_

            # env.render()
    print('Done with random gameplay, game on.')

    for i in range(numGames):
        done = False
        if i % 10 == 0 and i > 0:
            avg_score = np.mean(scores[max(0, i-10): (i+1)])
            print('episode', i, 'score', score,
                  'average_score %.3f' % avg_score,
                  'epsilon %.3f' % agent.epsilon)
            # agent.save_model()
        else:
            print('episode: ', i, 'score', score)
        observation, info = env.reset()
        observation = preprocess(observation)
        stacked_frames = None
        observation = stack_frames(stacked_frames, observation, stack_size)

        while not done:
            action = agent.choose_action([0, 1, 2])
            action += 1
            observation_, reward, terminated, truncated, info = env.step(action)
            observation_ = stack_frames(stacked_frames, preprocess(observation_),
                                        stack_size)
            action -= 1
            agent.store_transition(observation, action, reward,
                                   observation_, int(done))
            observation = observation_

            agent.learn()
    scores.append(score)







    # # n_steps = 0
    # for i in range(numGames):
    #     done = False
    #
    #     # observation = env.reset()
    #     observation, info = env.reset()
    #     observation = preprocess(observation)
    #     # print('obezrvation: ', observation)
    #     ic('obezrvation 1 shape: ', observation.shape)
    #     stacked_frames = None
    #     observation = stack_frames(stacked_frames, observation, stack_size)
    #     score = 0
    #     while not done:
    #         action = agent.choose_action(observation)
    #         action += 1
    #         # observation_, reward, done, _, info = env.step(action)
    #         observation_, reward, terminated, truncated, info = env.step(action)
    #         ic('obezrvation 2 shape: ', observation_.shape)
    #         n_steps += 1
    #         ic(n_steps)
    #         observation_ = stack_frames(stacked_frames, preprocess(observation_), stack_size)
    #         score += reward
    #         action -= 1
    #         agent.store_transition(observation, action, reward,
    #                                observation_, int(done))
    #         observation = observation_
    #         if n_steps % 4 == 0:
    #             agent.learn()
    #     if i % 10 == 0 and i > 0:
    #         avg_score = np.mean(scores[max(0, i - 10):(i + 1)])
    #         print('episode', i, 'score', score,
    #               'average_score %.3f' % avg_score,
    #               'epsilon %.3f' % agent.epsilon)
    #
    #         # agent.save_models()
    #     else:
    #         print('episode: ', i, 'score', score)
    #
    #     eps_history.append(agent.epsilon)
    #     scores.append(score)
    #
    # x = [i + 1 for i in range(numGames)]
    # plot_learning_curve(x, scores, eps_history, 'training_plot.jpg')


import gym
import Box2D
print(Box2D.__version__)


env = gym.make("LunarLander-v2")

env.reset()

print("sample action: ", env.action_space.sample())


print('observation space shape', env.observation_space.shape)
print('sample observation', env.observation_space.sample())

env.close()



# fp, pathname, description = imp.find_module('_Box2D', [dirname(__file__)])

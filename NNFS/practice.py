import numpy as np
import math
import os


class Layer_Dense:

    # Layer initialization
    def __init__(self, n_inputs, n_neurons):
        # Initialize weights and biases
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        # # Set regularization strength
        # self.weight_regularizer_l1 = weight_regularizer_l1
        # self.weight_regularizer_l2 = weight_regularizer_l2
        # self.bias_regularizer_l1 = bias_regularizer_l1
        # self.bias_regularizer_l2 = bias_regularizer_l2

    # Forward pass
    def forward(self, inputs, training):
        # Remember input values
        self.inputs = inputs
        # Calculate output values from inputs, weights and biases
        self.output = np.dot(inputs, self.weights) + self.biases




class Optimizer_Adam:

    # Initialize optimizer - set settings
    def __init__(self, learning_rate=0.001, decay=0., epsilon=1e-7, beta_1=0.9, beta_2=0.999):
        self.learning_rate = learning_rate
        self.current_learning_rate = learning_rate
        self.decay = decay
        self.iterations = 0
        self.epsilon = epsilon
        self.beta_1 = beta_1
        self.beta_2 = beta_2


dweights = 5.3
n_neurons = 4
n_inputs = 3


weights = 0.1 * np.random.randn(n_inputs, n_neurons)
print(weights)

weight_momentums = np.zeros_like(weights)
print(weight_momentums)


beta_1 = 0.9



weight_momentums = beta_1 * weight_momentums + (1 - beta_1) * dweights


print(weight_momentums)









model = Layer_Dense
print(model)
# fp = model.forward(n_inputs, n_neurons, training=False)







# softmax_outputs = np.array([[0.7, 0.1, 0.2],
#                             [0.1, 0.5, 0.4],
#                             [0.02, 0.9, 0.08]])
#
# class_t = [0, 1, 1]
#
# class_targets = np.array([[1, 0, 0],
#                           [0, 1, 0],
#                           [0, 1, 0]])
#
#
# print(np.mean(- np.log(np.sum(softmax_outputs * class_targets, axis=1))))





# print(sum([1, 2, 3]) / len([1, 2, 3]))
# print(np.mean([1, 2, 3]))
# print(sum(np.array([1, 2, 3]) / sum([1, 2, 3])))
# print(-np.log())





# inputs = np.array([[4.8, 1.21, 2.385],
#                    [8.9, -1.81, 0.2],
#                    [1.41, 1.051, 0.026]])
#
# class_targets = [0, 1, 1]
#
# print(inputs[[0, 1, 2], class_targets])




# CLIP
# y_pred = 0.000009
# y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)
# print(y_pred_clipped)







# # Euler Expotentiation and Normalization in raw p
# li = [[1, 2, 3]]
# inputs = np.array([[4.8, 1.21, 2.385],
#                    [8.9, -1.81, 0.2],
#                    [1.41, 1.051, 0.026]])
#
# ex = np.exp(li - np.max(li, axis=1, keepdims=True))
# pro = ex / np.sum(ex, axis=1, keepdims=True)
# print(pro)
#
#
# li1 = [1, 2, 3]
# l = []
# l1 = []
# for i in li1:
#     exp1 = math.e ** (i - max(li1))
#     l.append(exp1)
#
# for j in l:
#     l1.append(j / sum(l))
# print(l1)








# """
# You have a million grams of a radioactive element with a half-life of one minute. This means that, every minute,
# the mass of the element halves. Of the following options,
# which is the shortest time after which you have less than a gram?
# """
#
#
# i = 1_000_000
# l = []
# while (n := i * 0.5) > 1:
#     i = n
#     l.append(i)
#
# for i, v in enumerate(l, start=1):
#     print(i, v)
#
#
#
#
# """
# Someone gives the choice between giving you one dollar today, two tomorrow, four the next day, and so forth,
# with the amount doubling each day for a month (31 days), or giving you a million dollars today.
# Which one will net you the most money?
# """
#
# i = 1
# l = []
# while (n := i*2) < 2_000_000_000:
#     i = n
#     l.append(i)
#
# for i, v in enumerate(l, start=2):
#     print(i, v)








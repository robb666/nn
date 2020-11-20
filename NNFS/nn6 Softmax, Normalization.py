# Softamx activation func
import math
import numpy as np

print(math.e)
print()

layer_outputs = [4.8, 1.21, --2.385]

exp_values = []
for output in layer_outputs:
    exp_values.append(math.e ** output)

# print('Expotentiated values')
# print(exp_values)

# Normalization
norm_base = sum(exp_values)
norm_val = []
for n in exp_values:
    norm_val.append(n / norm_base)

# print()
# print('Normalized:')
# print(norm_val)

# Normalization w/ NumPy
numpy_exp_values = np.exp(layer_outputs)
norm_values = numpy_exp_values / np.sum(numpy_exp_values)
# print()
# print('Numpy expotentiated values:')
# print(numpy_exp_values)
# print('Numpy sum of normalized values:')
# print(norm_values)
# print('\n\n\n')


# Get unnormalized probabilities

inputs = np.array([[4.8, 1.21, 2.385],
                   [8.9, -1.81, 0.2],
                   [1.41, 1.051, 0.026]])

exp_values = np.exp(inputs)

# np sum axis=0 sumuje kolumny
# np sum axis=1 sumuje rzędy
sum = np.sum(inputs, axis=1, keepdims=True)
# print('Sum without axis:')
# print(sum)


# Softmax activation
class Activation_Softmax:

    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)

        self.output = probabilities


# Some examples of dead/exploding neurons
# print(np.exp(-np.inf), np.exp(0))

softmax = Activation_Softmax()

softmax.forward([[-2, -1, 0]])
print(softmax.output)























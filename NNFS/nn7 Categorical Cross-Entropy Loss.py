import math


softmax_output = [0.7, 0.1, 0.2]
# Ground truth
target_output = [1, 0, 0]

"""Log loss"""
# loss = -(math.log(softmax_output[0])*target_output[0] +
#          math.log(softmax_output[1])*target_output[1] +
#          math.log(softmax_output[2])*target_output[2])

loss = - math.log(softmax_output[0])
print(loss)

print(math.log(1))
print(math.log(0.95))
print(math.log(0.9))
print(math.log(0.8))
print(math.log(0.7))
print('\n\n\n')


import numpy as np

b = 5.2
print(np.log(20.085536923187664))
print(math.e ** 3)
print('\n\n\n')



softmax_outputs = np.array([[0.7, 0.1, 0.2],
                            [0.1, 0.5, 0.4],
                            [0.02, 0.9, 0.08]])

class_targets = [0, 1, 1]

for targ_idx, distribution in zip(class_targets, softmax_outputs):
    print(distribution[targ_idx])
print('\n\n\n')



# with numpy
print(softmax_outputs[[0, 1, 2], class_targets])
print(softmax_outputs[range(len(softmax_outputs)), class_targets])
print(- np.log(softmax_outputs[range(len(softmax_outputs)), class_targets]))

neg_log = - np.log(softmax_outputs[range(len(softmax_outputs)), class_targets])
average_loss = np.mean(neg_log)
print(average_loss)
print('\n\n\n')

class_targets = np.array([[1, 0, 0],
                          [0, 1, 0],
                          [0, 1, 0]])
print(len(class_targets.shape))
# Probabilities for target values only if categorical labels
correct_confidences = 0
if len(class_targets.shape) == 1:
    correct_confidences = softmax_outputs[range(len(softmax_outputs)), class_targets]
    print(correct_confidences)

# Mask values - only for one-hot encoded labels
elif len(class_targets.shape) == 2:
    correct_confidences = np.sum(softmax_outputs * class_targets, axis=1)
    print(correct_confidences)


# Losses
neg_log = - np.log(correct_confidences)
print(neg_log)
average_loss = np.mean(neg_log)
print(average_loss)


# print(- np.log(0))
print(np.e ** (- np.inf))
print(-np.log(1+1e-7))
# y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)


print(np.mean([10, 5, 4, 7, 1, 3]))
print(len(class_targets.shape))
print(correct_confidences)


# class Loss:
#     def calcylate(self, output, y):
#         sample_losses = self.forward(output, y)
#         data_loss = np.mean(sample_losses)
#         return data_loss
#
#
# class Loss_CategoricalCrossentropy(Loss):
#     samples = len(y_pred)
#     y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)
#
#     if len(y_true.shape) == 1:
#         correct_confidences = y_pred_clipped[range(samples), y_true]
#     elif len(y_true.shape) == 1:
#         correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)
#
#     negative_log_likelihoods = - np.log(correct_confidences)
#
#     return negative_log_likelihoods

print(np.exp(0), np.exp(-0.1))



























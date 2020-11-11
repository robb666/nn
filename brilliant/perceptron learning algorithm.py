import numpy as np

x1 = [-1, 1]
x2 = [0, -1]
x3 = [10, 1]

y1 = 1
y2 = -1
y3 = 1

w0 = [0, 0]
b0 = 0


w01 = w0 + np.dot(y1, x1)
b1 = b0 + y1
print(w01)

output1 = sum(w01 * x2) + b1
print(output1)


w02 = w01 + np.dot(y2, x2)
print(w02)
b2 = b1 + y2


output3 = sum(w02 * x3) + b2

print(output3)  # x3

w03 = w02 + y3*x3
print(w03)

b3 = b2 + y3
print(b3)

output1 = np.dot(w03, x1) + b3
print(output1)

w04 = w03 + y1*x1
print(w04)
b4 = b3 + y1
print(b4)

# correctly classified x2 and x3, back to x1

output1 = np.dot(w04, x1) + b4
print(output1)

w05 = w04 + y1*x1
print(w05)
b5 = b4 + y1
print(b5)

output1 = np.dot(w05, x1) + b5
print()
print(w05[0] + w05[1] + b5)





















# for i in x1, x2, x3:
#     y = i
#     print(y)







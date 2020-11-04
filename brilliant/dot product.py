import numpy as np


























x = [1, 4, 3, -1]

def magnitude(x):
    """magnitude of various vectors"""
    return sum(k**2 for k in x)**0.5


# print(magnitude(x))
#
# print(25**0.5)









def integration(x, w, b):
    """Dot product"""
    weighted_sum = sum(x[k] * w[k] for k in range(0, len(x)))
    return weighted_sum + b


w = [3,-1, 1, 2]
x = [1, 4, 3,-1]
b = 0



# print(integration(x, w, b))
#
#
# output = np.dot(w, x)
# print(output)



import matplotlib.pyplot as plt
import numpy as np

# Generate data for a Gaussian distribution
mu, sigma = 0, 1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

# Create the plot
plt.figure(figsize=(10,6))
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.title('Gaussian Distribution (mean = 0, std = 0.1)')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()

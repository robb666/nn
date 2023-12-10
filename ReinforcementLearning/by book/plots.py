import matplotlib.pyplot as plt
import numpy as np

# Generate data for a Gaussian distribution
mu = 0  # mean and standard deviation

# Adjusting the standard deviation to achieve a variance of 1
desired_variance = 1
sigma = np.sqrt(desired_variance)  # Standard deviation is the square root of variance

print(sigma)


samples = np.random.normal(mu, sigma, 1000)
integer_samples_with_variance_1 = np.clip(np.round(samples), 1, 10)


# Plotting the histogram
plt.figure(figsize=(10,6))
plt.hist(integer_samples_with_variance_1, bins=np.arange(1, 12) - 0.5, density=True, rwidth=0.8)
plt.xticks(range(1, 11))
plt.title('Gaussian Distribution with Integer Values (1 to 10) and Variance 1')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
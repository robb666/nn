import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Creating violin plot
plt.violinplot(data)

# Adding titles and labels
plt.title('Example of a Violin Plot')
plt.xlabel('Category')
plt.ylabel('Values')

# Display the plot
plt.show()
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

photo = io.imread('zdj.jpg')
print(photo.shape)

vertical = np.array(photo[:, :, 0].T)

plt.imshow(vertical[:, ::-1])
plt.show()

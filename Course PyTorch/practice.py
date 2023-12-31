import torch

# Example matrices
mat1 = torch.tensor([[[[1, 2],
                       [3, 4],
                       [5, 6]]]])

mat2 = torch.tensor([[5, 6],
                     [7, 8],
                     [9, 9]])



# mat2 = mat2.reshape(2, 3)
print('mat1.shape: ', mat1.shape)
mat1 = mat1.reshape(2, 3)

print('mat1.shape: ', mat1.shape)
print('mat1.ndim: ', mat1.ndim)

print()
print(mat1)

print('mat2.shape: ', mat2.shape)
print('mat2.ndim: ', mat2.ndim)


# Matrix multiplication
result = torch.matmul(mat1, mat2)

print(result)

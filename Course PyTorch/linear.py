import torch
import torch.nn as nn
import numpy
import matplotlib.pyplot as plt
from icecream import ic
from graphviz import Digraph

print(torch.__version__)


class PyParams(nn.Module):
  def __init__(self):
    super().__init__()
    self.weights = nn.Parameter(torch.randn(1,
                                            requires_grad=True,
                                            dtype=torch.float))
    self.bias = nn.Parameter(torch.randn(1,
                                         requires_grad=True,
                                         dtype=torch.float))

  def forward(self, x: torch.Tensor) -> torch.Tensor:
    return self.weights * x + self.bias


if __name__ == '__main__':
  model_0 = PyParams()

  weight = 0.7
  bias = 0.3

  start = 0
  end = 1
  step = 0.02
  X = torch.arange(start, end, step).unsqueeze(dim=1)

  y = weight * X + bias

  train_split = int(0.8 * len(X))
  X_train, y_train = X[:train_split], y[:train_split]
  X_test, y_test = X[train_split:], y[train_split:]

  epochs = 400

  loss_fn = nn.L1Loss()
  optimizer = torch.optim.SGD(params=model_0.parameters(), lr=.01)

  for epoch in range(epochs):
    model_0.train()

    y_preds = model_0(X_train)
    loss = loss_fn(y_preds, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    model_0.eval()

  with torch.inference_mode():
    y_preds = model_0(X_test)


  def plot_predictions(train_data=X_train,
                       train_labels=y_train,
                       test_data=X_test,
                       test_labels=y_test,
                       predictions=None):
    plt.figure(figsize=(10, 7))

    plt.scatter(train_data, train_labels, c="b", s=4, label="Traning data")
    plt.scatter(test_data, test_labels, c="g", s=4, label="Testing data")

    if predictions is not None:
      plt.scatter(test_data, predictions, c="r", s=4, label="Predictions")
    plt.legend(prop={"size": 14})

  plot_predictions(predictions=y_preds)
  plt.savefig('test_linear.png')

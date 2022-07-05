import math
import torch
from torch import nn
from d2l import torch as d2l


weights = torch.ones((2, 10)) * 0.1
values = torch.arange(20.0).reshape((2, 10))
print(weights.unsqueeze(1).shape)

# torch.bmm(weights.unsqueeze(1), values.unsqueeze(-1))

print(weights.squeeze(-1).shape)
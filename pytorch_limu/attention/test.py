import math
import torch
from torch import nn
from d2l import torch as d2l

x=torch.rand(2, 2, 4).shape
print(torch.rand(2, 2, 4).shape)

print(torch.repeat_interleave(torch.tensor([2, 3]), x[2]))
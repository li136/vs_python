import math
import torch
from torch import nn
from d2l import torch as d2l

a=torch.tensor([1.0,2.0,3.0])
b=a.repeat_interleave(3).reshape((-1, 3))
print(b)
c=b - torch.tensor([1.0,2.0,3.0])
print(c)
print(nn.functional.softmax(c,dim=1))
print(torch.matmul(b - torch.tensor([1.0,2.0,3.0]), a))
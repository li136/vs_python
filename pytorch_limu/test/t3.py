import torch
from torch import nn
from d2l import torch as d2l

a=torch.rand(1,2,3)
print(a)
a += nn.Parameter(torch.randn(1, 2,3)).data[:, :2, :]
print(a)

b=torch.tensor([[[1]],[[2]]])
c=b[0,:,:]
print(b.shape)
print(c)
print(c.shape)
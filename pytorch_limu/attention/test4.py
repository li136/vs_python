import math
import torch
from torch import nn
from d2l import torch as d2l

a=torch.ones([2,1,8])
b=torch.ones([2,10,8])
c=a+b
print(c.shape)
# print(c)
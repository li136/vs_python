import math
import torch
from torch import nn
from d2l import torch as d2l

X = torch.ones((2, 1, 4))
Y = torch.ones((2, 4, 6))
# bmm也是矩阵乘法，2是批量
print(torch.bmm(X, Y).shape)
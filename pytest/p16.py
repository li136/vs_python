from torch.nn import functional as F
import math
import torch
from torch import nn
from einops import rearrange,repeat

a= torch.randn(2,2)
print(a)
b = rearrange(a, 'a b -> b a')
print(b)
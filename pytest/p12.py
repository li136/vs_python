# test einops
from einops import rearrange,repeat
import torch
 
a = torch.randn(3, 9, 9)  # [3, 9, 9]
output = rearrange(a, 'c (r p) w -> c r p w', p=3)
print(output.shape)   # [3, 3, 3, 9]


a = torch.randn(9, 9)  # [9, 9]
output_tensor = repeat(a, 'h w -> c h w', c=3)  # [3, 9, 9]
print(output_tensor.shape)
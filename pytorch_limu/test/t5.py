import torch.nn as nn
import torch
@torch.no_grad()
def init_weights(m):
    # print(m)
    if type(m) == nn.Linear:
        m.weight.fill_(1.0)
        print(m.weight)
net = nn.Sequential(nn.Linear(2,4), nn.Linear(4, 8))
print(net)
print('isinstance torch.nn.Module',isinstance(net,torch.nn.Module))
print(' ')
net.apply(init_weights)
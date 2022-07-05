import math
from turtle import forward
import pandas
import torch 
from torch import nn
from d2l import torch as d2l

class ffn(nn.Module):
    def __init__(self, input, hiddens, output,**kwargs):
        super(ffn,self).__init__(**kwargs)
        self.dense1=nn.Linear(input,hiddens)
        self.dense2=nn.Linear(hiddens,output)
        self.relu=nn.ReLU()

    def forward(self,X):
        return self.dense2(self.relu(self.dense1(X)))

class res_LN(nn.Module):
    def __init__(self, norm_shape, dropout, **kwargs):
        super(res_LN,self).__init__(**kwargs)
        self.dropout = nn.Dropout(dropout)
        self.ln = nn.LayerNorm(norm_shape)

    def forward(self, X, Y):
        # print(C)
        # print("---------------")
        return self.ln(self.dropout(Y) + X)

# add_norm = res_LN([3, 4], 0.5)
# add_norm.eval()
# print("--------------------------------")
# print(add_norm(torch.ones((2, 3, 4)), torch.ones((2, 3, 4))).shape)
# print("--------------------------------")
class encoderblock(nn.Module):
    def __init__(self, key, query, value, hiddens, 
                norm_shape, ffn_input,ffn_hiddens,num_heads,
                dropout, use_bias=False, **kwargs):
        super(encoderblock, self).__init__(**kwargs)
        self.attention = d2l.MultiHeadAttention(
            key, query, value, hiddens, num_heads, dropout,use_bias)
        self.resnorm1 = res_LN(norm_shape, dropout)
        self.resnorm2 = res_LN(norm_shape, dropout)
        self.ffn = ffn(ffn_input, ffn_hiddens, hiddens)
    
    def forward(self, X, valid_lens):
        Y = self.resnorm1(X,self.attention(X, X, X, valid_lens))
        return self.resnorm2(Y, self.ffn(Y))

X = torch.ones((2, 100, 24))
valid_lens = torch.tensor([3, 2])
encoder_blk = encoderblock(24, 24, 24, 24, [100, 24], 24, 48, 8, 0.5)
encoder_blk.eval()
print(encoder_blk(X, valid_lens).shape)

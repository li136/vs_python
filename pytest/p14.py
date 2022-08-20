
import torch as t
from torch import nn

if __name__ == '__main__':
    embedding = nn.Embedding(10, 2)  # 10个词，每个词用2维词向量表示
    input = t.arange(0, 6).view(3, 2).long()  # 3个句子，每句子有2个词
    print(input.size())
    a,b = input.size()
    print(b)
    input = t.autograd.Variable(input)
    print(input.size())
    output = embedding(input)
    print(output.size())
    print(embedding.weight.size())
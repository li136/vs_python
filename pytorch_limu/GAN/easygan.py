import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

real_data_num = 1000 #真实数据数量
batch = 64 #每次运算处理多少数据

def make_data(w, b, data_num): 
    """生成 Y = Xw + b + 噪声的实验数据。数据大小data_num*2"""
    X = torch.randn(data_num)
    Y = X*w + b
    Y += torch.normal(0, 1, Y.shape)
    X = X.view(len(X),1)
    Y = Y.view(len(Y),1)
    data = torch.cat((X, Y), dim=1)
    return data

real_data = make_data(w = 3, b = 1, data_num = 1000) #生成真实数据样本

G = nn.Sequential( #定义生成器，
    nn.Linear(2,64),
    nn.ReLU(),
    nn.Linear(64,2)
)
D = nn.Sequential( #定义判别器
    nn.Linear(2,64),
    nn.ReLU(),
    nn.Linear(64,1),
    nn.Sigmoid()
)

optimizer_G = torch.optim.Adam(G.parameters(),lr=0.0001) #定义生成器优化函数
optimizer_D = torch.optim.Adam(D.parameters(),lr=0.0001) #定义判别器优化函数

for step in range(10001): #运算5001次
    
    """更新5次判别器D"""
    for stepp in range(5):
        A = np.arange(1,1000)
        a = np.random.choice(A, 64)
        real_data_sample = real_data[a] #上面三行对真实数据采样

        noise_z =  torch.Tensor(np.random.rand(64,2)) #产生随机向量
        G_make = G(noise_z) #随机向量丢进G生成

        pro_atrist0 = D(real_data_sample)#给真值打分
        pro_atrist1 = D(G_make)#给假值打分

        G_loss = torch.mean(torch.log(1-pro_atrist1))
        D_loss = -torch.mean(torch.log(pro_atrist0)+torch.log(1-pro_atrist1))  

        optimizer_D.zero_grad()
        D_loss.backward( )
        optimizer_D.step()


    """更新1次生成器G"""
    A = np.arange(1,1000)
    a = np.random.choice(A, 64)
    real_data_sample = real_data[a] #上面三行实现对真实数据采样

    noise_z =  torch.Tensor(np.random.rand(64,2)) #产生随机向量
    G_make = G(noise_z) #随机向量丢进G生成

    pro_atrist1 = D(G_make)#给假值打分

    G_loss = torch.mean(torch.log(1-pro_atrist1))

    optimizer_G.zero_grad()
    G_loss.backward(retain_graph=True)

    optimizer_G.step()

    plt.ion()#下面都是输出画图使的
    if step % 2000 == 0:
        noise_z =  torch.Tensor(np.random.rand(1000,2))
        G_make = G(noise_z)
        A = G_make.detach().numpy()
        plt.scatter(A[:,0], A[:,1], 10, label= step )
        plt.legend(loc='upper left')
        plt.pause(0.1)
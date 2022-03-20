import torch

x = torch.arange(12)
print(x)

print(x.shape)

print(x.numel())

X=x.reshape(3,4)
print(X)

print(torch.ones(2,3,4))
print(torch.randn(3,4))

# todo tensor
print("---------------------------")
x=torch.tensor([1.0,2,4,8])
y=torch.tensor([2,2,2,2])
print(x+y)
# torch.arange
# torch.cat
X = torch.arange(12, dtype=torch.float32).reshape((3,4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(torch.cat((X, Y), dim=0),"\n", torch.cat((X, Y), dim=1))

print(X==Y)

a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))
print(a+b)

# todo [-1]选择最后一个元素，可以用[1:3-Net]选择第二个和第三个元素：
print(X[-1],"\n", X[1:3])

X[1, 2] = 9
print(X)

A = X.numpy()
B = torch.tensor(A)
print(type(A), "\n", type(B))
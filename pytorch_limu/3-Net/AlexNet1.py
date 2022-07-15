import torch
from torch import nn
from d2l import torch as d2l
import torchvision
from torchvision import transforms
import torch.utils.data as data

net = nn.Sequential(
    nn.Conv2d(1, 96, kernel_size=7, padding=3), nn.ReLU(),
    nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
    nn.Conv2d(96, 256, kernel_size=3, padding=1), nn.ReLU(),
    nn.Conv2d(256, 256, kernel_size=3, padding=1), nn.ReLU(),
    nn.Conv2d(256, 128, kernel_size=3, padding=1), nn.ReLU(),
    nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
    nn.Flatten(),
    nn.Linear(6272, 4096), nn.ReLU(),
    nn.Dropout(p=0.5),
    nn.Linear(4096, 4096), nn.ReLU(),
    nn.Dropout(p=0.5),
    nn.Linear(4096, 10))

# X = torch.randn(1, 1, 28, 28)
# for layer in net:
#     X=layer(X)
#     print(layer.__class__.__name__,'output shape:\t',X.shape)

batch_size = 128


trans = [transforms.ToTensor()]
trans.insert(0, transforms.Resize(28))
trans = transforms.Compose(trans)
mnist_train = torchvision.datasets.FashionMNIST(
    root="../data", train=True, transform=trans, download=True)
mnist_test = torchvision.datasets.FashionMNIST(
    root="../data", train=False, transform=trans, download=True)
train_iter = data.DataLoader(mnist_train, batch_size, shuffle=True,
                        num_workers=d2l.get_dataloader_workers())
test_iter = data.DataLoader(mnist_test, batch_size, shuffle=False,
                        num_workers=d2l.get_dataloader_workers())

lr, num_epochs = 0.01, 10
d2l.train_ch6(net, train_iter, test_iter, num_epochs, lr, d2l.try_gpu())
d2l.plt.show()
import numpy as np

x1 = np.ones((3,1))
w = np.ones((4,3))

z1 = np.matmul(w,x1)
print(z1)

x2 = np.ones((5,3,1))
z2 = np.matmul(x2.squeeze(2),w.T)
print(z2)
print(z2.shape)
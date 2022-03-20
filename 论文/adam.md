## 特点
- RMSProp、AdaGrad、Momentum
- ![公式](https://upload-images.jianshu.io/upload_images/10046814-59e992b67938aec9.png?imageMogr2/auto-orient/strip|imageView2/2/format/webp)
- RMSProp算法，加权均值，调整v和m
## 知识点
- Momentum将梯度作为加速度，使过去梯度信息也会影响现在的学习率，详见mt
- AdaGrad使用梯度平方累加的方法，计算每个参数过去调整的值的平方的总和。总和越大的参数就少动点。见公式中的vt
- RMSporp使用加权均值，调整vt和mt的值，慢慢遗忘过去的梯度信息
- ![avatar](img/IMG_20220622_155045.jpg)
- ![avatar](img/IMG_20220622_155052.jpg)
## 疑问
- 
- 
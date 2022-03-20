## 特点
- 对每层的输入做一个reference, 学习形成残差函数， 而不是学习一些没有reference的函数。这种残差函数更容易优化，能使网络层数大大加深。  
残差函数理解为残差网络更贴切一点
- 残差网络（Residual Network）是一种非常有效的缓解梯度消失问题网络，极大的提高了可以有效训练的网络的深度。

## 知识点
- 随着网络深度的增加，精度会饱和，然后迅速退化。
-  对于深度神经网络，如果我们能将新添加的层训练成恒等映射（identity function），新模型和原模型将同样有效。 同时，由于新模型可能得出更优的解来拟合训练数据集，因此添加层似乎更容易降低训练误差。  
后半句不能理解
- 使用1*1卷积减少通道数，再卷积，再用1*1卷积增加通道数
- shortcut connections
-     if F has only a single layer,is similar to a linear layer: y = W1x + x   
-     Let us consider H(x) as an underlying mapping to be fit by a few stacked layers (not necessarily the entire net),with x denoting the inputs to the first of these layers. If one hypothesizes that multiple nonlinear layers can asymptotically approximate complicated functions^2, then it is equivalent to hypothesize that they can asymptotically approximate the residual functions, i.e., H(x) − x (assuming that the input and output are of the same dimensions). So rather than expect stacked layers to approximate H(x), we explicitly let these layers approximate a residual function F(x) := H(x) − x. The original function thus becomes F(x)+x. Although both forms should be able to asymptotically approximate the desired functions (as hypothesized),the ease of learning might be different.     残差原理，不翻译直接看原文
-     We argue that this optimization difficulty is unlikely to be caused by vanishing gradients. These plain networks are trained with BN [16], which ensures forward propagated signals to have non-zero variances. We also verify that the backward propagated gradients exhibit healthy norms with BN. So neither forward nor backward signals vanish. In fact, the 34-layer plain net is still able to achieve competitive accuracy (Table 3), suggesting that the solver works to some extent. We conjecture that the deep plain nets may have exponentially low convergence rates, which impact the reducing of the training error3. The reason for such optimization difficulties will be studied in the future. 作者认为网络退化不是梯度消失的问题，但现在还是会认为是resnet梯度保持的比较好

## 疑问
- 为什么深的网络会退化？？？？？？地图太大迷路了吗？？？  
因为梯度消失梯度爆炸不能被完美解决？
-     If the optimal function is closer to an identity mapping than to a zero mapping, it should be easier for the solver to find the perturbations with reference to an identity mapping, than to learn the function as a new one.We show by experiments (Fig. 7) that the learned residual functions in general have small responses, suggesting that identity mappings provide reasonable preconditioning.
- resnet网络模型和我先训练一个浅层模型，多次加新的层（不改变已训练好的浅层参数）重新训练，以及加新层（旧参数仅作为初始参数）全部重新训练。在结果上有什么差别
- 感觉残差不贴切模型原意
- identity mappings，恒等映射，在一个浅层网络基础上叠加y=x的层
- F(x) = H(x) - x  
F(x)、H(x)、F(x)是啥？  
H(x)是原始网络、F(x)是残差网络、x是上一层的输入
- 深度增加，训练速度为什么会比VGG快。因为全是卷积吗？
- auxiliary classifiers
- “inception” layer

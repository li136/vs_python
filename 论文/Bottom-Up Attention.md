- 将 top-down attention 和 bottom-up attention 结合
- 通过 Faster RCNN（backbone：ResNet-101) 来产生这样的视觉特征 V，将Faster RCNN检测的结果经过非最大抑制和分类得分阈值选出一些显著图像区域
- 记输入的图片为P，那么图片理解和 VQA 模型的输入都是一个大小为k的V集合{k1~kv}。每个 image feature 编码了一个显著图像区域。每一个框能对应一个类别。将vi和从 ground truth object class 学习到的一个 embedding 结合在一起，然后将它们送入额外的一个属性 softmax 分类器，以此来获得区域对应的属性。
- in captioning and VQA we utilize only the feature vectors – not the predicted labels.
- select all regions where any class detection probability exceeds a confidence threshold. 

- image caption

    第一个LSTM层描述为top-down视觉注意模型，将第二个LSTM层描述为语言模型。Attention LSTM的输入由Language LSTM的前一次输出、平均池化特征以及之前生成的单词的编码组成
    给定Attention LSTM的输出在每一个时间步t为k个图像特征的每一个特征vi生成一个归一化注意力权重。利用用于Language LSTM 输入的attended图像特征计算所有输入特征的凸组合

    Language LSTM的输入包括attended图像特征和Attention LSTM的输出

    ![1](https://img-blog.csdnimg.cn/20210712222304131.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjcwNzMyNg==,size_16,color_FFFFFF,t_70#pic_center)
- image caption

    首先对问题进行编码，作为GRU（gated recurrent unit）的隐藏状态q，每个输入单词用一个学习过的单词嵌入来表示，给定GRU的输出q，我们为k个图像特征中的每一个vi生成非标准化的注意力权重

![2](https://img-blog.csdnimg.cn/20210712225103548.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjcwNzMyNg==,size_16,color_FFFFFF,t_70#pic_center)
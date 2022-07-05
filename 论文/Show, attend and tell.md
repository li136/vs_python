## 特点
- 用cnn作为encoder，用attention和LSTM作为decoder
- 图像转文字
## 知识点
- 输入图像I II归一化到224 × 224 224\times 224224×224    
使用现成的VGG网络部分架构，输出为conv5_3层的14×14×512维特征。  
用attention
再通过一层全连接层作为transformer作为LSTM的第一个hidden state，再用LSTM得到输出句子y
- 
## 疑问
- 
- 
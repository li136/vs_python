## 特点
- Self-Attention是 Transformer 的重点
- 纯基于注意力
- 使用编码器-解码器架构处理序列对
## 知识点
- 多头注意力：对同样的key，value，query，抽取不同的信息。  
例如短距离关系和长距离关系  
使用h个独立的注意力池化，然后合并输出得到最终输出  
- 位置编码Positional Encoding，添加位置信息，因为attention会破坏忽略原来的位置信息
- encoding的input embedding后要除num_hiddens根号，再加上位置编码Positional Encoding
- 层归一化
- 基于位置的前馈网络
- 编码器的输出y1-yn作为解码器中第i个tramsformer块中的key和value。query来自目标序列
## 疑问
![transformer块](https://pic4.zhimg.com/v2-f6380627207ff4d1e72addfafeaff0bb_r.jpg)
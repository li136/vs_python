# Counterfactual VQA: A Cause-Effect Look at Language Bias
```bash
提供了分析先验语言知识的方法
可以在VQA模型中减少language bias的影响
提供新的思路：基于因果关系的分析方法
```
```bash
VQA模型的回答过程很有可能并不依赖于视觉和语言的混合推理，而是依赖于语言的相关性。举个例子，在VQA数据集中，和运动相关的问题仅仅回答‘tennis’的准确率为40%，以‘Did you see ... ’ 开头的问题光是回答‘yes’就可以达到90%的准确率。这是很不合理的，因为学习到过多的这种语言间的相关性会导致模型无法推广，当前的一大挑战是如何在有偏训练下进行无偏推理。
```
```bash
模型的主要思想就是从混合模态对答案的所有影响中，取出语言对答案的直接影响，保留视觉和语言对答案的混合影响，也就是说将language bias看作问题对答案的直接因果效应，从总因果效应中减去language的直接因果效应从而减少bias的影响。
```
![1](https://pic3.zhimg.com/v2-8d0142700cb901951bf1a77536dbe9b2_r.jpg)
```bash
这里有一个生动的例子来反映Figure1的过程，在Figure2中，假设有一个问题：这个香蕉的颜色是什么，训练集中的大部分的答案都是黄色。左边的是传统的VQA模型，右边的是本文介绍CF-VQA模型。左边的传统模型既有语言和视觉的单独影响也有混合推理的影响（这两部分的总和成为total effect），但是因为数据集的原因，语言的推理占比比较大，最终覆盖了图片的推理贡献，给出了‘yellow’这个答案。

但是右边的CF-VQA模型不同，它不光进行了传统VQA的推理，也进行了只有语言的推理，通过tota effect减去language effect去除了语言相关性对答案的影响，给出了正确答案green

语言先验包括“坏”的语言偏见（例如，将香蕉的颜色与主色“黄色”结合起来）和“好”的语言语境（例如，根据问题类型“什么颜色”缩小答案空间）。简单地排除额外的分支无法利用良好的上下文。
```
```bash
Debiasing Strategies in VQA：

strengthening visual grounding, weakening language prior, and implicit/explicit data argumentation.
```
![1](img\CFVQA.png)
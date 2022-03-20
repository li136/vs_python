## RCNN
- 先用CNN对整个原始图片抽取特征，再使用Rol池化层对每个锚框产生固定长度的特征。再加全连接，做预测。

## Faster RCNN
- 用启发式搜索获得更好的锚框
## Mask RCNN
- 在faster rcnn做完Rol后，如果数据集有像素级别的标号，用fcn利用这些信息
- 
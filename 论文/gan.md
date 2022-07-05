## 特点
- 两个网络对抗，进步
- 
## 知识点
- 生成器用随机噪音生成虚假的结果。  
判别器对虚假结果和真实结果做预测  
- 使用adam做优化
- 生成器loss：log(1-pro_atrist1)  
判别器loss： - (log(pro_atrist0)+log(1-pro_atrist1))  
pro_atrist0为判别器对真实结果的打分结果，pro_atrist1为判别器对虚假结果的打分结果  
## 疑问
- 
- 
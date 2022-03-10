import json

# 异常
try:
    print(5/0)
except ZeroDivisionError:
    print("Zero")
else:
    print("没问题")

# json存数据
number = [1,2,3,4,5]
file='number.json'
with open(file,'w') as f:
    json.dump(number,f)
# json读数据
with open(file) as f:
    numbers=json.load(f)
print(numbers)
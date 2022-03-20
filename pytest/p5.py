cars=['qwe','asd','zxc']
for car in cars:
    if car == 'qwe':
        print(car.upper())
    else:
        print(car)

# and和or
q1=1
q2=2
if q1==1 and q2==2:
    print('ok1')
if q1==1 or q2==1:
    print('ok2')

# in和not in
if 'qwe' in cars:
    print('ok3')
if 'ewq' not in cars:
    print('ok4')
print(q1==1)


# if-elif-else
if q1==2:
    print('q1')
elif q2==1:
    print('q2')
else:
    print('q3')

if cars:
    print('数组非空')
else:
    print('数组为空')

# 两个数组
carss=['qwe','asd','cxz']
for car in cars:
    if car in carss:
        print(car)
    else:
        print('carss数组中无该元素')


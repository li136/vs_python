# from p8_3 import user2
# user2()

# 效果同上
import p8_3 as p
p.user2()


# 传递任意数量的实参
def user(*qwe):
    for q in qwe:
        print(q)
    print(qwe)

# 用字典接受任意关键字实参
def user1(f,**qwe):
    qwe['t']=f
    return qwe

user('asd')
user('asd','zxc')

qwe=user1('qwe',asd=1,zxc=2)
print(f"\n{qwe}")
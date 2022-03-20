def user():
    print("hello world")

def user1(m):
    print(f"hello {m}")

def user2(m1,m2):
    print(f"hello {m1} and {m2}")
# 默认值
def user3(m1='zxc',m2='cxz'):
    print(f"hello {m1} and {m2}")

def user4(m1='qwe',m2='asd'):
    return m1

# 返回字典,同理也可传递列表
def user5(m1='qwe',m2='asd'):
    return {'qwe':m1,'asd':m2}

# 函数可修改列表
def user6(m1):
    m1.append(21)

user()
user1('qwe')
user2('qwe','asd')

# 指定参数
user2(m2='qwe',m1='asd')

user3()

print(user4())
print(user4(2))

print(f"\n{user5(1,2)}")

m2=['qwe','qwe']
user6(m2)
print(m2)

#这样就不会影响列表了，传递的是列表副本
user6(m2[:])
print(m2)
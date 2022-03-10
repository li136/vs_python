# 列表
bic=['q3','q2','q1']
print(bic)

# 类似数组
print(bic[0])
print(bic[-1])

# 内置各类函数
bic.sort()
print(bic)
bic.reverse()
print(bic)
bic.reverse()
bic[0]='qwe'
print(bic)

bic.append('q4')
bic.insert(1,'q1')
print(bic)


del bic[2]
print(bic)


ans=bic.pop()
print(bic)
print(ans)


ans=bic.pop(0)
print(bic)
print(ans)

bic.remove('q3')
print(bic)
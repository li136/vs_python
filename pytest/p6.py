from re import A


alien={'qwe':'qwe','asd':5}
print(alien['asd'])
print(alien['qwe'])

# 字典内容可动态添加，改变，删除
alien['zxc']='cxz'
print(alien['zxc'])

alien['asd'] += 3
print(alien['asd'])

del alien['zxc']
if ('zxc' not in alien):
    print('ok\n')
print(alien.get('qwe','没有qwe'))
print(alien.get('asd','没有asd'))
print(alien.get('zxc','没有zxc\n'))

# 遍历字典
for key,value in alien.items():
    print(f"Key={key}  Value={value}")

# 集合
car={'qwe','asd','zxc','zxc'}
print(car)
print('\n')

# 嵌套字典
aliens=[]
for t in range(5):
    newalien={'color':'yellow','point':5}
    aliens.append(newalien)
for a in aliens:
    print(a)

# 同理，可在字典中放字典、在字典中放列表
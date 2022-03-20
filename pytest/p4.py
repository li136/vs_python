bic=['q3','q2','q1']

for b in bic:
    print(b)
    print(b.title())

print()

# 到5停止
for value in range(1,5):
    print(value)

print()

val=[1,2,3,4,5]
print(max(val))
print(min(val))
print(sum(val))

print()

squ=[v*2 for v in range(1,5)]
print(squ)
print(squ[0:2])
print(squ[2:])
for qwe in squ[:3]:
    print(qwe)

print()

#  元组
s=(1,2,3)
print(s)
print(s[1])
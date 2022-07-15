class A():
    qwe=1

a=A()
setattr(a, "qwe", 28)
print(a.qwe)
setattr(a, "asd", 12)
print(a.asd)
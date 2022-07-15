class A():
    q1=12
    q2='qwe'

a=A()
b=1
for t in dir(a):
    if not t.startswith('_'):
        print(t)
        if isinstance(getattr(a,t),type(b)):
            print(getattr(a, t))
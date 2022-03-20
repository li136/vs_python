class Dog:
    def __init__(q,w=2,e=3):
        q.w=w
        q.e=e
    
    def sit(q):
        print(f"{q.w} ok")

    def over(q):
        print(q.e)

qwe=Dog('asd',12)
qwe1=Dog()

qwe.sit()
qwe.over()
    
print(qwe.w)

qwe1.sit()

# 子类继承
class g(Dog):
    def __init__(q, w=2, e=3, r=4):
        super().__init__(w, e)
        q.r=r
    def getq(q):
        print(f"g have {q.w} and {q.e} and {q.r}")
    # 重写父类的方法
    def sit(q):
        print("重写")
        return super().sit()

g1=g()
g1.getq()
g1.sit()



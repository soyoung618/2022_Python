class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("객체가 생성되었습니다")
    def print_info(self):
        print("*"*20)
        print("이름:",self.name)
        print("나이:",self.age) 
        print("*"*20)    
        print()

p1=Person('홍길동',20)
p1.print_info()

p2=Person('강김찬',40)
p2.print_info()


p3=Person('을지문덕',30)
p3.print_info()


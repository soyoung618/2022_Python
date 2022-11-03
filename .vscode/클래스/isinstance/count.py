from tkinter.font import names


class Person:
    #클래스 변수
    count_class_var=0

    #생성자
    def __int__(self,name,age,power):
        self.name=name
        self.age=age
        self.power=power
        self.increase_obi()

    def increase_obi(self):
        Person.count_class_var +=1

print("현재까지 생성된 인스턴스 객체의 객수:",Person.count_class_var)
p1=Person("홍길동",20,62)
print("현재까지 생성된 인스턴스 객체의 객수:",Person.count_class_var)
p2=Person("파이썬",28,22)
print("현재까지 생성된 인스턴스 객체의 객수:",Person.count_class_var)


class Person:
    pass
class Monster:
    pass

p1=Person()
result=isinstance(p1,Person)
print("[1] p1 인스턴스는 Person 클래스의 인스턴스 객체가 맞나요? ..>",result)
print("[1] p1 인스턴스는 Person 클래스의 인스턴스 객체가 맞나요? ..>",isinstance(p1,Person))

result2=isinstance(p1,Monster)
print("[2] p1 인스턴스는 Monster 클래스의 인스턴스 객체가 맞나요? ..>",result2)
print("[2] p1 인스턴스는 Monster 클래스의 인스턴스 객체가 맞나요? ..>",isinstance(p1,Monster))
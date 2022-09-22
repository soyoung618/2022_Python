 #for 변수 in range() 함수 :문장 1
from imghdr import what
from logging.config import valid_ident
from multiprocessing.sharedctypes import Value
import xdrlib


for x in range(3,9,2):
    print(x, end=" ")

#기본적인 for문의 예 - 응용
lst=["apple",100,3.14]
for item in lst:
    print(item, type(item))

print()

d={"apple":100,"arange":200, "banana":300}
for k,v in d.items():
    print(k,v)

print()

#a를 이용해서 다음과 가팅 출력되도록 프로그램을 작성하시오
a=[(1,2),(3,4,),(5,6)]
for (first1,last2) in a:
    print(first1 + last2)

print()

#다음과 같이 별을 찍는 프로그램을 작성하시오

for i in range(10):
    for j in range(i+1):
        print('*',end=" ")
    print('')

print()

#정답
for i in range(1,11):
    print("*"*i)

print()

#구구단을 출력하는 프로그램을 작성하시오
for x in range(2,5+1): 
    for y in range(1,9+1):
        print("{} x {} = {}".format(x,y,x*y))

print()

#for문을 이용하여 별찍기
for i in range(1,11,2):
    print('{:^10}'.format("*" * i))

#정답
for i in range(1,6):
    print(' '*(5-i),'*'*(2* i-1))

print()

#리스트 안의 리스트 요소를 출력할 때도 중첩 반복문을 사용한다
table=[["월","화","수"],[100,200,300]]
for row in table:
    for col in row:
        print(str(col)+" ")
    print()

#break, continue 문
for i in range(1,9+1):
    if i==7:
        break
    print("2 x {} = {}".format(i,2*i))

for i in range(1,9+1):
    if i% 2 ==0:
        continue
    print("2 x {} = {}".format(i,2*i))

print()

lst=[1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item > 5: break
    print("itme:{0}".format(item))
    
lst=[1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item > 5: continue
    print("itme:{0}".format(item))

print()

#리스트 컴프리헨션
array = []
for i in range(1,10,2):
    array.append(i*i)
print(array)
array = [i*i for i in range(1,10,2)]
print(array)
array = [i*i for ri in range(1,10,3) if i*i>30]
print(array)

print()

#기본적인 while문
value = 5
while value > 0:
    print(Value)
    value-=1

print()

x=3
while x<6:
    print(x)
    x+=1 #없으면 무한반복

print()

#echo = input()
#while echo !="exit":
#    print(echo)
#    echo=input()

#print()

#echo = input()
#while True:
#    if echo =="exit":
#        break
#   print(echo)
#   echo=input()

#print()

#range() 
#규칙이 있는 수열을 생성한다
#시작값과 종료값, 증가 감소 스텝을 지정하면 수열을 생성한다.
print(list(range(10)))
print(list(range(5,10)))
print(list(range(10,0,-1)))
print(list(range(10,20,2)))

print()

#리스트 함축(comprehension)
lst=[1,2,3,4,5]
print(lst)
ls=[i**2 for i in lst]
print(lst)

print()

test=("apple","banana","orange")
test_len=[len(i) for i in test]
print(test_len)

print()

d={100:"apple", 200:"banana", 300:"orange"}
d_upper=[v.upper() for v in d.values()]
print(d_upper)

print()

#반복문 작성 시 도움이 되는 함수
#형식) filter(<function> | None, <이터레이션이 가능한 자료형>)
lst=[10,25,30]
itel=filter(None,lst)
for item in itel:
    print("item : {0}".format(item))

print()

def getBiggerThan10(i):
    return i>20
lst=[10,25,30]
itel=filter(getBiggerThan10,lst)
for item in itel:
    print("item : {0}".format(item))

print()

#입력받은 양의 정수가 3의 배수, 5의 배수, 혹은 8의 배수인지를 알려주는 프로그램으로 설계하고 작성하라. 양의 정수가 3의 배수이면 3의 배수 이다 라고 출력하고 5의 배수이면
#5의 배수이다를 출력하고 8의 배수이면 8의 배수이다를 출력하라. 그 외의 경우이면 어느 배수도 아니다를 출력해라.

x= int(input())
if x%3==0:
    print("{0}는 3의 배수".format(x))
elif x%5==0:
    print("{0}는 5의 배수".format(x))  
elif x%8==0:
    print("{0}는 8의 배수".format(x))  
else:
    print("{0}는 어느 배수도 아니다".format(x))









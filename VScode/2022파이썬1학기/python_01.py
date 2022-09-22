from ctypes import c_longdouble
from gc import collect
import keyword
import sys
from tkinter import E
from turtle import color
print('Python start!')
print("Python start!")
print("""Python start!""")
print('''Python start!''')

print()

print('p', 'y', 't', 'h', 'o', 'n', sep='')
print('010', '7777', '7777', sep='-')
print('python', 'google.com', sep='@')

print()

print('Welcome To', end='    ')
print('IT News', end='')
print('web site')

print()

print("learn Python", file=sys.stdout)

# 숫자형

print(8+5)
age = 18
print(age)

after_2 = 2
print(age+after_2)
result = age-after_2
print(result)

print()
age = 18
print(age)
age += 2
print(age)
age -= 1
print(age)
age *= 2
print(age)
age /= 2
print(age)
age //= 2
print(age)
age %= 6
print(age)
age **= 3
print(age)

print()
age = 18
print(type(age))
pi = 2.14
print(type(pi))
age /= 2  # 9.0
print(type(age))
x = 10+3.14  # 13.14
print(type(x))

print()
print(0b110111000)  # 2진수
print(type(0b110111000))
print(0o130)  # 8진수
print(type(0o130))
print(0xD7A)  # 16진수
print(type(0xD7A))

print()
print(10e3)
print(type(10e3))
print(1.23456E2)
print(type(1.23456E2))
print(1.23456e-2)
print(1.23456e22)

print()
print(8+24j)  # 실수:8, 허수:24인 복소수
c = 1.2+3.4J  # 실수:1.2. 허수:3.4인 복소수
print(type(1.2+3.4j))
print(c.real)
print(c.conjugate())  # 컬레 복소수를 구하는 함수
d = 1j
print(d*d.conjugate())

print()
print(int(12.7))
print(int('321'))
print(float(456))
print(float('65.4'))
print(float('123e4'))
print(complex(1.23))
print(complex('1.23+45.6j'))
print(str(1.23))

print("***************************************")
# 문자형
print()
greeting = 'Hello'
to = "wold!"
print(greeting)
print(type(greeting))
say_hello = greeting + ","+to
print(say_hello)
print("Hello*5")
print("\"Hello\"\n"+to)
multilne = """Happy
programming"""
print(multilne)
# 문자열 인덱싱과 슬라이싱
s = "Life is too short."
print(s[3])
print(s[11])
print(s[-1])
print(s[-7])
print(s[-18])

s = "Life is too short, you need python."
print(s[3:7])  # 인덱스 3부터 인덱스 7번 바로 앞(6) 바로 앞까지
print(s[-10:-7])  # 인데스 -10번부터 인덱스 -7번 바로 앞까지
print(s[3:-10])     #
print(s[-10:30])    #
print(s[3:2])       #
print(s[30])  # 인덱스 30번부터 맨 뒤까지
print(s[-7])  # 인덱스 -7번부터 맨 뒤까지
print(s[:4])  # 맨 알부터 인덱스 4번 바로 앞까지
print(s[-17])       #
print(s[:])  # 맨 앞부토 맨 뒤까지. 즉 문자열 전체

# 문자열 함수
h = "  Happy programming!"
print(len(h))  # 글자 수 세기
print(h.count("p"))  # h 문자열에서 인자 'p'의 개수 세기
print(h.upper())  # 모두 대문자로 변환하기
print(h.lower())  # 모두 소문자로 변환하기
print(h.strip())  # 왼쪽, 오른쪽 모두 공백 없애기
print(h.replace("Happy", "Funny"))  # 문자열 대체하기
print(h.find("ap"))  # h 문자열에서 인자 'ap'를 왼쪽부터 찾기
print(h.rfind("a"))  # h 문자열에서 인자 'a'를 오른쪽부터 찾기
print(h.find("zoo"))  # 찾기 못하면 -1 리턴

h = "    Happy programming!"
print("a" in h)  # h 문자열에 'a'가 있는지 확인
print("amp" in h)  # h 문자열에 'amp'가 있는지 확인
x = "01::23::ab::&&"
y = x.split("::")  # x 문자열을 '::'로 나누어 리스트 만들기
print(y)
print(", ".join(y))  # y 리스트를 ', '로 이어서 문자열 만들기

# format:문자열 형식을 미리 정하고, 인자를 주어 문자열을 완성한다.

s = "name: {}, number: {},soccer: {}"
s.format("Ronaldo", 7, True)
print("name: {name}, number: {num}".format(name="jordan", num=23))

# 정수를 표현하는 여러 가지 방법
print("{:d}".format(515))  # 정수를 넣는다
print("{:5d}".format(515))  # 최소 5칸을 차지하고 정수를 넣는다
print("{:+5d}".format(515))     # 양수면 +를 표시한다
print("{:=+5d}".format(515))  # +을 맨 앞에 표시한다
print("{:05d}".format(515))  # 빈칸은 0으로 채운다
print("{:+05d}".format(515))  # 양수면 0 앞에 +를 표시한다

# 실수를 표현하는 여러 가지 방법
print("{:f}".format(11.17))  # 실수를 넣는다
print("{:12f}".format(11.17))  # 최소 12칸을 차지하고 실수를 넣는다
print("{:12.1f}".format(11.17))  # 소수점 1자리까지 반올림해서 나타낸다

# 혼자 해 보기
print("{:=+6.1f}".format(11.17))

# 예제)2*3=6
a = 2
b = 3
s = '구구단{0}x{1} = {2}'.format(a, b, a*b)
print(s)
# 클래스 밖 = 함수
# 클래스 안 = 메서드

# 직업 대입하기
s1 = 'name : {0}'.format('soyoung')
print(s1)
# 변수로 대입하기
sge = 55
s2 = 'age : {0}'.format(age)
print(s2)
# 이름으로 대입하기
s3 = 'number : {num}, genden : {gen}'.format(num=1234, gen=567)
print(s3)
# 인덱스를 입력하지 않으면? 순서대로 들어감
s4 = 'name:{},city:{}'.format('BlockDMask', 'seoul')
print(s4)
# 인덱스 순서를 바꾸면, 인덱스 순사가 바뀌여도 번호가 있기 때문에 번호에 맞는 인자 값이 들어가게 된다
s5 = 'songl:{1},song2:{0}'.format('인덱스1', '인덱스2')
print(s5)
# 인덱스를 중복해서 입력하면, 또 들어간다
s6 = 'test1:{0},test2{1}, test3: {0}'.format('인덱스0', '인덱스1')
print(s6)
# format 함수 사용시 중괄호가 나오게 하려면?
# 중괄호 출력, 출력할 값을 중괄호 겹쳐서 출력 할려면 중괄호를 세개로 겹치면 된다.
s7 = 'Format example. {{}},{}'.format('test')
print(s7)
# 중괄호 겹쳐진 인자값
s8 = 'This is value {{{0}}}'.format(1212)
print(s8)
# 문자열 정렬하기
# 왼쪽정렬
s9 = 'this is {0:<10} | done {1:<5} |'.format('left', 'a')
print(s9)
# 오른쪽정렬
s10 = 'this is {0:>10} | done {1:>5} |'.format('right', 'a')
print(s10)
# 가운데 정렬
s11 = 'this is {0:^10} | done {1:^5} |'.format('center', 'a')
print(s11)
# 왼쪽 <, 오른쪽 >, 가운데 ^ 사용
# 문자열에 공백이 아닌 값 채우기
# 왼쪽 정렬
s12 = 'this is {0:-<10} | done {1:o<5} |'.format('left', 'a')
print(s12)
# 오른쪽정렬
s13 = 'this is {0:+>10} | done {1:0>5} |'.format('right', 'b')
print(s13)
# 가운데 정렬
s14 = 'this is {0:.^10} | done {1:@^5} |'.format('center', 'c')
print(s14)
# 자리수와 소수점 표현하기
# 정수 N자리, 0Nd, 정수를 표현할때 특수문자 x
s15 = '정수 3자리 : {0:03d}, {1:03d}'.format(12345, 12)
print(s15)
# 소수점 N자리,0.Nf
s16 = '아래 2자리 : {0:0.2f}, 아래 5자리 {1:0.5f}'.format(123.1234567, 3.14)
print(s16)

# 구구단 프로그램
a = 1
b = 2
# s = '구구단 : {0}x{1} = {2}'.format(a, b, a*b)
for a in range(2, 10):
    print('{0}단'.format(a))
    for b in range(1, 10):
        print('{0}x{1} = {2:2}'.format(a, b, a*b))  # {2:2} 수 자릿수

# %서식문자
num = 10
s = 'my age %d' % num
print(s)

# 문자열 , 정수, 실수를 %로 포매팅 해보기
# %기호 문자 출력
names = ['Kim', 'park', 'lee']
for name in names:
    print('my name is %s' % name)

# % 기호 정수 출력
money = 1000
s2 = 'give me %d won' % money
print(s2)
# % 기호 실수 출력
d = 3.141592
print('value %f' % d)

# 포매팅 해야할 변수 값이 두개 이상일때는 ()를 이용한다
s1 = 'my name is  %s.age : %d' % ('mirim', 100)
print(s1)
# 출력해야할 값이 점점 많아 질수록
age = 78
money = 20000
name = 'Jang'
weight = 63.12
etc = 'abcde'
s2 = 'my name is %s, age:%d, weight:%f, money:%d, etc:%s' % (
    name, age, weight, money, etc)
print(s2)

# string fotmatting
# 변해야 하는 값이 있는 위치를 포매팅 할 위치로 잡아서 실행
month = 1
while month <= 12:
    print(f'2020년 {month}월')
    month = month + 1

# f-sting
# 문자열 맨 앞에 f를 붙이고, 출력할 변수, 값을 중괄호 안에 넣는다
s = 'coffee'
n = 5
result = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'
print(result)

# f-string과 왼쪽 정렬, 오른쪽 정렬, 가운데 정렬
# 왼쪽 정렬
s1 = 'left'
result1 = f'|{s1:<10}|'
print(result1)
# 가운데 정렬
s2 = 'mid'
result2 = f'|{s2:^10}|'
print(result2)
# 오르쪽 정렬
s3 = 'right'
result3 = f'|{s3:>10}|'
print(result3)

# f-string 에서 중괄호 출력 방법
# f-struing 중괄호 출력
num = 10
result = f'my age {{ {num} }},{{num}}'
print(result)

# f-string과 딕셔너리
d = {'name': 'Mirim', 'gender': 'female', 'age': 18}
result = f'my name {d["name"]} ,gender {d["gender"]} ,age {d["age"]}'
print(result)

# f-string 과 리스트
n = [100, 200, 300]
print(f'list : {n[0]}, {n[1]}, {n[2]}')
for v in n:
    print(f'list with for : {v}')

strB = '파이썬 연습'
print(len(strB))

# 변수와 함수
strA = "Hello pythin"
x = 5
y = 3.14
print(type(strA))
print(type(x))
print(type(y))

# 키워드
print(keyword.kwlist)

# 문자열
print("py""thon")
print("py"+"thon")
print("py"*3)

# 문자열 인덱싱
strA = "python"
print(strA[0])

# 문자열 슬라이싱
strA = "python"
print(strA[0:1])
print(strA[1:3])
print(strA[:2])
print(strA[-2:1])  # -2로시작해서 1을 못만남=>공백
print(strA[:])

# 문저욜 인덱싱과 슬라이싱
strB = "python is powerful"
print(strB[0])
print(strB[0:6])
print(strB[:6])

strB = "python is powerful"
print(strB[-1])
print(strB[-2])
print(strB[-3:])

strB = "python is powerful"
print(strB[7:18])
print(strB[:])
print(strB[::2])
print(strB[-11:-9])
print(strB[-18:-12])

# 리스트
colors = ["red", "green", "blue"]
print(colors)
print(type(colors))

# append() 함수
print(colors)
colors.append("blue")
print(colors)

# insert()함수
print(colors)
colors.insert(1, "block")
print(colors)

# index()메서드
print(colors)
print(colors.index("red"))
colors += ["red"]
print(colors)
print(colors.index("red", 1))
colors += "red"
print(colors)

# count()메서드 : 현재 해당 갑의 개수를 반환
# pop()메서드 : 값을 뽑아내서 반환
print(colors)
print(colors.count("red"))
print(colors.pop())
print(colors.pop())
print(colors.pop(1))
print(colors)

# remove()메서드 : 단순히 해당 값을 삭제
print(colors)
print(colors.remove("blue"))
print(colors)

print(colors)
colors.remove("blue")
print(colors)
# extend()메서드:데이터추가
print(colors)
print(colors.extend(["blue", "yellow", "white"]))
print(colors)

# sort()메서드 : 오름차순 정렬
# reverse()메서드 : 내림차분 정렬
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)


# 튜플
t = (1, 2, 3)
print(type(t))

# 함수에서 하나 이상의 값을 리턴하는


def calc(a, b):
    return a+b, a*b


x, y = calc(5, 4)
print(x, y)

# 문자열 포맷팅
print("id :%s, name:%s" % ("kim", "안소영"))

# 튜플에 있는 값을 함수 인수로 사용하는 경우
args = (3, 4)
print(calc(*args))

# 세트
a = {1, 2, 3, 4}
b = {3, 4, 4, 5}
print(a)
print(b)
print(type(a))
print(type(b))

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# 리스트,세트,튜플은 다음과 같이 생성자list(),set(),tuple()을 이용해서 서로 변환 가능
# TUPLE->SET
a = set((1, 2, 3, 2))
print(a)
print(type(a))
# SET->LIST
b = list(a)
print(b)
print(type(b))
# LIST->TUPLE
c = tuple(b)
print(c)
print(type(c))

# 딕셔너리
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

colors = {"apple": "red", "banana": "yellow"}
print(colors)

colors["cherry"] = "red"
print(colors)

for item in colors.items():
    print(item)

for k, v in colors.items():
    print(k, v)

print(colors)
del colors["cherry"]
print(colors)
colors.clear()
print(colors)

device = {"아이폰": s, "아이패드": 10, "윈도우플랫": 20}
device["아이맥"] = 15
device["아이폰"] = 6
print(device)
del device["아이폰"]
print(device)

phone = {"kim": "1111", "lee": "2222", "park": "3333"}
print(phone.keys())
print(phone.values())

print("park" in phone)
print("moon" in phone)

p = phone
print(p)

# 디셔너리 for문으로 참조하기
d = {"a": 100, "b": 200, "c": 300}

for key in d.keys():
    print(key)
for value in d.values():
    print(value)

# bool 참과 거짓을 나타내는 자료형 true,false 사용 가능
isRight = False
print(type(isRight))
print(1 < 2)
print(1 != 2)
print(1 == 2)
print(True and True and False)
print(1 == 2)
print(True or False or False)

# 수치를 논리연산자에 사용하는 경우
# 0은 False로 간주 . 음수를 포함한 다른 값은 모두 True로 간주
# 문자열을 논리 연산자에 사용하는 경우에도 "만 False로 간주
# 값이 없는상태를 타나내는 NOne도 False로 간주
print(bool(0))
print(bool(-1))
print(bool("test"))
print(bool(None))
print(bool(""))
print(bool(" "))
print(bool(''))
print(bool(' '))

# immutable 객체(상태변경x)
print("immutable 객체")
a = 99
b = 99
c = 99
d = 99
e = 99
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
print(hex(id(d)))
print(hex(id(e)))

# mutable 객체(상태변경o)

print("\mutable 객체")
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
arr3 = [1, 2, 3]
arr4 = [1, 2, 3]
print(hex(id(arr1)))
print(hex(id(arr2)))
print(hex(id(arr3)))
print(hex(id(arr4)))

# immutable 객체(상태 변경 불가능)
print("a"*50)
print("immutable 객체예제")
print("a"*50)
print("i, int 값이 변환되면?")
num1 = 99
num2 = 99
num3 = 99
num4 = 99
print(f"num1 값 : {num1} \t주소 : {hex(id(num1))}")
print(f"num2 값 : {num2} \t주소 : {hex(id(num2))}")
print(f"num3 값 : {num3} \t주소 : {hex(id(num3))}")
print(f"num4 값 : {num4} \t주소 : {hex(id(num4))}")
num1 += 1
num3 += 1
num4 += 10
print(f"num1 값 : {num1} \t주소 : {hex(id(num1))}")
print(f"num2 값 : {num2} \t주소 : {hex(id(num2))}")
print(f"num3 값 : {num3} \t주소 : {hex(id(num3))}")
print(f"num4 값 : {num4} \t주소 : {hex(id(num4))}")

# immutable 객체 str값 변경시
print("\n2, str 값이 벼경된다면?")
s1 = "BlockDMask"
s2 = "BlockDMask"
s3 = "BlockDMask"
s4 = "BlockDMask"
print(f"s1 값 : {s1} \t주소 : {hex(id(s1))}")
print(f"s2 값 : {s2} \t주소 : {hex(id(s2))}")
print(f"s3 값 : {s3} \t주소 : {hex(id(s3))}")
print(f"s4 값 : {s4} \t주소 : {hex(id(s4))}")
s1 = s1.replace('D', 'ZZZ')
s2 = "BlockDMask"
s4 = s3.upper
print(f"s1 값 : {s1} \t주소 : {hex(id(s1))}")
print(f"s2 값 : {s2} \t주소 : {hex(id(s2))}")
print(f"s3 값 : {s3} \t주소 : {hex(id(s3))}")
print(f"s4 값 : {s4} \t주소 : {hex(id(s4))}")

# mutable 객체-list,set,디셔너리
# print("a"*50)
#print("mutable 객체예제")
# print("a"*50)
#print("1, List 값이 변환되면?")
#arr1 = ['a', 'b', 77]
#arr2 = ['a', 'b', 77]
#arr3 = ['a', 'b', 77]
#print(f"arr1 값 : {arr1} \t주소 : {hex(id(arr1))}")
#print(f"arr2 값 : {arr2} \t주소 : {hex(id(arr2))}")
#print(f"arr3 값 : {arr3} \t주소 : {hex(id(arr3))}")
# arr1.oppend(10)
# arr2.oppend(10)
#rint(f"arr1 값 : {arr1} \t주소 : {hex(id(arr1))}")
#print(f"arr2 값 : {arr2} \t주소 : {hex(id(arr2))}")
#print(f"arr3 값 : {arr3} \t주소 : {hex(id(arr3))}")

print("\n2, dictonary 값이 벼경된다면?")
d1 = {'a': 11, 'b': 22, 'c': 33}
d2 = {'a': 11, 'b': 22, 'c': 33}
d3 = {'a': 11, 'b': 22, 'c': 33}
print(f"d1 값 : {d1} \t주소 : {hex(id(d1))}")
print(f"d2 값 : {d2} \t주소 : {hex(id(d2))}")
print(f"d3 값 : {d3} \t주소 : {hex(id(d3))}")
d1['a'] = 99
d1['d'] = 44
print(f"d1 값 : {d1} \t주소 : {hex(id(d1))}")
print(f"d2 값 : {d2} \t주소 : {hex(id(d2))}")
print(f"d3 값 : {d3} \t주소 : {hex(id(d3))}")


t = ()
print(t)
xy = (2560, 1330)
print(xy)
color = 129, 247, 216
print(color)
xy+color
print(xy+color)
xy*2
print(xy*2)

print()

color = 129, 247, 216
red, green, blue = color
print(red)
print(green)
print(blue)

x, y = 1920, 1080
print(x)
print(y)

print()

x = 2560
y = 1440
x, y = y, x
print(x)
print(y)

a = (123, "abc", True, 123)
print(a[1])
print(a[2:])
# print(a[1]=2)
print(a.index("abc"))
print(a.count(123))
t = (1, 2, 3)
t += (4,)  # 추가 : a, (콤마해주기)
print(t)

print()

d = {}
urls = {"google": "google.com", 18: "unesco.org"}
urls["x"] = 2560
print(urls)
urls["x"] = 1920
print(urls)
del urls["x"]
print(urls.pop(18))
print(urls.clear())

print()

urls = {"google": "google.com", 18: "unesco.org"}
print(urls.get("google"))
print("google" in urls)
print("google.com" in urls)
print("google.com" in urls.values())

print()

game = {"LOL", "Overwatch", "tetris", 1942, 2048}
print(game)
print(set("Funny"))
print(set([2048, "Tetris", "Cube"]))
print(set((2560, 1440)))
print(set({"google": "google.com", 18: "unesco.org"}))
print(set(range(3)))

print()

s3 = {3, 6, 9, 12}
s4 = {4, 8, 12, 16}
s3 & s4
print(s3.intersection(s4))

s3 | s4
print(s3.union(s4))

s3-s4
print(s3.difference(s4))

s3 ^ s4
print(s3.symmetric_difference(s4))

# 숙제
our_team = ["김비야", "김유진", "박선주", "백선미", "안소영",
            "양헤원", "이혜령", "임재연", "최윤영", "최혜민", "하도연", "하진"]
print(our_team[9])
print(our_team[5:9])

club = {"김비야": "영화감상반", "김유진": "코딩클리닉반", "박선주": "도서반", "백선미": "심리학연구반",  "안소영": "금융경제반",
        "양혜원": "피구반", "이혜령": "교지편집반", "임재연": "또래상담반", "최윤영": "사진반", "최혜민": "코딩클리닉반",
        "하도연": "배드민턴반", "하진": "영화감상반"}

print(club["안소영"])

print(club[our_team[0]])


# mutable 객체 안에 있는 immutable
# mutable
print("a"*50)
print("mutable 객체 요소로 존재하는 immutable,mutable")
print("a"*50)
arr1 = [55, 66, [11, 22], 'a', 'b']
arr2 = [55, 66, [11, 22], 'a', 'b']
# 리스트(immutable) 객체의 주소
print(f"arr1:{arr1}\t:{hex(id(arr1))}")
print(f"arr2:{arr1}\t:{hex(id(arr2))}")

# 리스트 내부의 mutable 요소
print("-"*50)
print("리스트 내부의 mutable 요소들")
print(f"arr1[0] : {arr1[0]} \t주소 : {hex(id(arr1[0]))}")
print(f"arr2[0] : {arr2[0]} \t주소 : {hex(id(arr2[0]))}")
print(f"arr1[1] : {arr1[1]} \t주소 : {hex(id(arr1[1]))}")
print(f"arr2[1] : {arr2[1]} \t주소 : {hex(id(arr2[1]))}")
print(f"arr1[3] : {arr1[3]} \t주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]} \t주소 : {hex(id(arr2[3]))}")
print(f"arr1[4] : {arr1[4]} \t주소 : {hex(id(arr1[4]))}")
print(f"arr2[4] : {arr2[4]} \t주소 : {hex(id(arr2[4]))}")

# 리스트 내부의 mutable 요소 (그 안에 있는 mutable 인 list는 어떨까? -> 각각 주소가 다른것을 볼 수 있음)
print("-"*50)
print("리스트 내부의 mutable 요소들")
print(f"arr1[2] : {arr1[2]} \t주소 : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]} \t주소 : {hex(id(arr2[2]))}")


# 얕은 복사, 깊은 복사

# 얕은 복사
arr1 = [1, 2, 3]
arr2 = arr1
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")
arr1.append(4)
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")

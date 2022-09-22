print('Python start!')
print("Python start!")
print("""Python start!""")
print('''Python start!''')

print()

print('p','y','t','h','o','n', sep='')
print('010','7777','7777',sep='-')
print('python','google.com',sep='@')

print()

print('Welcome To',end='    ')
print('IT News', end='')
print('web site')

print()

import sys
print("learn Python", file=sys.stdout)

#숫자형

print(8+5)
age=18
print(age)

after_2=2      
print(age+after_2)
result= age-after_2    
print(result)

print()
age=18  
print(age)
age +=2
print(age)
age -=1
print(age)
age *=2
print(age)
age /=2
print(age)
age //=2
print(age)
age %=6
print(age)
age **=3
print(age)

print()
age=18
print (type(age))
pi=2.14
print(type(pi))
age /=2             #9.0
print(type(age))
x=10+3.14           #13.14
print(type(x))

print()
print(0b110111000)  #2진수
print(type(0b110111000))
print(0o130)        #8진수
print(type(0o130))       
print(0xD7A)        #16진수
print(type(0xD7A))

print()
print(10e3)
print(type(10e3))
print(1.23456E2)
print(type(1.23456E2))
print(1.23456e-2)
print(1.23456e22)

print()
print(8+24j)    #실수:8, 허수:24인 복소수
c =1.2+3.4J     #실수:1.2. 허수:3.4인 복소수
print(type(1.2+3.4j))
print(c.real)
print(c.conjugate())    #컬레 복소수를 구하는 함수
d=1j
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
#문자형
print()
greeting='Hello'
to="wold!"
print(greeting)
print(type(greeting))
say_hello =greeting +","+to
print(say_hello)
print("Hello*5")
print("\"Hello\"\n"+to)
multilne ="""Happy
programming"""
print(multilne)

s = "Life is too short."
print(s[3])
print(s[11])
print(s[-1])
print(s[-7])
print(s[-18])

s = "Life is too short, you need python."
print(s[3:7])       #인덱스 3부터 인덱스 7번 바로 앞(6) 바로 앞까지
print(s[-10:-7])    #인데스 -10번부터 인덱스 -7번 바로 앞까지
print(s[3:-10])     #
print(s[-10:30])    #
print(s[3:2])       #인덱스 3번부터 인덱스 2번 바로 앞까지. 못 구함 (주의)
print(s[30])        #인덱스 30번부터 맨 뒤까지
print(s[-7])        #인덱스 -7번부터 맨 뒤까지
print(s[:4])        #맨 알부터 인덱스 4번 바로 앞까지
print(s[-17])       #
print(s[:])         #맨 앞부토 맨 뒤까지. 즉 문자열 전체

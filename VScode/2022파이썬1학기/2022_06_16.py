# 근로세득에 대한 소득세
import random
import random  # 임의의 값을 얻기 위해 사용하는 random 모듈을 가져온다
from re import T


num = int(input())
if num <= 2000:
    tax = num*0.05
elif num <= 4000:
    tax = num*0.15
elif num <= 8000:
    tax = num*2.5
elif num > 8000:
    tax = num*0.4
else:
    print("근로 소득 없음")


# 현 연봉 근무평가 등급을 입력 연봉인상액, 새 연봉인상액

i = int(input("현 연봉을 입력 하세요: "))
j = (input("근무평가등급을 입력하세요. (우수, 보통, 불량) : "))

if j == '우수':
    print()


# 입력 받은 수가 소수 인지 판별하는 프로그램을 작성하라 ( 과제 )


# 함수
def times(a, b):
    return a*b


print(times)
print(times(10, 5))

myTimes = times
print(times)
print(times(10, 5))

myTimes = times
print(myTimes)
print(times(10, 5))

# 표준함수와 사용자 정의 함수

# 절댓값
print(10, "의 절댓값: ", abs(10))
print(-10, "의 절댓값: ", abs(-10))
# 10진수 -> 2진수변환
print(128, "의 2진수 : ", bin(128))
print(255, "의 2진수 : ", bin(255))

print(7, "의 8진수 : ", oct(7))
print(8, "의 8진수 : ", oct(8))

print(15, "의 16진수 : ", hex(15))
print(16, "의 16진수 : ", hex(16))
# 연산
number = [1, 5, -2, 0, 6]
print(number, "중 가장 큰 값은", max(number))
print(number, "중 가장 작은 값은", min(number))
print(number, "합계는", sum(number))
print("2의 10승은 ", pow(2, 10))
# 반올림
pi = 3.56789
print(pi, "의 소수점 1자리 반올림은", round(pi))
print(pi, "의 소수점 1자리 반올림은", round(pi, 0))
print(pi, "의 소수점 2자리 반올림은", round(pi, 1))
print(pi, "의 소수점 3자리 반올림은", round(pi, 2))
print(pi, "의 소수점 4자리 반올림은", round(pi, 3))
# 문자열 관련 내장 함수와 문자열 형 변환 함수
user_name = input("이름은? ")
user_age = input("나이는? ")
print(user_name + "님! 나이는 " + str(user_age) + "세군요!")
say = "{0}님! 나이는 {1}세군요! {1}세라니 놀라워요!"
print(say.format(user_name, user_age))

pi = "3.14159"

print("문자열 출력 :", pi)
print("실수 변환 출력 : ", float(pi))
print(float(pi)+100)
year = "2018"
print("올해 연도 : ", year)
print("100년 뒤는", int(year) + 100, "년 입니다.")
print("숫자를 문자열로 변환하려면 str()을 이용합니다.")
print("올해는 "+str(year)+"년입니다.")

# 리스트 관련 내장 함수
list = ['d', 'c', 'a', 'b']
list.reverse()
print("리스트 항목 순서 뒤집기", list)
list.sort()
print("리스트 항목 정렬하기", list)
list.sort(reverse=True)
print("리스트 항목 역정렬하기", list)
for index, value in enumerate(list):
    print("인덱스", index, "위치의 값은 ", value)

str1 = "나는 문자열"
print(str)
n = 3
print(str(n))  # TypeError: 'str' object is not callable => str을 문자열로 부를수 없다. (str을 변수로 잡았기 때문에 오류( 객체로 봄 )=>str1은 가능.)

# 사용자 정의 함수


def input(s):
    print(s)


input("현재의 input() 함수는 사용자 정의 함수 입니다.")

# 매개변수가 없는 함수
# 주사위 굴리는 프로그램 만들기

# 첫 프로그램
n = random.randint(1, 6)  # 1에서6까지의 정수 중에서 하나를 뽑는다.
print("결과 : ", n)
n = random.randint(1, 6)
print("결과 : ", n)
n = random.randint(1, 6)
print("결과 : ", n)

# 출력 결과 변경 시 => 변경하고자 하는 출력문을 일일이 수정

# 함수화


def rolling_dice():
    n = random.randint(1, 6)
    print("6면 주사위 굴린 결과: ", n)


rolling_dice()
rolling_dice()
rolling_dice()

# • 입력 받은 수가 소수인지 판별하는 프로그램을 작성하라
# • 소수는 어떻게 구할까?
# • n이 소수인지 판별하기 위해서는 2부터 n까지의 숫자 중 나누어서
# 나머지가 0인 숫자가 있고, 그 숫자가 n과 다르다면 소수가 아니다.
# 만약 나누어 떨어진 숫자가 n과 같다면 그 수는 소수이다.


def prime_number(number):
    if number != 1:

        for f in range(2, number):

            if number % f == 0:
                return False
    else:
        return False

    return True


num = input("숫자 입력: ")
if prime_number(int(num)):
    print("숫자" + num + " = 소수 입니다.")
else:
    print("숫자 " + num + " = 소수가 아닙니다.")


# 매개변수가 있는 함수
import random
print()


def rolling_dice(pip):
    n = random.randint(1, pip)
    print(pip, "면 주사위 굴린 결과 : ", n)


rolling_dice(4)
rolling_dice(6)
rolling_dice(10)

print()


def rolling_dice(pip, repeat):
    for r in range(1, repeat+1):
        n = random.randint(1, pip)
        print(pip, "면 주사위 굴린 결과", r, ":", n)


rolling_dice(4, 3)
rolling_dice(6, 2)
rolling_dice(10, 4)

print()

# def func_sum(in_list):
#    sum=0
#    li= in_list.split()
#    print(li)
#    for i in range(0,len(li)):
#        sum += int(li(i))
#    return sum
#in_list=input("데이터 입력 : ")

#print("합 : ",func_sum(in_list))

print()

print("❤")
print("❤", "🐱")
print("❤", "🐱", "📺")

print()


def p(*args):
    for a in args:
        str = str + a
    print(str)


print("❤")
print("❤", "🐱")
print("❤", "🐱", "📺", "🤞")

print()


def p(space, space_num, *args):
    str = args[0]
    for i in range(1, len(args)):
        str = str + (space * space_num)+args[i]
    print(str)


p(",", 3, "❤")
p(".", 2, "❤", "🐱")
p("_", 3, "❤", "🐱", "📺", "🤞")

print()


def star(num1, *num2):
    for a in num2:
        print(num1*a)


star("✌", 3)
star("❤", 1, 2, 3,)

# 키워드인자를 사용한 함수
# 위치 인자 : 호출하는 함수의 매개 변수 순서대로 호출되는 함수의 인자 값에 해당 값이 넘겨짐
# 키워드 인자 : 함수 정의에 있는 변수듫의 순서에 상관없이 직접 변수명을 지정하여 함수 호출

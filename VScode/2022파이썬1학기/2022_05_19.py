# 리스트에서 중복된 숫자들을 제거해 보자
a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]
print("원본 : ", a)
print("중복 제거 후 : ", list(set(a)))

# 파이썬은 다음과 같이 동일한 값에 여러개의 변수를 선언할 수 있다. a,b 변수를 선언한후 a의 첫번째 요소 값을 변경하면 b의 값은?
a = b = [1, 2, 3]
a[1] = 4
print(a)
print(b)

# ,변수
a = b = [1, 2, 3]
print(hex(id(a)))
print(hex(id(b)))
a[1] = 4
print(a)
print(b)
print(hex(id(a)))
print(hex(id(b)))

print(bin(0b1010))
print(bin(0b1010 & 0b0110))
print(bin(0b1010 | 0b0110))
print(bin(0b1010 ^ 0b0110))
print(bin(~0b1010))

print((0b1010))
print((0b1010 & 0b0110))
print((0b1010 | 0b0110))
print((0b1010 ^ 0b0110))
print((~0b1010))

print(bin(0b1010 << 2))
print(0b1010 << 2)
print(bin(0b1010 >> 2))
print(0b1010 >> 2)
# if문
a = 5
if a < 5:
    print("테스트 입니다")
else:
    print("else문 입니다")

#x = input("숫자입력 : ")
# print(a)
# print(type(x))

#x = int(input())
# if x % 2 == 0:
 #   print("짝수")
# else:
#    print("홀수")

#password = input("암호를 입력하세요 : ")
# f password == "암호":
#    print("암호이다")
# else:
 #   print("암호가 아니다")

# 예(1)
money = 1
if money:
    print("택시를")
print("타고")
#    print("가자")

money = 2000
if money >= 3000:
    print("택시를 타고 가다")
else:
    print("걸어 가다")

money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가다")
else:
    print("걸어 가다")

# 만약 주머니에 돈이 있으면 택시를 타고 없으면 걸어가라
pocket = ['paper', 'cellphone', 'money', 'card']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("갈아 가라")
# 주머니에 돈이 있으면 아무 것도 하지 말고, 돈이 없으면 카드를 꺼내라
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
print("수행 완료")

# 만약 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라.
pocket = ['money', 'card']
if 'money' in pocket:
    print("택시를 타라 -money")
else:
    if 'card' in pocket:
        print("택시를 타라 -card")
    else:
        print("걸어 가라")

saying = "Life is too short, you need python"

if "wife" in saying:
    print("wife")
elif "python" in saying and "you" not in saying:
    print("python")

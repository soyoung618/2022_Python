import random
from re import T
random_numer=random.randint(1,100)
print(random_numer)
cnt=1
while True:
    try:
        my_number=int (input("1~100 사이의 수 입력 : "))
        if(my_number>random_numer):
            print("다운")
        elif(my_number<random_numer):
            print("업")
        else:
            print(f"{cnt}회 만에 맞았습니다 ~!~!~!~!")
            break
        cnt=cnt+1
    except:
        print("에러가 발생 했습니다. 숫자를 입력하세요.")
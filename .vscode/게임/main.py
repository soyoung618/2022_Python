import random
origin=[0,0,0]
#데이타 생성
for i in range(0,3):
    origin[i]=random.randint(0,9)
    for j in range(0,i):
        if origin[i] == origin[j]:
            origin[i]=random.randint(0,9)

    print(origin[i],end= " ")
print()

#user 데이터 입력
my_data=[0,0,0]
for i in range(0,3):
    my_data[i]=int(input())

#판정
#strike
strike=0
for i in range(0,3):
    if(origin[i]==my_data[i]):
        strike=strike+1
print(strike,"strike")

#ball
ball=0
for i in range(0,3):    #origin 방 번호
    for j in range(0,3):     #my_data 방 번호
        if(i!=j):    #ball 처리
            if(origin[i]==my_data[j]):
                ball=ball=1

print(ball,"ball")


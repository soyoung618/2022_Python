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
cnt=0
while True:
    #user 데이터 입력
    my_data=[0,0,0]

    my_data=input(f"{cnt},숫자를 입력 하세요.").split(" ")
    my_data=list(map(int,my_data))
    #print(my_data)
    cnt=cnt+1

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

if(strike==3):
    print(f"축하합니다. {cnt}회 만에 맞추었습니다.")
elif(cnt==10):
    print()
    


# 2305 안소영
print("1 ~ N 까지의 소수와 그 갯수를 구하는 프로그램")
num = int(input("N 입력 : "))
n=int(input());#정수 입력받기

for i in range(1,n+1):
    if(n%i==0):
        print(i, end=" ")

prime_count = 0
for num1 in range(1, num+1):
    count = 0
    for x in range(1, num1+1):
        if num1 % x == 0:
            count = count+1
    if count == 2:
        prime_count = prime_count+1
print("1 ~ ", num, "까지 소수의 갯수 : ", prime_count)

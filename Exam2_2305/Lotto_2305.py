# 2305 안소영
import random

myList=[]
num = random.randrange(0,10)

for i in range(10):
    while num in myList:
        num=random.randrange(0,10)
    myList.append(num)

def func_lotto():
    num = random.randint(1, 45)
    num1 = random.randint(1, 45)
    num2 = random.randint(1, 45)
    num3 = random.randint(1, 45)
    num4 = random.randint(1, 45)
    num5 = random.randint(1, 45)

    print("당첨번호 : ", num, num1, num2, num3, num4, num5)

func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
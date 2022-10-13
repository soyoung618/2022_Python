from calculator import add
from calculator import sub
from calculator import mul
from calculator import div

num1=int(input("첫번째 수는? : "))
num2=int(input("두번째 수는? : "))
print(num1,"+",num2,"=",add(num1,num2))
print(num1,"-",num2,"=",sub(num1,num2))
print(num1,"*",num2,"=",mul(num1,num2))
print(num1,"/",num2,"=",div(num1,num2))
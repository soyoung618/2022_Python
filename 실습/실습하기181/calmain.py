import calculator

num1=int(input("첫번째 수는? : "))
num2=int(input("두번째 수는? : "))

print(num1,"+",num2,"=",calculator.add(num1,num2))
print(num1,"-",num2,"=",calculator.sub(num1,num2))
print(num1,"*",num2,"=",calculator.mul(num1,num2))
print(num1,"/",num2,"=",calculator.div(num1,num2))
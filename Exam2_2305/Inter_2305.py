# 2305 안소영

str1 = (input("첫 번째 문자열 입력 : "))
str2 = (input("두 번째 문자열 입력 : "))

intersection = list(set(str1) & set(str2))
print( intersection ) 
intersection = list(set(str1).intersection(str2))
print( intersection ) 

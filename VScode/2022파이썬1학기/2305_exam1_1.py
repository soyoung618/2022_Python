#주민등록번호 앞 6자리를 변수 id_number에 넣고 출생년도 끝 두자리 \n출생 월일 \n그 두개의 곱 출력

id_number= "020316"
year=id_number[0:2]
day=id_number[2:6]

print(year)
print(day)
print(int(year)*int(day))

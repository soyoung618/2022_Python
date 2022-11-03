from datetime import datetime
from unittest import result
today =datetime.today()
weekdat = today.weekday()
week=""
if weekdat ==0:
    week="월"
elif weekdat ==1:
    week="화"
elif weekdat ==2:
    week="수"
elif weekdat ==3:
    week="목"
elif weekdat ==4:
    week="금"
elif weekdat ==5:
    week="토"
else:
    week="일"

result_format ="오늘은{:d}년 {:d}월 {:d}일 {}요일 입니다."
result=result_format.format(today.year,today.month,today.day,week)
print(result)

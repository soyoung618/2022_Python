from gtts import gTTS   #텍스트를 음성으로 변환
from playsound import playsound

file_path="Mydata.txt"
with open(file_path,'rt',encoding='UTF8') as f:
    read_file=f.read()
#test="안녕하세요 파이썬 입니다."

tts=gTTS(text=read_file, lang="ko")
mp=("schoolsong.mp3")
tts.save(mp)

playsound(mp)
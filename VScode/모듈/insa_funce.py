import hello_func
import greeting_func

def main():
    print("insa_finc 모듈입니다.")
    print("__name__ :",__name__)  #실행하면 __main__이 출력된다
    hello_func.heelo()
    greeting_func.greeting()
main()
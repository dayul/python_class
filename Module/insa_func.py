import hello_func
import greeting_func

def main() :
    print("insa 모듈 입니다")
    print("__name__ : ", __name__)      # __main__ 출력됨 (내장 변수 __name__ : 해당 모듈의 이름을 가짐)
    hello_func.hello()
    greeting_func.greeting()

main()

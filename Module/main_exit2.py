import sys as s         # 모듈이름 변경해서 import

sys = "반복 시스템 입니다."

while True:
    print(sys)
    print(s.path)  # 모듈 검색 경로
    print("종료하려면 exit를 입력하세요. ")
    user_input = input("> ")
    if user_input == "exit":
        s.exit()
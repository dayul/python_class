# exit 함수를 import 가능

import sys
# from sys import exit - 이렇게 import하고 sys.exit() 하면 에러

while True:
    print("종료하려면 exit를 입력하시오")
    user_input = input("> ")
    if user_input == "exit":
        sys.exit()
        # exit()
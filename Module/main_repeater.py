from repeater import *      # 모든 함수를 import - 출처를 밝히지 않아도 됨
# import sys - 같긴한데 import만 하면 sys.함수() 처럼 출처를 밝혀야 함
# from repeater import repeat, once

s = input("반복할 문자를 입력하시오.")
n = input("반복 횟수를 입력하시오.")
repeat(s, int(n))
repeat(s)
once(s)
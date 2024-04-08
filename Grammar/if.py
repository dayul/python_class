# 아래 들여쓰기가 중요함, {}같은 역할
age = int(input())            # 문자로 받은 값을 정수형으로 변환
if 10 <= age < 20:
    print("10대")
elif 20 <= age < 30:            # else-if를 줄여서 elif라고 씀
    print("20대")
else:
    print("10, 20대가 아님")

x = int(input())
if x >= 10 and x % 2 == 0:      # 여러 조건
    print("10 이상 짝수")

y = int(input())
if x > 10:          # 중첩 제어문
    if x % 2 == 0:
        print("10 초과 짝수")
    else:
        print("10 초과 홀수")
else:
    print("10 이하")



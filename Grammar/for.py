for i in range(3, 9, 2):    # 3에서 9-1까지 2씩 증가
    print(i)        # 3 5 7

for ch in "Love":           # 문자열
    print(ch)       # L o v e

for item in ["힙합", "발라드"]:      # 리스트
    print(item)     # 힙합 발라드

for item in (2459, 305):    # 튜플
    print(item)     # 2459 305

pl = {"C":1972, "Java":1995, "Python":1991}     # 딕셔너리
for key in pl:
    print(key, ":", pl[key])        # 쉼표 (,)나 + 로 이어서 쓸 수 있음

for item in {"HTML", "CSS", "Javascript"}:
    print(item + "을 할 수 있다.")


for i in range(1, 9+1):       # 1부터 9까지
    print("2 X {} = {}".format(i, 2*i))

# 중첩 반복문
for dan in range(2, 10):
    print("---{}단----".format(dan))
    for i in range(1, 10):
        print("{} X {} = {}".format(dan, i, dan*i))
    print("----------")

# 리스트 요소 출력
table = [["월", "화", "수"], [100, 200, 300]]
for row in table:
    for col in row:
        print(str(col) + " ")       # str() 문자열로 변환, 문자열 + 정수 연산 안됨
    print()

# break, countinue문
for i in range(1, 10):
    if i == 7:
        break
    print(i)

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print("2 X {} = {}".format(i, 2*i))
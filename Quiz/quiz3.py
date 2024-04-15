height = float(input("키를 입력해주세요 : "))   # input() 안에 문자열을 넣어 입력에 도움을 줌

if (height >= 140 and height < 170) or (height >= 175 and height <= 180):
    print("탑승 가능")
# elif height >= 175 and height <= 180:
#     print("탑승 가능")
else:
    print("불가능")

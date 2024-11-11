import array

f = open("data.bin", "wb")      # 이진 데이터 쓰기 모드

byte_arr = []
for i in range(0, 256):
    byte_arr.append(i)

data = bytes(byte_arr)      # byte로 변환
f.write(data)

f.close()

f = open("data.bin", "rb")      # 이진 데이터 읽기
data = array.array("B")         # unsign char 타입이 저장될 것이라는 것을 명시
data.fromfile(f, 10)        # 이진 파일의 내용을 불러옴 10개 == 10byte

for item in data:
    print(item, end=", ")
f.close()
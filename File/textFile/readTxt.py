f = open("text.txt", "w", encoding="utf-8")

f.write("안녕하세요")
f.write("\n")
f.write("유후")
f.write("\n")

f.close()

# 파일 읽기
f = open("text.txt", "r", encoding="utf-8")
# str = f.read()      # 파일 내용 전체를 읽어옴
# print(str)

# \n을 기준으로 한줄로 인식
line1 = f.readline()
print("1 : " + line1)
line2 = f.readline()
print("2 : " + line2)
line3 = f.readline()
print("3 : " + line3)       # 빈 문자열

f.close()
# 쓰기 접근 모드이므로 파일이 없으면 생성해서 연다.
f = open("file.txt", "w")

f.write("hello")
f.write("\n")
f.write("world")

f.close()

# 이어 붙이기 모드3
f = open("file.txt", "a")

f.write("\n")
f.write("append")
f.close()

# 한글 입력
# f = open("file.txt", "w", encoding="utf-8")
# f.write("안녕")
# f.close()

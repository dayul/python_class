s = "Life is too short, You need Python."
# 인덱싱
print(s[0])     # 첫번째 글자
print(s[11])    # " "
print(s[-1])    # 마지막 글자
print(s[-18])   # 첫번째 글자

# 슬라이싱 문자열
# [인덱스1 : 인덱스2 : 간격] (인덱스1부터 인덱스2-1 까지 간격에 맞게 출력)
print(s[3:7])
print(s[3:-10])
print(s[-10:-7])
print(s[3:2])   # 못 구함
print(s[30:])   # 30번부터 끝까지
print(s[-7:])   # -7부터 뒤까지
print(s[:4])    # 처음부터 4번 바로 앞까지
print(s[:])     # 문자열 전체




str = " PeYeTeHeOeN "
str1 = str.strip()      # 왼쪽 오른쪽 모두 공백 없애기
str2 = str1.split('e')  # e를 기준으로 리스트화
answer1 = ''.join(str2) # 공백으로 리스트를 문자열로 바꿈
print(answer1)
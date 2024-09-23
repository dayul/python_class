from datetime import datetime

# 현재 날짜 시각 객체 얻기
today = datetime.now()
print('현재 시각', today)

print('연, 월, 일 : ', today.year, today.month, today.day)
print('시, 분, 초 : ', today.hour, today.minute, today.second)
print('요일 : ', today.weekday())     # 월요일0~ 일요일6 (속성이 아니라 메소드임)

# 특정 날짜 객체 만들기
day = datetime(2018, 1, 1, 0, 0, 0)
print(day)

# 2018년부터 지나온 시간 구하기
print(today - day)
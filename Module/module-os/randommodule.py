import random

print(random.random())      # 0이상, 1미만 실수

print(random.uniform(2, 5)) # 시작 2 이상, 끝 10 미만 실수

print(random.randrange(1, 7, 2))     # step도 줄 수 있음
                                                    # 1, 3, 5 정수
# 리스트 선택
season = ['봄', '여름', '가을', '겨울']
print(random.choice(season))

list = [1, 2, 3, 4, 5]
# 순서 섞기
random.shuffle(list)
print(list)

print(random.sample(list, 2))   # lsit에서 중복없이 2개뽑기
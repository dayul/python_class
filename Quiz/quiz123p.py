import random

# 1번
def gugudan(dan=2):
    for i in range(dan, dan + 1) :
        for j in range(1, 9 + 1):
            print("{:d} x {:d} = {:d}".format( i, j, i*j))

gugudan()       # 기본으로 2단 출력
gugudan(8)      # 8단 출력

# 2번
def rolling_dice(pip=6, repeat=1):
    for r in range(1, repeat + 1):
        n = random.randint(1, pip)
        print(str(pip) + "면 주사위 굴린 결과", r, ":", n)

rolling_dice()      # 기본 인자 사용
rolling_dice(6, 2)
rolling_dice(5, repeat=1)       # 키워드 인자 사용

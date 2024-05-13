#  별 찍기
# *
#  *
#   *
#    *

for i in range(1, 6):
    for j in range(1, 6):
        if j == i:
            print("*", end="")      # j와 i가 같을 때만 별을 출력
        else:
            print(" ", end="")
    print()

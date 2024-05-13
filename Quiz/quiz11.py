# 문자열을 이용하여 369게임을 했을 때, (끝자리가 3, 6, 9일때마다 박수를 한번씩 친다.)
# 1부터 100까지 진행하여 박수를 친 횟수를 출력

clap = 0

for i in range(1, 101):
    a = str(i)
    # if a[-1] == '3' or a[-1] == '6' or a[-1] == '9':
    if a[-1] in ['3', '6', '9']:
        clap += 1


print(clap, "번")
print("{:d}번".format(clap))
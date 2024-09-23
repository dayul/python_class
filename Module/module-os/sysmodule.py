import sys

print('실행 파일명', sys.argv[0])

for i in range(1, len(sys.argv)) :
    print(sys.argv[i])

sys.exit()

print('exit 아래 내용은 출력되지 않음')
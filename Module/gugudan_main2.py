import gugudan2

def main():
    for i in range(9, 10):
        print("=" * 20)
        gugudan2.gugudan(i)

if __name__ == "__main__":          # __name__이 __main__일 경우에만 실행
    main()  
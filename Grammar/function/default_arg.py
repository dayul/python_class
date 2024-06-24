def hello(msg="안녕"):
    print(msg + "!")

hello("하이")
hello()

def hello2(name="없음", msg="안녕"):
    print(name + msg)

hello2("추", "하이")
hello2("추")
hello2()

def hello3(name, msg="안녕"):     # 기본인자는 뒤에
    print(name + msg)
hello3("김")

def fn(a, b=[]):
    b.append(a)
    print(b)

fn(3)
fn(5)       # b는 최초 실행때만 초기화 , [3, 5]
fn(10)      # [3, 5, 10]

def hello4(name, msg="안녕", feeling="!!"):
    print(name + msg + feeling)

hello4("박", feeling="0o0")      # 기본값인 안녕이 출력
hello4("정", msg="hello", feeling="lol")

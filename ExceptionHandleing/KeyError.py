dict = {"apple":"사과", "home":"집", 1:"one"}

try:
    print(dict["apple"])
    print(dict["error"])
except KeyError:
    print("KeyError를 처리합니다.")
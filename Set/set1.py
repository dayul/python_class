# 집합, 중복된 값을 가지지 않음, 순서가 없음
# 교집합, 합집합, 차집합 등 연산 가능

# set 생성
game = {"LoL", "Overwatch", "2048"}
print(game)     # 순서 없이 랜덤 배치

print(set("Funny"))
print(set([2048, "Cube", "Tetris"]))
print(set((2550, 3402)))
print(set({"google":"google.com", 16:"naver.com"}))     # key값만 출력
print(set(range(3)))

# set에 추가
print(game.add("Fifa"))    # 순서없이 랜덤으로 들어감
print(game.update(("NBA", "MLB")))     # 각각 들어감

# set에서 제거
print(game.remove("LoL"))

# 순서가 다 다름
# 교집합
s1 = {3, 6, 9, 12}
s2 = {4, 8, 12, 16}
print(s1 & s2)              # {12}
print(s1.intersection(s2))  # {12}

# 합집합
print(s1 | s2)      # {3, 4, 6, 8, 9, 12, 16}
print(s1.union(s2)) # {3, 4, 6, 8, 9, 12, 16}

# 차집합
print(s1 - s2)              # {9, 3, 6}
print(s1.difference(s2))    # {9, 3, 6}

# 대칭 차집합 (교집합 제외)
print(s1 ^ s2)                      # {3, 4, 6, 8, 9, 16}
print(s1.symmetric_difference(s2))  # {3, 4, 6, 8, 9, 16}

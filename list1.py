l = []      # 빈 리스트
player = ["Messi", 10, True]

# list() : list로 변환
# 1. 리스트 생성
print(list("Happy"))    # 문자열을 리스트로 ['H', 'a', 'p', 'p', 'y']
print(list((122, 323)))   # 튜플을 리스트로 [122, 323]
print(list({"menu":"pizza","price":"10000"}))       # 딕셔너리를 리스트로 ['menu', 'price']
print(list({"사과", "배"}))        # 셋을 리스트로 ['사과', '배']
nums = list(range(3))       # range() 함수의 각 요소가 하나씩 리스트로 [0, 1, 2]

# 2. 리스트 요소 추가
print(nums + [10, 11])      # [0, 1, 2, 10, 11]

nums += [10, 11]            # [0, 1, 2, 10, 11]
print(nums)

nums.append(20)
print(nums)         # [0, 1, 2, 10, 11, 20]
nums.append([30,31])     # [0, 1, 2, 10, 11, 20, [30, 31]]
print(nums)

nums.insert(2,40)
print(nums)         # [0, 1, 40, 2, 10, 11, 20, [30, 31]]

nums.extend([50,51])
print(nums)         # [0, 1, 40, 2, 10, 11, 20, [30, 31], 50, 51]

# 3. 리스트 요소 수정
nums[7] = 61
print(nums[7])      # 61
print(nums)         # [0, 1, 40, 2, 10, 11, 20, 61, 50, 51]

# 4. 리스트 요소 제거
del nums[2]     # nums[2]를 제거
print(nums)     # [0, 1, 2, 10, 11, 20, 61, 50, 51]

nums.remove(20)   # 값중 20을 제거
print(nums)       # [0, 1, 2, 10, 11, 61, 50, 51]

nums.pop()         # 번호를 안 쓰면 가장 마지막 값을 배열에서 사라지게 함
nums.pop(5)        # nums[5]를 사라지게 함

nums.clear()        # 빈 리스트로 만듦 (모든 요소 제거)

# 5. 리스트에서 요소 검색
nums = list(range(3))       # [0, 1, 2]
nums += [100, 10]
print(nums)                 # [0, 1, 2, 100, 10]
print(nums[3])              # 100

print(3 in nums)        # 요소에 3이 있나요? False
print(10 in nums)       # 요소에 10이 있나요? True

# 6. 리스트 관련 함수
print(len(nums))       # 배열 길이 출력
nums.sort()             # 오름차순
nums.reverse()          # 현재 상태에서 리스트를 거꾸로 만듦
print(nums.count(2))           # 찾고자하는 데이터의 개수를 출력

# range() 함수
# - 0부터가 기본
print(range(3))         # range(0, 3)
print(list(range(3)))   # [0, 1, 2]
print(range(1, 10))     # range(1, 10)
print(range(1, 10, 2))  # range(1, 10, 2)
print(set(range(1, 10, 2)))     # {1, 3, 5, 7, 9}
print(list(range(1, -5, -2)))   # 거꾸로, 왼쪽으로 -2씩 센다, [1, -1, -3]

for i in range(3):
    print(i)

'''
range()의 범위, 0, 1, 2를 반복
0
1
2'''
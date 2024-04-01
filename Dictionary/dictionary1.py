d = {}
urls = {"google":"google.com", 18:"unesco.org"}     # 키 값에 튜플도 넣을 수 있음

# 요소 추가, 키 값으로 지정
urls["x"] = 5500
print(urls)     # 키가 없으면 추가됨, {'google': 'google.com', 18: 'unesco.org', 'x': 5500}

# 요소 수정, 키 값으로 지정
urls["x"] = 1000
print(urls)     # 키가 있으면 수정됨, {'google': 'google.com', 18: 'unesco.org', 'x': 1000}

# 요소 제거, 키 값으로 지정
del urls["x"]   # {'google': 'google.com', 18: 'unesco.org'}
print(urls)
urls.pop(18)    # 키 값이 18인 요소를 제거
print(urls)     # {'google': 'google.com'}

# 요소 검색, 키 값으로 지정
urls = {'google': 'google.com', 18: 'unesco.org'}
print(urls["google"])   # google.com
print(urls.get("google"))   # 위와 같음
print("google" in urls)     # 키 "google"이 있는지 확인, True
print("google.com" in urls) # False

print("google.com" in urls.values())    # 값을 찾음, True

# 관련 함수
print(len(urls))
print(urls.keys())      # 가지고 있는 키들을 보여줌, dict_keys(['google', 18])
print(urls.values())    # 키 안의 값들을 보여줌, dict_values(['google.com', 'unesco.org'])
print(urls.items())     # 키와 값을 함께 보여줌, dict_items([('google', 'google.com'), (18, 'unesco.org')])
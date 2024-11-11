f = open("data.bin", "wb")      # wb : 이진데이터 쓰기모드(저장모드)
byte_arr = bytes([255, 0, 127])     # 이진 데이터로 변경
f.write(byte_arr)
f.close()
x = 3
while x < 6:
    print(x)
    x+=1        # x++이 없음


echo = input()
# while echo != "exit":
#     print(echo)
#     echo = input()
    
#위의 while문과 같음
while True:
    if echo == "exit":
        break
    print(echo)
    echo = input()

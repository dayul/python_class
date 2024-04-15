month = int(input("몇 월인지 입력하세요 : "))
day31 = [1, 3, 5, 7, 8, 10, 12]

if  month in day31:
    print("31일까지 입니다.")
elif month != 28:
    print("30일까지 입니다.")
else:
    print("28일까지 입니다.")
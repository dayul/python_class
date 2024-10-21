import os 
data = os.listdir('.')
print(data)

for d in data:
    print(d)
    print(f"is directory? : {os.path.isdir(d)}")
    print(f"is file? : {os.path.isfile(d)}")
    # print("is file? : " + str(os.path.isfile(d)))

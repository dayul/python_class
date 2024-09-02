import sys

# parameter 넣기

def tri_area(w, h):
    return w * h * 1/2

def box_area(w, h):
    return w * h

def print_area(w, h):
    print("가로", w, "세로", h, "인 삼각형의 넓이 : ", tri_area(w, h))
    print("가로", w, "세로", h, "인 사각형의 넓이 : ", box_area(w, h))

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print_area(int(sys.argv[1]), int(sys.argv[2]))
        print(sys.argv[0])      # python file의 이름이 저장되어 있음
                                # C:\Users\dyulc\Desktop\2024년도 미림 2학년\수업\python_class\pythonProject\Module\area3.py
    else:
        print("사용법 Python area3 가로 세로")
        
        
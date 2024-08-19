def tri_area(w, h):
    return w*h*1/2

def box_area(w, h):
    return w*h

def print_area(w, h):
    print("가로 : {}, 세로 : {}, 인 삼각형의 넓이 : {}".format(w, h, tri_area(w, h)))
    print("가로 : {}, 세로 : {}, 인 사각형의 넓이 : {}".format(w, h, box_area(w, h)))

if __name__ == "__main__":
    print_area(3, 5)
    print_area(6, 10)
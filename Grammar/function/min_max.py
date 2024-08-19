def min_max(*args):
    min = args[0]
    max = args[0]
    for arg in args:
        if min > arg:
            min = arg
        if max < arg:
            max = arg
    return min, max

print(min_max(52, -3, 23, 89, -21))
# 튜플
min_value, max_value = min_max(5, -3, 23, 89, -21)
print("최고", max_value)
print("최저", min_value)
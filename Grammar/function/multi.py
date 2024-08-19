def multi_num(multi, start, end):
    result = []
    for n in range(start, end + 1):
        if n % multi == 0:
            result.append(n)
    return result

multi2 = multi_num(17, 1, 200)
print("multi_num(17, 1, 200)", multi2)
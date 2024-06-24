def sum(*numbers):
    sum_value = 0
    for num in numbers:
        sum_value = sum_value + num
    return sum_value

result = sum(1,3)
print(result)
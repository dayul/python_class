def min(*numbers):
     min_value = numbers[0]
     for num in numbers:
         if min_value > num:
             min_value = num
     return min_value

result = min(1, 3, 4)
print(result)
 
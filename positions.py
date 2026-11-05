input_string = input("Введите целые числа через пробел: ").strip()

if not input_string:
    print("Нет данных")
else:
    numbers = [int(x) for x in input_string.split()]
    
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
            
    max_indices = []
    for index, num in enumerate(numbers):
        if num == max_value:
            max_indices.append(index)
            
    print(max_indices)


input_string = input("Введите целые числа через пробел: ").strip()

if not input_string:
    print("Нет данных")
else:
    numbers = [int(x) for x in input_string.split()]
    
    count = 0
    total_sum = 0
    
    minimum = numbers[0]
    maximum = numbers[0]
    
    for num in numbers:
        count += 1
        total_sum += num
        
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
            
    average = total_sum / count if count > 0 else 0.00
    
    print(f"Количество: {count}")
    print(f"Сумма: {total_sum}")
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Среднее: {average:.2f}")

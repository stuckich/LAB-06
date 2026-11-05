# transform.py
input_string = input("Введите целые числа через пробел: ").strip()

# Корректно обрабатываем пустой ввод
if not input_string:
    original_list = []
    transformed_list = []
else:
    original_list = [int(x) for x in input_string.split()]
    
    # Создаем новый список, используя тернарный оператор (или функцию abs())
    transformed_list = [num if num >= 0 else -num for num in original_list]

print("Исходный список:", original_list)
print("Новый список:   ", transformed_list)

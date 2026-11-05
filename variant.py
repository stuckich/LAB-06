import sys

def main():
    line = input("Введите целые числа через пробел: ")
    
    try:
        numbers = [int(x) for x in line.split()]
    except ValueError:
        print("Ошибка: Введены не только целые числа.")
        return

    result = [num for num in numbers if num > 0 and num % 2 == 0]

    count = len(result)
    total_sum = sum(result)
    sorted_result = sorted(result)

    print(f"Список в исходном порядке: {result}")
    print(f"Количество элементов: {count}")
    print(f"Сумма элементов: {total_sum}")
    print(f"Отсортированная структура: {sorted_result}")

if __name__ == "__main__":
    main()

import math

def calculate_factorial(n: int) -> int:
    return math.factorial(n)

def get_positive_integer() -> int:
    while True:
        user_input = input("Введите положительное целое число: ")
        try:
            number = int(user_input)
            if number <= 0:
                print("Ошибка: число должно быть положительным (больше 0). Попробуйте снова.")
                continue
            return number
        except ValueError:
            print("Ошибка: вы ввели нечисловое значение. Пожалуйста, введите целое число.")

def main():
    number = get_positive_integer()
    result = calculate_factorial(number)
    print(f"Факториал числа {number} равен: {result}")

if __name__ == "__main__":
    main()

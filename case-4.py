import random

def get_valid_guess(min_val: int, max_val: int) -> int:
    """Запрашивает у пользователя целое число в заданном диапазоне с обработкой ошибок."""
    while True:
        user_input = input(f"Введите целое число от {min_val} до {max_val}: ")
        try:
            guess = int(user_input)
            if min_val <= guess <= max_val:
                return guess
            else:
                print(f"Число должно быть в диапазоне от {min_val} до {max_val}. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введено нечисловое значение. Пожалуйста, введите целое число.")

def play_guess_number():
    min_val, max_val = 1, 100
    secret_number = random.randint(min_val, max_val)
    max_attempts = 7
    attempts = 0

    print("Добро пожаловать в игру «Угадай число»!")
    print(f"Я загадал число от {min_val} до {max_val}. У вас есть {max_attempts} попыток.")

    while attempts < max_attempts:
        guess = get_valid_guess(min_val, max_val)
        attempts += 1
        remaining = max_attempts - attempts

        if guess == secret_number:
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
            return
        elif guess < secret_number:
            print("Слишком маленькое число.")
        else:
            print("Слишком большое число.")

        if remaining > 0:
            print(f"Осталось попыток: {remaining}")
        else:
            print(f"Попытки закончились. Загаданное число было: {secret_number}")

def main():
    play_guess_number()

if __name__ == "__main__":
    main()

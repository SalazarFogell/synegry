import random

def get_valid_number(min_val: int, max_val: int) -> int:
    while True:
        user_input = input(f"Введите целое число от {min_val} до {max_val}: ")
        try:
            number = int(user_input)
            if min_val <= number <= max_val:
                return number
            else:
                print(f"Число должно быть в диапазоне от {min_val} до {max_val}. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введено нечисловое значение. Пожалуйста, введите целое число.")

def play_game():
    min_val, max_val = 1, 100
    secret_number = random.randint(min_val, max_val)
    max_attempts = 7
    attempts = 0

    print("Добро пожаловать в игру «Угадай число»!")
    print(f"Я загадал число от {min_val} до {max_val}. У вас есть {max_attempts} попыток.")

    while attempts < max_attempts:
        guess = get_valid_number(min_val, max_val)
        attempts += 1
        remaining = max_attempts - attempts

        if guess == secret_number:
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
            return True
        elif guess < secret_number:
            print("Слишком маленькое число.")
        else:
            print("Слишком большое число.")

        if attempts == 4:
            # Доп. подсказка что бы уже точно победить
            low_hint = max(min_val, secret_number - 10)
            high_hint = min(max_val, secret_number + 10)
            print(f"Подсказка: число находится между {low_hint} и {high_hint}.")

        if remaining > 0:
            print(f"Осталось попыток: {remaining}")
        else:
            print(f"Попытки закончились. Загаданное число было: {secret_number}")
            return False

def main():
    while True:
        play_game()
        again = input("Хотите сыграть ещё раз? (да/нет): ").strip().lower()
        if again not in ("да", "д", "yes", "y"):
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    main()

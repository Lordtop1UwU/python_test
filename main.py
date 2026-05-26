import random
import time

def math_trainer():
    print("Добро пожаловать в тренажёр таблицы умножения!")
    print("Для выхода введите 'q'")
    print("-" * 40)

    # Инициализация статистики
    correct_answers = 0
    total_questions = 0
    response_times = []

    while True:
        # Генерация чисел для умножения (от 1 до 10)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 * num2

        # Фиксируем значение времени в момент начала тренировки
        start_time = time.time()

        # Вывод примера на экран игрока
        player_input = input(f"{num1} × {num2} = ")

        # Если игрок нажал q - выходим из программы.
        if player_input.lower() == 'q':
            break

        # Потраченое время
        end_time = time.time()
        response_time = end_time - start_time
        response_times.append(response_time)


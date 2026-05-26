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

        # Проверка ответа
        try:
            player_answer = int(player_input)
            total_questions += 1

            # Проверка правильности ответа
            if player_answer == correct_answer:
                print("Правильно!")
                correct_answers += 1
            else:
                print(f"Неверно. Правильный ответ: {correct_answer}")
        except ValueError:
            print("Пожалуйста, введите число или 'q' для выхода")
            continue

        print(f"Время ответа: {response_time:.2f} сек")
        print("-" * 20)

    # Вывод итоговой статистики

        accuracy = (correct_answers / total_questions) * 100
        average_time = sum(response_times) / len(response_times)

        print("=" * 40)
        print("ИТОГИ ТРЕНИРОВКИ:")
        print(f"Всего примеров: {total_questions}")
        print(f"Правильных ответов: {correct_answers}")
        print(f"Ошибок: {total_questions - correct_answers}")


# Запуск программы
if __name__ == "__main__":
    math_trainer()
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.menu import (
    print_header,
    show_main_menu,
    show_category_menu,
    get_category_name,
    show_question,
    get_user_answer,
    is_close_match,
    show_result,
    show_session_statistics,
    save_log,
    show_statistics_from_log
)
from modules.timer import SessionTimer

TEST_QUESTIONS = {
    "однокоренные": [
        {"question": "Какое слово является однокоренным к слову 'вода'?", "correct": "водный"},
        {"question": "Какое слово однокоренное к слову 'лес'?", "correct": "лесной"},
        {"question": "Какое слово однокоренное к слову 'дом'?", "correct": "домик"}
    ],
    "антонимы": [
        {"question": "Антоним к слову 'холодный'?", "correct": "горячий"},
        {"question": "Антоним к слову 'высокий'?", "correct": "низкий"},
        {"question": "Антоним к слову 'добрый'?", "correct": "злой"}
    ],
    "синонимы": [
        {"question": "Синоним к слову 'красивый'?", "correct": "прекрасный"},
        {"question": "Синоним к слову 'быстрый'?", "correct": "скорый"},
        {"question": "Синоним к слову 'умный'?", "correct": "разумный"}
    ]
}


def run_training_session(category_choice):
    category_name = get_category_name(category_choice)
    print(f"\nНачинаем тренировку по теме: {category_name.upper()}")

    questions = TEST_QUESTIONS.get(category_name, [])
    if not questions:
        print("Вопросы для этой категории не найдены!")
        return

    total_questions = len(questions)
    correct_count = 0

    timer = SessionTimer()
    timer.start()

    for i, q in enumerate(questions, 1):
        show_question(q["question"], i, total_questions)
        user_answer = get_user_answer()

        is_correct = is_close_match(user_answer, q["correct"])

        if is_correct:
            correct_count += 1

        show_result(is_correct, q["correct"])

    timer.stop()
    elapsed_time = timer.get_elapsed_time()

    percentage = (correct_count / total_questions) * 100

    show_session_statistics(correct_count, total_questions, percentage, elapsed_time)

    log_data = (f"{timer.get_formatted_date()} | Категория: {category_name} | "
                f"Правильных: {correct_count}/{total_questions} | "
                f"{percentage:.1f}% | Время: {elapsed_time}")
    save_log("training_log.txt", log_data)


def main():
    print_header()

    while True:
        choice = show_main_menu()

        if choice == "1":
            category = show_category_menu()
            run_training_session(category)
            input("\nНажмите Enter, чтобы продолжить...")

        elif choice == "2":
            show_statistics_from_log("training_log.txt")
            input("\nНажмите Enter, чтобы продолжить...")

        elif choice == "3":
            print("\nСпасибо за тренировку! До свидания!")
            break


if __name__ == "__main__":
    main()
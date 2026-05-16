
# Тренажёр словообразования
# Точка входа в программу

# Интегрирует:
# word_bank.py (база слов от аналитика)
# task_generator.py (генерация заданий от аналитика)
# menu.py (интерфейс от UI/тестировщика)
# timer.py (таймер от UI/тестировщика)

import sys
from modules.word_bank import get_words_for_category, check_answer, calculate_score
from modules.task_generator import get_random_questions, get_question_count
from modules.menu import (
    print_header,
    show_main_menu,
    show_category_menu,
    get_category_name,
    show_question,
    get_user_answer,
    show_result,
    show_session_statistics,
    save_log,
    show_statistics_from_log
)
from modules.timer import SessionTimer


def run_training_session(category_choice):
    # Запускает тренировку в выбранной категории
    # Аргументы:  category_choice (str): выбор пользователя ("1", "2" или "3")

    # Получаем название категории из выбора
    category_name = get_category_name(category_choice)

    if not category_name:
        print("\n⚠️ Ошибка: неверный выбор категории!")
        return

    print(f"\n🎯 Начинаем тренировку по теме: {category_name.upper()}")

    # Проверяем, есть ли вопросы в этой категории
    questions_count = get_question_count(category_name)
    if questions_count == 0:
        print(f"\n⚠️ В категории '{category_name}' пока нет слов для тренировки!")
        print("   Добавьте слова в базу данных (modules/word_bank.py)")
        return

    print(f"📚 Доступно вопросов: {questions_count}")

    # Генерируем вопросы (максимум 5, но не больше, чем есть)
    num_questions = min(5, questions_count)
    questions = get_random_questions(category_name, num_questions)

    if not questions:
        print("\n⚠️ Ошибка: не удалось сгенерировать вопросы!")
        return

    total_questions = len(questions)
    correct_count = 0

    # Запускаем таймер
    timer = SessionTimer()
    timer.start()

    # Проходим по всем вопросам
    for i, (word, question_text, correct_options) in enumerate(questions, 1):
        # Показываем вопрос
        show_question(question_text, i, total_questions)

        # Получаем ответ пользователя
        user_answer = get_user_answer()

        # Проверяем ответ (используем модуль аналитика)
        is_correct = check_answer(word, user_answer, category_name)

        # Форматируем правильный ответ для показа (первые 3 варианта)
        correct_display = ", ".join(correct_options[:3])
        if len(correct_options) > 3:
            correct_display += "..."

        # Показываем результат
        show_result(is_correct, correct_display)

        if is_correct:
            correct_count += 1

        print()  # Пустая строка для разделения вопросов

    # Останавливаем таймер
    timer.stop()
    elapsed_time = timer.get_elapsed_time()

    # Рассчитываем процент правильных ответов
    percentage = calculate_score(correct_count, total_questions)

    # Показываем статистику сессии
    show_session_statistics(correct_count, total_questions, percentage, elapsed_time)

    # Сохраняем результаты в лог
    log_data = (f"{timer.get_formatted_date()} | Категория: {category_name} | "
                f"Правильных: {correct_count}/{total_questions} | "
                f"{percentage:.1f}% | Время: {elapsed_time}")
    save_log("training_log.txt", log_data)


def main():
    # Главная функция программы
    # Управляет циклом меню и навигацией

    # Показываем заголовок программы
    print_header()

    # Основной цикл программы
    while True:
        # Показываем главное меню и получаем выбор
        choice = show_main_menu()

        if choice == "1":
            # Начать тренировку
            category_choice = show_category_menu()
            run_training_session(category_choice)
            input("\nНажмите Enter, чтобы продолжить...")

        elif choice == "2":
            # Показать статистику
            show_statistics_from_log("training_log.txt")
            input("\nНажмите Enter, чтобы продолжить...")

        elif choice == "3":
            # Выйти из программы
            print("\n👋 Спасибо за тренировку! До свидания!")
            save_log("training_log.txt", f"[{SessionTimer().get_formatted_date()}] ПРОГРАММА ЗАВЕРШЕНА")
            sys.exit(0)

        else:
            # Этот случай не должен произойти, так как show_main_menu уже проверяет ввод
            print("\n⚠️ Неверный выбор!")


# Точка входа в программу
if __name__ == "__main__":
    main()
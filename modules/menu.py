import datetime

def print_header():
    print("=" * 50)
    print("     ТРЕНАЖЁР СЛОВООБРАЗОВАНИЯ v1.0")
    print(f"     Время запуска: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    print("=" * 50)

def show_main_menu():
    print("\nГЛАВНОЕ МЕНЮ:")
    print("1. Начать тренировку")
    print("2. Показать статистику")
    print("3. Выйти")
    
    while True:
        choice = input("\nВыберите действие (1-3): ").strip()
        if choice == "1":
            return "1"
        elif choice == "2":
            return "2"
        elif choice == "3":
            return "3"
        print("Ошибка: введите 1, 2 или 3")

def show_category_menu():
    print("\nВЫБЕРИТЕ КАТЕГОРИЮ:")
    print("1. Однокоренные слова")
    print("2. Антонимы")
    print("3. Синонимы")
    
    while True:
        choice = input("\nВаш выбор (1-3): ").strip()
        if choice == "1":
            return "1"
        elif choice == "2":
            return "2"
        elif choice == "3":
            return "3"
        print("Ошибка: введите 1, 2 или 3")

def get_category_name(choice):
    categories = {
        "1": "однокоренные",
        "2": "антонимы",
        "3": "синонимы"
    }
    return categories.get(choice, "")

def show_question(question_text, question_num, total):
    print(f"\nВопрос {question_num}/{total}")
    print("-" * 40)
    print(question_text)
    print("-" * 40)

def get_user_answer():
    answer = input("Ваш ответ: ").strip()
    if answer == "":
        print("Вы ничего не ввели. Попробуйте ещё раз.")
        return get_user_answer()
    return answer

def is_close_match(user_answer, correct_answer):
    user_answer = user_answer.lower().strip()
    correct_answer = correct_answer.lower().strip()
    
    if user_answer == correct_answer:
        return True
    
    if abs(len(user_answer) - len(correct_answer)) > 1:
        return False
    
    differences = 0
    min_length = min(len(user_answer), len(correct_answer))
    
    for i in range(min_length):
        if user_answer[i] != correct_answer[i]:
            differences += 1
    
    differences += abs(len(user_answer) - len(correct_answer))
    return differences <= 1

def show_result(is_correct, correct_answer=""):
    if is_correct:
        print("ПРАВИЛЬНО! Молодец!")
    else:
        if correct_answer:
            print(f"НЕПРАВИЛЬНО. Правильный ответ: {correct_answer}")
        else:
            print("НЕПРАВИЛЬНО. Попробуйте ещё раз!")

def show_session_statistics(correct, total, percentage, elapsed_time):
    print("\n" + "=" * 50)
    print("СТАТИСТИКА СЕССИИ:")
    print(f"   Правильных ответов: {correct}/{total}")
    print(f"   Процент правильных: {percentage:.1f}%")
    print(f"   Время тренировки: {elapsed_time}")
    
    print("\nОЦЕНКА:")
    if percentage >= 80:
        print("   ОТЛИЧНО!")
    elif percentage >= 60:
        print("   ХОРОШО!")
    else:
        print("   НУЖНО ЕЩЁ ПОТРЕНИРОВАТЬСЯ!")
    print("=" * 50)

def save_log(filename, data):
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(data + "\n")
        print(f"Результат сохранён в файл: {filename}")
    except Exception as e:
        print(f"Ошибка сохранения лога: {e}")

def show_statistics_from_log(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if not lines:
            print("\nСтатистика пока пуста. Пройдите хотя бы одну тренировку.")
            return
        
        print("\n" + "=" * 50)
        print("ИСТОРИЯ ТРЕНИРОВОК:")
        print("=" * 50)
        
        for line in lines:
            print(line.strip())
        
        print("=" * 50)
        
    except FileNotFoundError:
        print("\nФайл статистики не найден. Пройдите тренировку, чтобы создать его.")
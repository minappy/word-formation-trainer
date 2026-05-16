# Модуль для генерации заданий
# Случайным образом выбирает слова из базы и формирует вопросы


import random
from modules.word_bank import get_words_for_category


def generate_question(word, category):
    # Генерирует текст вопроса для пользователя
    category_ru = {
        "однокоренные": "однокоренных слов",
        "антонимы": "антонимов",
        "синонимы": "синонимов"
    }
    return f"К слову '{word}' подберите {category_ru.get(category, category)} (через запятую):"


def get_random_questions(category, count=5):
    # Возвращает список случайных вопросов с ответами
    words_dict = get_words_for_category(category)
    
    if len(words_dict) < count:
        count = len(words_dict)
    
    if count == 0:
        return []
    
    # Выбираем случайные слова
    selected_words = random.sample(list(words_dict.keys()), count)
    
    questions = []
    for word in selected_words:
        question_text = generate_question(word, category)
        correct_options = words_dict[word]
        questions.append((word, question_text, correct_options))
    
    return questions


def get_question_count(category):
    # Возвращает количество доступных вопросов для категории
    words_dict = get_words_for_category(category)
    return len(words_dict)
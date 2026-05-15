"""
Модули тренажёра словообразования
"""

from .word_bank import (
    WORD_CATEGORIES, 
    get_categories, 
    get_words_for_category, 
    check_answer, 
    calculate_score
)
from .task_generator import (
    generate_question, 
    get_random_questions, 
    get_question_count
)

__all__ = [
    'WORD_CATEGORIES',
    'get_categories',
    'get_words_for_category',
    'check_answer',
    'calculate_score',
    'generate_question',
    'get_random_questions',
    'get_question_count'
]
# Модуль таймера для отслеживания времени тренировки


import datetime


class SessionTimer:
    # Класс для измерения времени тренировочной сессии

    def __init__(self):
        # Инициализация таймера
        self.start_time = None
        self.end_time = None

    def start(self):
        # Запускает таймер (запоминает время начала)
        self.start_time = datetime.datetime.now()
        self.end_time = None
        print("⏱️ Таймер запущен!")

    def stop(self):
        # Останавливает таймер (запоминает время окончания)
        if self.start_time:
            self.end_time = datetime.datetime.now()
            print("⏱️ Таймер остановлен!")
        else:
            print("⚠️ Таймер не был запущен!")

    def get_elapsed_time(self):
        # Возвращает прошедшее время в формате ММ:СС
        # Возвращает: str - время в формате "ММ:СС" или "00:00" если таймер не запущен

        if not self.start_time:
            return "00:00"

        end = self.end_time if self.end_time else datetime.datetime.now()
        delta = end - self.start_time

        minutes = delta.seconds // 60
        seconds = delta.seconds % 60

        return f"{minutes:02d}:{seconds:02d}"

    def get_elapsed_seconds(self):
        # Возвращает прошедшее время в секундах
        # Возвращает: int - количество секунд или 0 если таймер не запущен

        if not self.start_time:
            return 0

        end = self.end_time if self.end_time else datetime.datetime.now()
        delta = end - self.start_time

        return delta.seconds

    def reset(self):
        # Сбрасывает таймер
        self.start_time = None
        self.end_time = None
        print("🔄 Таймер сброшен")

    def get_formatted_date(self):
        # Возвращает текущую дату для лога
        # Возвращает: str - дата и время в формате "ДД.ММ.ГГГГ ЧЧ:ММ:СС"

        return datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

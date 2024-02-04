from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from random import randint, shuffle

new_quest_templ = 'Нове питання'  # Зразок нового питання
new_answer_templ = 'Нова відповідь'  # Зразок нової відповіді

text_wrong = 'Невірно'  # Текст для неправильної відповіді
text_correct = 'Вірно'  # Текст для правильної відповіді

import re
from docx import Document

# Открываем файл Word
doc = Document(r'c:\Pet_project\Шаблонер\src\ПримерТест.docx')

# Инициализируем пустой список для хранения извлеченных значений
values = []

# Проходим по всем абзацам документа
for paragraph in doc.paragraphs:
    # Извлекаем текст из абзаца
    text = paragraph.text
    # Ищем все значения между #$ и $#
    matches = re.findall(r'#\$(.*?)\$#', text)
    # Добавляем найденные значения в список
    values.extend(matches)

# Получаем уникальные значения из списка
unique_values = list(set(values))

# Выводим уникальные значения
print(unique_values)

#########################################

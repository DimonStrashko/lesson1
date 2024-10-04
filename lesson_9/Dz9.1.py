import re

def popular_words(text: str, words: list) -> dict:
    # Приводимо текст до нижнього регістру
    text_lower = text.lower()

    # Створюємо словник з кількістю входжень кожного шуканого слова, використовуючи регулярні вирази для пошуку цілих слів
    word_count = {word: len(re.findall(r'\b' + re.escape(word) + r'\b', text_lower)) for word in words}

    return word_count

# Тест
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

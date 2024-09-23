def correct_sentence(text):
    # Розділяємо текст на речення
    sentences = text.split('.')

    # Виправляємо кожне речення
    corrected_sentences = []
    for sentence in sentences:
        # Видаляємо пробіли в кінці і на початку
        sentence = sentence.strip()
        if not sentence:
            continue  # Пропускаємо порожні речення
        # Змінюємо першу букву на велику
        corrected_sentence = sentence[0].upper() + sentence[1:]
        # Додаємо крапку, якщо речення не закінчується на крапку
        if not corrected_sentence.endswith('.'):
            corrected_sentence += '.'
        corrected_sentences.append(corrected_sentence)

    # Об'єднуємо речення в один рядок
    return ' '.join(corrected_sentences)


# Тестування функції
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')

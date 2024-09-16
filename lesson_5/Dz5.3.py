# 'Python Community'
# 'i like python community!'
# 'Should, I. subscribe? Yes!'
s = input('Рядок:')

# Видалити всі символи пунктуації та пробіли
cleaned = ''.join(c for c in s if c.isalnum() or c.isspace())

# Розділити рядок на слова і перетворити їх у форматі "Title Case"
words = []
word = ''
for c in cleaned:
    if c.isalpha():  # Перевіряємо, чи є символ літерою
        word += c  # Додаємо літеру до поточного слова
    elif c.isspace():  # Перевіряємо, чи є символ пробілом
        if word:  # Якщо поточне слово не пусте
            words.append(word.capitalize())  # Додаємо слово до списку з великою літерою на початку
            word = ''  # Очищаємо змінну для нового слова
# Додаємо останнє слово, якщо воно не пусте
if word:
    words.append(word.capitalize())

# Створити хештег
hashtag = '#' + ''.join(words)

# Переконатися, що довжина хештегу не перевищує 140 символів
if len(hashtag) > 140:
    hashtag = hashtag[:140]

# Вивести результат
print(hashtag)
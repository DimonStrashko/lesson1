def is_palindrome(text):
    # Создаём пустую строку для очищенной версии текста
    cleaned = ''

    # Проходим по каждому символу в исходном тексте
    for char in text:
        # Проверяем, является ли символ буквой или цифрой
        if char.isalnum():
            # Приводим символ к нижнему регистру и добавляем к очищенной строке
            cleaned += char.lower()

    # Проверяем, является ли очищенная строка палиндромом
    return cleaned == cleaned[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")


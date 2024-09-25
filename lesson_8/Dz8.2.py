def is_palindrome(text):
    # Видаляємо всі пробіли з рядка
    cleaned= text.replace(" ", "")
    # Перетворюємо всі символи до нижнього регістру
    cleaned = cleaned.lower()
    # Перевіряємо, чи дорівнює рядок своєму оберненому варіанту
    return cleaned == cleaned[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
from inspect import isgenerator  # Імпортуємо isgenerator

def some_gen(begin, end, func):
    current = begin
    for _ in range(end):
        yield current
        current = func(current)  # Оновлюємо значення на основі функції


# Перевіряємо тест
def pow(x):
    return x ** 2

# Генератор
gen = some_gen(2, 4, pow)

# Тести
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

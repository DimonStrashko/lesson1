def difference(*args) -> float:
    # Якщо аргументів немає, повертаємо 0
    if not args:
        return 0

    # Обчислюємо різницю між максимумом і мінімумом
    return round(max(args) - min(args), 2)


# Тести
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

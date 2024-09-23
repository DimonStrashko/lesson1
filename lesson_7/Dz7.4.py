def common_elements():
    # Генеруємо множину чисел кратних 3
    kratno_3 = {i for i in range(100) if i % 3 == 0}
    # Генеруємо множину чисел кратних 5
    kratno_5 = {i for i in range(100) if i % 5 == 0}

    # Знаходимо перетин обох множин
    intersection_set = kratno_3.intersection(kratno_5)

    return intersection_set


otvet = common_elements()
print(otvet)

# Тестування функції
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
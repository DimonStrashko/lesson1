def add_one(some_list):
    # 1. Перетворюємо список цифр у рядок і потім у число
    number = int(''.join(map(str, some_list)))

    # 2. Додаємо 1 до отриманого числа
    number += 1

    # 3. Перетворюємо число назад у список цифр і повертаємо результат
    return [int(digit) for digit in str(number)]

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

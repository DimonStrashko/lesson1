 Запитуємо у користувача 4-х значне число
number = int(input("Введіть 4-х значне число: "))
 # Отримуємо кожну цифру числа
thousands, remainder = divmod(number, 1000)
# тисячі
hundreds, remainder = divmod(remainder, 100)
# сотні
tens, ones = divmod(remainder, 10)
# десятки і одиниці

    # Виводимо цифри в стовпчику
print(thousands)
print(hundreds)
print(tens)
print(ones)
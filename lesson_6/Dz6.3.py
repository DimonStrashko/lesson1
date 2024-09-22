# Запит на введення користувача
user_input = input("Введіть ціле число: ")

# Перетворення введеного рядка на число
number = int(user_input)

while number > 9:
    product = 1  # Початкове значення добутку
    # Перемноження всіх цифр числа
    for digit in str(number):
        product *= int(digit)
    number = product  # Оновлюємо число на добуток

# Виведення результату
print("Результат:", number)

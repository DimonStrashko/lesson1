# Введення першого числа
num1 = float(input("Введіть перше число: "))

# Введення оператора
operator = input("Введіть оператор (+, -, *, /): ")

# Введення другого числа
num2 = float(input("Введіть друге число: "))

# Виконання відповідної операції
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Помилка: ділення на нуль!")
        result = None  # Встановлюємо result в None для уникнення помилки при виведенні
    else:
        result = num1 / num2

# Виведення результату
if result is not None:
    print(f"Результат: {result}")

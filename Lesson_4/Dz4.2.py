# [1, 3, 5]
test = [6]
#  []
if not test:
    print(0)  # Для порожнього списку результат завжди 0
else:
    r = 0
    for i in range(0, len(test), 2):  # Ітеруємо через парні індекси
        r += test[i]  # Додаємо значення елемента з парним індексом
        last = test[-1]
        result = r * last
        print(result)
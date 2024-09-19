import string
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA
# Введіть рядок у форматі "літера-літера"
x = input("введення через дефіс дві літери:")

# Розділімо рядок за дефісом
start, end = x.split('-')

# Знайдемо індекси літер
start_index = string.ascii_letters.index(start)
end_index = string.ascii_letters.index(end)

# Виріжемо потрібний діапазон
result = string.ascii_letters[start_index:end_index + 1]

# Виведемо результат
print(result)

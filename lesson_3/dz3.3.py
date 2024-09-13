# [1, 2, 3, 4, 5, 6]
# [1, 2, 3]
# [1, 2, 3, 4, 5]
test = [1]
#  []

# Визначаємо довжину вхідного списку
x = len(test)

# Якщо вхідний список порожній, повертаємо список із двох порожніх списків
if x == 0:
    print([[], []])
else:
    middle = (x+1) // 2
    first = test[:middle]
    second = test[middle:]
    print([first, second])





# Запит на введення користувача
user = int(input("Введіть кількість секунд (0 - 8639999): "))
 # Перевірка введеного значення
if user_input < 0 or user_input >= 8640000:
    print("Число повинно бути від 0 до 8639999.")
else:
        # Визначення кількості днів, годин, хвилин та секунд
        days, remainder = divmod(user, 86400)  # 1 день = 86400 секунд
        hours, remainder = divmod(remainder, 3600)   # 1 година = 3600 секунд
        minutes, seconds = divmod(remainder, 60)      # 1 хвилина = 60 секунд
        # Визначення правильного відмінка слова "день"
        if days == 1:
            day_str = "день"
        elif 2 <= days <= 4:
            day_str = "дні"
        else:
            day_str = "днів"

        # Форматування значень з ведучими нулями
        formatted_time = f"{days} {day_str}, {hours:02}:{minutes:02}:{seconds:02}"
        print(formatted_time)



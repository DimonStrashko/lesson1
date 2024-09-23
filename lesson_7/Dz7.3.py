def second_index(text, some_str):
    # Знайдемо перше входження
    first_index = text.find(some_str)

    # Якщо першого входження немає, повертаємо None
    if first_index == -1:
        return None

    # Знайдемо друге входження, починаючи з індексу після першого входження
    second_index = text.find(some_str, first_index + len(some_str))

    return second_index if second_index != -1 else None


# Тести
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')

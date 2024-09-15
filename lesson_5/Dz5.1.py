import keyword
import string
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True
# Введення рядка користувачем
name = input("Введіть рядок: ")

# Перевірка, чи рядок не починається з цифри
if name[0].isdigit():
    print(False)
else:
    # Неприпустимі символи: пробіли і знаки пунктуації (крім нижнього підкреслення)
    invalid_chars = set(string.whitespace + string.punctuation) - {'_'}

    # Перевірка, чи рядок містить неприпустимі символи
    if any(c in invalid_chars for c in name):
        print(False)
    elif any(c.isupper() for c in name):
        # Перевірка, чи рядок не містить великі літери
        print(False)
    elif name in keyword.kwlist:
        # Перевірка, чи рядок не є зареєстрованим словом
        print(False)
    elif name.count('_') > 1:
        # Перевірка кількості нижніх підкреслень
        print(False)
    else:
        print(True)

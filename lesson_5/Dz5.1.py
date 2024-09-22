import keyword
import string

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
        # Перевірка, чи рядок не є зарезервованим словом
        print(False)
    else:
        # Перевірка наявності символів поряд із нижнім підкресленням
        underscores_count = name.count('_')
        valid = True

        if underscores_count > 1:
            for i in range(len(name)):
                if name[i] == '_':
                    # Перевірка, чи є символи з обох боків
                    if (i == 0 or i == len(name) - 1 or not name[i - 1].isalpha() or not name[i + 1].isalpha()):
                        valid = False
                        break
        elif underscores_count == 1:
            # Якщо лише одне `_`, рядок вважається дійсним
            valid = True

        print(valid)

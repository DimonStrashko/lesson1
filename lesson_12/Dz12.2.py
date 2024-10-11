class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price} USD, description: {self.description}, dimensions: {self.dimensions}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"User: {self.name} {self.surname}, Phone: {self.numberphone}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def get_total(self):
        total = sum(item.price * cnt for item, cnt in self.products.items())
        return total

    def __str__(self):
        items_str = "\n".join(f"{item.name}: {cnt} pcs." for item, cnt in self.products.items())
        return f"{self.user}\nItems:\n{items_str}\nTotal: {self.get_total()} USD"


# Створимо товари
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

# Перевірка виведення товарів
print(lemon)  # lemon, price: 5
print(apple)  # apple, price: 2

# Створимо користувача
buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

# Створимо кошик і додамо товари
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
Total: 60 USD
"""

# Перевірка обчислення загальної вартості
assert cart.get_total() == 60, "Всього 60"

# Змінимо кількість яблук
cart.add_item(apple, -10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
Total: 40 USD
"""

assert cart.get_total() == 40

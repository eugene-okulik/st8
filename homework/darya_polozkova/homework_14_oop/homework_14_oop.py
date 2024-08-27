class Flowers:

    def __init__(self, color, size, amount, lifetime, price):
        self.color = color
        self.size = size
        self.amount = amount
        self.lifetime = lifetime
        self.price = price

    def __str__(self):
        return f"This is a class: cost: {self. price}$, size: {self.size}, lifetime: {self.lifetime} days"


class Roses(Flowers):
    def __init__(self, color, size, amount, lifetime, price, name):
        super().__init__(color, size, amount, lifetime, price)
        self.name = name

    def __str__(self):
        return f"Flower: {self.name}, cost: {self. price}$, size: {self.size}, lifetime: {self.lifetime} days"


class Tulips(Flowers):
    def __init__(self, color, size, amount, lifetime, price, name):
        super().__init__(color, size, amount, lifetime, price)
        self.name = name

    def __str__(self):
        return f"Flower: {self.name}, cost: {self. price}$, size: {self.size}, lifetime: {self.lifetime} days"


class Orchids(Flowers):
    def __init__(self, color, size, amount, lifetime, price, name):
        super().__init__(color, size, amount, lifetime, price)
        self.name = name

    def __str__(self):
        return f"Flower: {self.name}, cost: {self. price}$, size: {self.size}, lifetime: {self.lifetime} days"


class Bouquet:
    def __init__(self):
        self.bouquet = []

    def add_flower(self, flower):
        self.bouquet.append(flower)

    def avg_lifetime(self):
        return int(sum(flower.lifetime for flower in self.bouquet) / len(self.bouquet))

    def price(self):
        return sum(flower.price for flower in self.bouquet)

    def sorting(self, param):
        if param == 'size':
            self.bouquet.sort(key=lambda x: x.size)
        elif param == 'price':
            self.bouquet.sort(key=lambda x: x.price)
        elif param == 'color':
            self.bouquet.sort(key=lambda x: x.color)
        else:
            print('Try one more time! Non-existing param is detected')
        return self.bouquet

    def find_by_max_price(self):
        max_price = max(self.bouquet, key=lambda x: x.price)
        return f'The most expensive flower costs: {max_price}'

    def find_by_max_lifetime(self):
        lifetime = max(self.bouquet, key=lambda x: x.lifetime)
        return f'The longest lifetime has: {lifetime}'

    def __repr__(self):
        return f"Here is your bouquet of {self.bouquet}"


flower_1 = Roses('white', 'medium', 10, 3, 10, 'Alba')
flower_2 = Orchids('purple', 'long', 9, 5, 9, 'Rex')
flower_3 = Tulips('blue', 'small', 11, 7, 7, 'Tulpan')

bouquet = Bouquet()
bouquet.add_flower(flower_1)
bouquet.add_flower(flower_2)
bouquet.add_flower(flower_3)

print(flower_1)
print(flower_2)
print(flower_3)
# Self-check среднее время жизни букета
print(f'You will have this beauty for {bouquet.avg_lifetime()} days')
# Self-check цена букета
print(f'Please pay {bouquet.price()}$ for your bouquet')
print(bouquet.sorting('color'))
print(bouquet.sorting('price'))
print(bouquet.find_by_max_price())
print(bouquet.find_by_max_lifetime())
print(bouquet)

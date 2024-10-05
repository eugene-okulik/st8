class Flowers:
    def __init__(self, color, price, lifeperiod, stem_length) -> None:
        self.color = color
        self.price = price
        self.lifeperiod = lifeperiod
        self.stem_length = stem_length

    def __str__(self):
        return f"Цвет: {self.color}, Цена: {self.price}, Время жизни: {self.lifeperiod} дней, Длина стебля: {self.stem_length} см"


class Rose(Flowers):
    def __init__(self, color, price, lifeperiod, stem_length) -> None:
        super().__init__(color, price, lifeperiod, stem_length)


class Tulip(Flowers):
    def __init__(self, color, price, lifeperiod, stem_length) -> None:
        super().__init__(color, price, lifeperiod, stem_length)


class Orchid(Flowers):
    def __init__(self, color, price, lifeperiod, stem_length) -> None:
        super().__init__(color, price, lifeperiod, stem_length)


class Bouquet():
    def __init__(self) -> None:
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_bouquet(self):
        return sum(flower.price for flower in self.flowers)

    def average_preiod(self):
        total_period = sum(flower.lifeperiod for flower in self.flowers)
        return total_period / len(self.flowers)

    def sort_by(self, parametr):
        if parametr == 'stem_length':
            self.flowers.sort(key=lambda x: x.stem_length)
        elif parametr == 'price':
            self.flowers.sort(key=lambda x: x.price)
        else:
            print('не верный параметр')
        return self.flowers


flower1 = Rose(color='red', price=10, lifeperiod=7, stem_length=30)
flower2 = Tulip(color='blue', price=15, lifeperiod=10, stem_length=40)
flower3 = Orchid(color='white', price=30, lifeperiod=30, stem_length=50)
bouquet1 = Bouquet()
bouquet1.add_flower(flower1)
bouquet1.add_flower(flower2)
bouquet1.add_flower(flower3)

print(f'Стоимость букета: {bouquet1.calculate_bouquet()}')
print(f'Среднее время увядания букета: {bouquet1.average_preiod()}')
sorted_flowers = bouquet1.sort_by('stem_length')
for flower in sorted_flowers:
    print(flower)

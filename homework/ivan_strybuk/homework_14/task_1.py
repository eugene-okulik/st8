class Flowers:
    """
    name = "Название"
    color = "Цвет цветка"
    freshness = "Cвежесть цветка"
    stem_length_cm = "стебель длина"
    cost = "стоимость"
    life_time_in_days = "жизни_время"
    smell = "запах"
    """

    smell = True

    def __init__(self, name, color, freshness, stem_length_cm: int, cost: int, life_time_in_days):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length_cm = stem_length_cm
        self.cost = cost
        self.life_time_in_days = life_time_in_days


class FlowersHolland(Flowers):

    def __init__(self, name, color, freshness, stem_length_cm: int, cost: int, life_time_in_days: int):
        super().__init__(name, color, freshness, stem_length_cm, cost, life_time_in_days)


class FlowersBelarus(Flowers):

    def __init__(self, name, color, stem_length_cm: int, cost: int, life_time_in_days: int, freshness="average"):
        super().__init__(name, color, freshness, stem_length_cm, cost, life_time_in_days)


class Bouquet:
    def __init__(self):
        self.l_flower = []

    def add_flower(self, element):
        self.l_flower.append(element)

    def avg_life_time(self):
        total_time = sum([flower.life_time_in_days for flower in self.l_flower])
        return total_time / len(self.l_flower)

    def sort(self, key):
        self.l_flower.sort(key=lambda x: getattr(x, key))

    def search(self, key, value):
        return [flower for flower in self.l_flower if getattr(flower, key) == value]


# Создание экземпляров цветов
first_flower = FlowersHolland("tulip", "red", "fresh", 15, 3, 5)
second_flower = FlowersHolland("orchid", "blue", "average", 20, 20, 10)
third_flower = FlowersHolland("red rose", "red", "fresh", 30, 15, 5)
fourth_flower = FlowersHolland("white rose", "white", "fresh", 10, 5, 5)

first_flower_BY = FlowersBelarus("red rose", "red", 20, 10, 3)
second_flower_BY = FlowersBelarus("white rose", "white", 20, 10, 3)
third_flower_BY = FlowersBelarus("tulip", "orange/white", 10, 22, 3)
fourth_flower_BY = FlowersBelarus("aster", "blue/red", 30, 15, 5)

# Создание букета
list_flowers = [first_flower, second_flower]  # пока не понял как это работает =)

bouquet = Bouquet()
bouquet.add_flower(first_flower)
bouquet.add_flower(second_flower)
bouquet.add_flower(third_flower_BY)
bouquet.add_flower(fourth_flower_BY)

avg_life = int(bouquet.avg_life_time())
print(f"Среднее время увядания букета: {avg_life} дней.")
bouquet.sort("cost")
print("Цветы в букете отсортированы по цене:", [flower.name for flower in bouquet.l_flower])
yellow_color = bouquet.search("life_time_in_days", avg_life)
print(f"Цветы в букете со средними временем увядания {avg_life} дней:", [flower.name for flower in yellow_color])

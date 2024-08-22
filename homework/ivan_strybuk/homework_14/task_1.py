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

    def __init__(self, name, color, freshness, stem_length_cm: int, cost: int, life_time_in_days):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length_cm = stem_length_cm
        self.cost = cost
        self.life_time_in_days = life_time_in_days
        self.list_flowers = []

    def add_flower(self, flower):
        self.list_flowers.append(flower)
        return self.list_flowers

    # def fading_time(self):
    #     # Метод, который определяет время увядания по среднему времени жизни всех цветов в букете.
    #     full_life_time = [value for value in self.life_time_in_days]
    #     return round(sum(full_life_time) / len(full_life_time), 2)

    # сортировка
    # def sorting(self):
    #     pass

    # поиск_цветков
    # def search_flowers(self):  # (например, по среднему времени жизни)
    #     pass


# Создание экземпляров цветов
first_flower = FlowersHolland("tulip", "red", "fresh", 15, 3, 5)
second_flower = FlowersHolland("orchid", "blue", "average", 20, 20, 10)
third_flower = FlowersHolland("red rose", "red", "fresh", 30, 15, 5)
fourth_flower = FlowersHolland("white rose", "white", "fresh", 10, 5, 5)

first_flower_BY = FlowersBelarus("red rose", "red", 20, 10, 3, "fresh")
second_flower_BY = FlowersBelarus("white rose", "white", 20, 10, 3)
third_flower_BY = FlowersBelarus("tulip", "orange/white", 10, 2, 3)
fourth_flower_BY = FlowersBelarus("aster", "blue/red", 30, 15, 5, "super fresh")

# Создание букета
bouquet = Bouquet("", "", "", 0, 0, 0)
bouquet.add_flower(first_flower)
bouquet.add_flower(second_flower)
bouquet.add_flower(third_flower)

list_flow = bouquet.list_flowers
print(list_flow)

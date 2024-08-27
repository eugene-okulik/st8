from Rose import Rose
from Carnation import Carnation
from Bouquet import Bouquet


class Main:
    def __init__(self):
        self.flower1 = Rose(name="Китайская роза", color="Красный", smell="Сильный",
                            price=10, stem_length=20, life_time_flow=7)
        self.flower2 = Carnation(name="Обыкновенная", color="Белый", smell="Слабый",
                                 price=5, stem_length=10, life_time_flow=5)
        self.flower3 = Rose(name="Шиповник", color="Розовый", smell="Сильный",
                            price=8, stem_length=15, life_time_flow=8)
        self.flower4 = Carnation(name="Аптечная", color="Белый", smell="Средний",
                                 price=3, stem_length=7, life_time_flow=3)

        self.flower_num = [self.flower1, self.flower2, self.flower3, self.flower4]

    def work_flower(self):
        bouquet = Bouquet(self.flower_num)

        avg_life = int(bouquet.life_time())
        bouquet.sort("price")
        search_key, search_value = "stem_length", 15
        stem_len_flow = bouquet.search(search_key, search_value)
        print(f"Цветы в букете с длинной стебля {search_value} см:", [flowers.name for flowers in stem_len_flow])
        print(f"Среднее время увядания букета: {avg_life} дней.")
        print("Цветы в букете отсортированы по цене:", [flower.name for flower in bouquet.flowers])

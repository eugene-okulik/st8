from typing import List


class Flower:

    def __init__(self, life_time, price, stem_length, color, freshness, name):
        self.life_time = life_time
        self.price = price
        self.stem_length = stem_length
        self.color = color
        self.freshness = freshness
        self.name = name


class Rose(Flower):

    def __init__(self, stem_length, color, freshness):
        super().__init__(10, 50, stem_length, color, freshness, "Roza")


class Romashka(Flower):

    def __init__(self, stem_length, color, freshness):
        super().__init__(7, 30, stem_length, color, freshness, "Romashka")


class Georgin(Flower):

    def __init__(self, stem_length, color, freshness):
        super().__init__(14, 20, stem_length, color, freshness, "Georgin")


class Bouquet:
    def __init__(self):
        self.flowers: List[Flower] = []

    def get_life_time(self):
        total_time = 0
        for one_flower in self.flowers:
            total_time = total_time + one_flower.life_time

        medium = total_time / len(self.flowers)
        return medium

    def add_flower(self, flower: Flower):
        self.flowers.append(flower)
        print(f"Added flower {flower.name} to bucket")

    def get_set_price(self):
        total_price = 0
        for oneFlower in self.flowers:
            total_price = total_price + oneFlower.price

        return total_price

    def sort_by_price(self):
        self.flowers.sort(key=lambda x: x.price)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.freshness)

    def find_with_price_less(self, max_price):
        result_list = []
        for flower in self.flowers:
            if flower.price <= max_price:
                result_list.append(flower)

        return result_list


rose_1 = Rose(17, "red", "4")
rose_2 = Rose(22, "red", "7")
georgin_1 = Georgin(18, "blue", "3")
georgin_2 = Georgin(19, "red", "5")
romashka_1 = Romashka(35, "yellow", "9")

bucket = Bouquet()
bucket.add_flower(rose_1)
bucket.add_flower(georgin_1)
bucket.add_flower(rose_2)
bucket.add_flower(georgin_2)
bucket.add_flower(romashka_1)

print(f"Bucket price: {bucket.get_set_price()}")
print(f"Bucket life time: {bucket.get_life_time()}")

bucket.sort_by_price()
bucket.sort_by_freshness()

for oneFlower in bucket.flowers:
    print(f"Bucket has flower: {oneFlower.name, oneFlower.color, oneFlower.freshness} {oneFlower.price} euro")

found_flowers = bucket.find_with_price_less(30)

for oneFlower in found_flowers:
    print(f"Found flower: {oneFlower.name, oneFlower.color, oneFlower.freshness} {oneFlower.price} euro")

class Bouquet:
    def __init__(self, flowers_bo):
        self.flowers = flowers_bo

    def add_flower(self, flower):
        self.flowers.append(flower)

    def life_time(self):
        total_life = sum([flower.life_time_flow for flower in self.flowers])
        return int(total_life / len(self.flowers))

    def sort(self, key):
        self.flowers.sort(key=lambda x: getattr(x, key))

    def search(self, key, value):
        return [flower for flower in self.flowers if getattr(flower, key) == value]

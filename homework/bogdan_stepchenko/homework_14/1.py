
class Flower:
    def __init__(self, name: str, cost: int, height: int, lifetime: int):
        self.name = name
        self.cost = cost
        self.height = height
        self.lifetime = lifetime

    def __str__(self):
        return f"Flower: {self.name}, cost: {self. cost}, height: {self.height}, lifetime: {self.lifetime}"


class Rose(Flower):
    def __init__(self, cost, height, lifetime, color):
        super().__init__('Rose', cost, height, lifetime)
        self.color = color

    def __str__(self):
        return super().__str__() + f", color: {self.color}"


class Carnation(Flower):
    def __init__(self, cost, height, lifetime, color):
        super().__init__('Carnation', cost, height, lifetime)
        self.color = color

    def __str__(self):
        return super().__str__() + f", color: {self.color}"


class Tulip(Flower):
    def __init__(self, cost, height, lifetime, country):
        super().__init__('Tulip', cost, height, lifetime)
        self.country = country

    def __str__(self):
        return super().__str__() + f", country: {self.country}"


rose_red = Rose(10, 20, 4, 'red')
print(rose_red)

rose_blue = Rose(20, 20, 3, 'blue')
print(rose_blue)

carnation_yellow = Carnation(3, 10, 2, 'yellow')
print(carnation_yellow)

tulip = Tulip(5, 15, 2, 'Belarus')
print(tulip)


class Bouquet:
    def __init__(self):
        self.bouquet = []

    def add_flower(self, flower):
        self.bouquet.append(flower)

    def bouquet_lifetime(self):
        return f"Bouquet lifetime: {sum(flower.lifetime for flower in self.bouquet)/len(self.bouquet)} days"

    def bouquet_cost(self):
        return f"Cost of bouquet: {sum(flower.cost for flower in self.bouquet)} euro"

    def sorting(self, param, reverse=False):
        params = ['cost', 'name', 'lifetime', 'color']

        if param in params:
            return sorted(self.bouquet, key=lambda flower: getattr(flower, param, None), reverse=reverse)
        else:
            return ValueError('Parameter for sorting() is incorrect!')

    def find_by_param(self, **kwargs):
        params = ['cost', 'name', 'lifetime', 'color', 'height', 'country']

        if not kwargs:
            return ValueError(f'Parameter and its value should be provided!')

        for key, value in kwargs.items():
            if key in params:
                founded_flower = list(filter(lambda flower: getattr(flower, key, None) == value, self.bouquet))
                if not founded_flower:
                    return ValueError('Flower with that value of parameter wasn\'t found')
                else:
                    print('Flower with that parameter and its value was found!')
                    return founded_flower[0]
            else:
                return ValueError('Parameter for find_by_param() is incorrect!')

    def __str__(self):
        return f"Bouquet contains: {self.bouquet}"


bouquet = Bouquet()
bouquet.add_flower(tulip)
bouquet.add_flower(rose_red)
bouquet.add_flower(rose_blue)

print(bouquet)
print(bouquet.bouquet_lifetime())   # workability bouquet_lifetime()
print(bouquet.bouquet_cost())   # workability bouquet_cost()
print(bouquet.sorting('cost', reverse=True))    # workability sorting() with correct parameter
print(bouquet.sorting('blabla'))    # workability of sorting with incorrect parameter
print(bouquet.find_by_param(cost=100))  # workability of find_by_param() with correct parameter and its value
print(bouquet.find_by_param(blabla=1000))   # workability of find_by_param() with incorrect parameter and its value

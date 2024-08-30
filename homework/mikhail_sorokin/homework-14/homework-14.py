"""
Создать классы цветов: общий класс для всех цветов и классы для нескольких видов. Создать экземпляры (объекты)
 цветов разных видов. Собрать букет (букет - еще один класс) с определением его стоимости. В букете цветы пусть
  хранятся в списке. Это будет список объектов.

Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.

Позволить сортировку цветов в букете на основе различных параметров
(свежесть/цвет/длина стебля/стоимость)(это тоже методы)

Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).
"""


class Flowers:
    kingdom = 'Plantae'
    name = str
    raff_count_total = int
    live_time = int
    price = float

    def __init__(self, price, **kwargs):
        self.price = price
        self.name = kwargs.get('name')
        self.name = kwargs.get('order')
        self.name = kwargs.get('family')
        self.name = kwargs.get('genus')
        self.name = kwargs.get('name')
        self.name = kwargs.get('live_time')


class Rafflesia(Flowers):
    order = "Malpighiales"
    family = "Rafflesiaceae"
    genus = "Rafflesia"
    name = "Rfflesia Arnoldii"
    raff_count_total = 0
    live_time = 90

    def __init__(self, count, price):
        super().__init__(price,
                         name=self.name, order=self.order, family=self.family,
                         genus=self.genus, live_time=self.live_time
                         )
        self.count = count
        Rafflesia.raff_count_total += count

    def __str__(self):
        return f"{self.name} (Count: {self.count}, Live Time: {self.live_time} days, Price: {self.price})"


class Tulip(Flowers):
    order = "Liliales"
    family = "Liliaceae"
    genus = "Tulipa"
    name = "Tulip"
    tulip_count_total = 0
    live_time = 7

    def __init__(self, count, price):
        super().__init__(price,
                         name=self.name, order=self.order, family=self.family,
                         genus=self.genus, live_time=self.live_time
                         )
        self.count = count
        Tulip.tulip_count_total += count

    def __str__(self):
        return f"{self.name} (Count: {self.count}, Live Time: {self.live_time} days, Price: {self.price})"


class Rose(Flowers):
    order = "Rosales"
    family = "Rosaceae"
    genus = "Rosa"
    name = "Rose"
    rose_count_total = 0
    live_time = 20

    def __init__(self, count, price):
        super().__init__(price,
                         name=self.name, order=self.order, family=self.family,
                         genus=self.genus, live_time=self.live_time)
        self.count = count
        Rose.rose_count_total += count

    def __str__(self):
        return f"{self.name} (Count: {self.count}, Live Time: {self.live_time} days, Price: {self.price})"


class Bouquet:
    def __init__(self):
        self.list_of_flowers = []

    def add_flowers(self, flower):
        self.list_of_flowers.append(flower)

    def bouquet_live_time(self):
        if not self.list_of_flowers:
            return 0
        total_live_time = sum(flower.live_time * flower.count for flower in self.list_of_flowers)
        total_flowers = sum(flower.count for flower in self.list_of_flowers)
        time = total_live_time / total_flowers
        return f"Bouquet live time is: {round(time)} days"

    def bouquet_price(self):
        total_price = sum(flower.price * flower.count for flower in self.list_of_flowers)
        return f"Total price of bouquet is: {total_price}"

    def sort_by_price(self, reverse=False):
        self.list_of_flowers.sort(key=lambda flower: flower.price, reverse=reverse)
        return self.list_of_flowers

    def sort_by_name(self, reverse=False):
        self.list_of_flowers.sort(key=lambda flower: flower.name, reverse=reverse)
        return self.list_of_flowers

    def multi_sort(self, sort_param, reverse=False):
        self.list_of_flowers.sort(key=lambda flower: getattr(flower, sort_param), reverse=reverse)
        return self.list_of_flowers

    def search(self, search_element):
        return [
            item for item in self.list_of_flowers
            if search_element in item.__dict__.values()
        ]

    def __str__(self):
        flowers_str = ", ".join(str(flower) for flower in self.list_of_flowers)

        return f"{flowers_str}"


rafflesia = Rafflesia(3, 11000)
tulip = Tulip(10, 200)
rose = Rose(33, 400)
bouquet = Bouquet()
bouquet.add_flowers(rafflesia)
bouquet.add_flowers(tulip)
bouquet.add_flowers(rose)

print(bouquet.bouquet_live_time())
print(bouquet)

print(bouquet.bouquet_price())

print(", ".join(str(flower) for flower in bouquet.sort_by_price()))
print(", ".join(str(flower) for flower in bouquet.sort_by_name(reverse=False)))
print(", ".join(str(flower) for flower in bouquet.multi_sort('count', reverse=True)))

print(", ".join(str(flower) for flower in bouquet.search(7)))

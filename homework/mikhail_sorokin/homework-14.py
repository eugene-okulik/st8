"""
Создать классы цветов: общий класс для всех цветов и классы для нескольких видов. Создать экземпляры (объекты)
 цветов разных видов. Собрать букет (букет - еще один класс) с определением его стоимости. В букете цветы пусть
  хранятся в списке. Это будет список объектов.

Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.

Позволить сортировку цветов в букете на основе различных параметров
(свежесть/цвет/длина стебля/стоимость)(это тоже методы)

Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).
"""


# хотел сделать чтобы общее кол-во цветов считалось, общая стоимость была, и прочее было в общем классе,
# но устал уже и туплю не понимаю как.
# Еще хотел чтобы если цветок паразит то время жизни букета уменьшалось, наверное позже допилю


class Flowers:
    kingdom = 'Plantae'
    order = str
    family = str
    genus = str
    name = str
    is_parasitic = bool(None)
    total_flowers_count = 0
    total_price = 0
    flowers_name = []

    def __init__(self, count, price, **kwargs):
        self.name = kwargs.get('order')
        self.name = kwargs.get('family')
        self.name = kwargs.get('genus')
        self.name = kwargs.get('name')
        self.count = count
        self.price = price
        self.total_flowers_count += count
        self.total_price += price
        self.flowers_name.append({self.name})


class Rafflesia(Flowers):
    order = "Malpighiales"
    family = "Rafflesiaceae"
    genus = "Rafflesia"
    name = "Rfflesia Arnoldii"
    is_parasitic = True
    raff_count_total = 0
    live_time = 90
    price = 11000

    def __init__(self, count, price):
        super().__init__(count, price, name=self.name, order=self.order, family=self.family, genus=self.genus)
        Rafflesia.raff_count_total += count


class Tulip(Flowers):
    order = "Liliales"
    family = "Liliaceae"
    genus = "Tulipa"
    name = "Tulip"
    tulip_count_total = 0
    live_time = 7
    price = 200

    def __init__(self, count, price):
        super().__init__(count, price, name=self.name, order=self.order, family=self.family, genus=self.genus)
        Tulip.tulip_count_total += count


class Rose(Flowers):
    order = "Rosales"
    family = "Rosaceae"
    genus = "Rosa"
    name = "Rose"
    rose_count_total = 0
    live_time = 20

    def __init__(self, count, price):
        super().__init__(count, price, name=self.name, order=self.order, family=self.family, genus=self.genus)
        Rose.rose_count_total += count


class Bouquet:
    def __init__(self):
        self.list_of_flowers = []

    def add_flowers(self, flower_name: str, flower_price: float, flower_count: int, flower_live_time: int):
        self.list_of_flowers.append({
            'name': flower_name,
            'count': flower_count,
            'live_time': flower_live_time,
            'price': flower_price
        })

    def bouquet_live_time(self):
        if not self.list_of_flowers:
            return 0
        total_live_time = sum(flower['live_time'] * flower['count'] for flower in self.list_of_flowers)
        total_flowers = sum(flower['count'] for flower in self.list_of_flowers)
        time = total_live_time / total_flowers
        return f"Bouquet live time is:  {round(time)} days"

    def bouquet_price(self):
        total_price = sum(flower['price'] * flower['count'] for flower in self.list_of_flowers)
        return f"Total price of bouquet is: {total_price}"

    def sort_by_price(self, reverse=False):
        """
        reverse: Если True, то сортировка по убыванию.
                 Если False, то сортировка по возрастанию.
        """
        self.list_of_flowers.sort(key=lambda flower: flower['price'], reverse=reverse)
        return self.list_of_flowers

    def sort_by_name(self, reverse=False):
        self.list_of_flowers.sort(key=lambda flower: flower['name'], reverse=reverse)
        return self.list_of_flowers

    def multi_sort(self, sort_param, reverse=False):
        self.list_of_flowers.sort(key=lambda flower: flower[f'{sort_param}'], reverse=reverse)
        return self.list_of_flowers

    def search(self, search_element):
        return [
            item for item in self.list_of_flowers
            if search_element in item.keys() or search_element in item.values()
        ]


rafflesia = Rafflesia(3, 11000 * 3)
tulip = Tulip(10, 200 * 10)
rose = Rose(33, 400 * 33)
bouquet = Bouquet()
bouquet.add_flowers(Rafflesia.name, rafflesia.price, rafflesia.count, rafflesia.live_time)
bouquet.add_flowers(tulip.name, tulip.price, tulip.count, tulip.live_time)
bouquet.add_flowers(rose.name, rose.price, rose.count, rose.live_time)
print(bouquet.bouquet_live_time(), bouquet.list_of_flowers)

print(bouquet.sort_by_price())
print(bouquet.sort_by_name(reverse=False))
print(bouquet.multi_sort('count', reverse=True))

print(bouquet.search(7))

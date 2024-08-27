from Flowers import Flowers


class Carnation(Flowers):
    def __init__(self, name, color, smell, price=int, stem_length=int, life_time_flow=int):
        super().__init__(name, color, smell, price, stem_length, life_time_flow)

class Human:
    default_name = None
    default_age = 0
    __money = 0
    __house = 0
    def __init__(self, name, age, money, house):
        self.default_name = name
        self.default_age = age
        self.__money = money
        self.__house = house

    def info(self):
        return 'name:', self.default_name, 'age:', self.default_age, 'money', self.__money, 'house:', self.__house

    def default_info(self):
        return default_name, default_age

    def __make_a_deal(self):
        result = __money - __house
        return result

    def earn_money(self):
        __money+= 500
        return __money

    def buy_house(self):
        if __house > __money:
            return 'Not enough money'

class House:
    def __init__(self,area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        result = self._price * (discount/ 100)
        return result

class SmallHouse(House):
    def __init__(self):
        self._area = 40


human1 = Human('bob', 24, )
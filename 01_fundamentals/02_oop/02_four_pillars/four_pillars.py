class CoffeeMaker:
    def __init__(self, name):
        self.name = name
        self.water_temp = 200

    def brew_now(self, beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")

    def clean(self):
        print("Cleaning!")


class CappuccinoMaker(CoffeeMaker):
    def __init__(self, name):
        super().__init__(name)
        self.milk = "whole"

    def make_cappuccino(self, beans):
        super().brew_now(beans)
        print("Frothy!!!")

    def clean(self):
        print("Cleaning the froth!")


class Barista:
    def __init__(self, name):
        self.name = name
        self.cafe = CoffeeMaker("Cafe")

    def make_coffee(self, beans):
        self.cafe.brew_now(beans)

# coffee_maker = CoffeeMaker('Mr. Coffee')
# print(coffee_maker.name)
# coffee_maker.brew_now('Guatemalan')

# cap = CappuccinoMaker('Captain my Captain')
# print(cap.name)
# print(cap.water_temp)
# print(cap.milk)
# cap.make_cappuccino('espresso')
# cap.brew_now('espresso')
# cap.clean()

ciso = Barista('Narciso')
print(ciso.name)
ciso.make_coffee('pinto')


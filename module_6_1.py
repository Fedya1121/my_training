class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

class Plant:
    adible = False

    def __init__(self, name):

        self.name = name

class Mammal(Animal):

    def eat(self, food):
        if food.adible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False



class Predator(Animal):

    def eat(self, food):
        if isinstance(food, Plant):
            print(f"{self.name} не может съесть {food.name}")
            self.alive = False
        else:
            self.fed = True
            print(f"{self.name} съел {food.name}")


class Flower(Plant):
    adible = False


class Fruit(Plant):
    adible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
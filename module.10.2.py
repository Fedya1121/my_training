import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def battle(self, name, power):
        day = 1
        enemy = 100
        while True:
            enemy -= power
            print(f"{name} сражается {day} день(дня)..., осталось {enemy} воинов.")
            time.sleep(1)
            day += 1
            if enemy == 0:
                print(f"{name} одержал победу спустя {day} дней(дня)!")
                break



    def run(self):
        print(f"{self.name}, на нас напали!")
        self.battle(self.name, self.power)
        print("Все битвы закончились!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

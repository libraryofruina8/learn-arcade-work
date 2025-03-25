from pyglet.input.xinput import BATTERY_LEVEL_FULL


class Cat():
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = 0

    def meow(self):
        print("Meow")

cute_cat = Cat()

cute_cat.name = "Cosmo"
cute_cat.color = "Black"
cute_cat.weight = 8

cute_cat.meow()

class Monster():
    def __init__(self):
        self.name = ""
        self.health = 0

    def decrease_health(self, lost_health):
        self.health -= lost_health
        if self.health < 1:
            print(self.name, "is dead")
        else:
            print(self.name, "health is now", self.health)


dude = Monster()
dude.name = "Barf"
dude.health = 100

dude.decrease_health(50)

class Star():






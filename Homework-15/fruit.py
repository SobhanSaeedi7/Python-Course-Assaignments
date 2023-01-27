import random
import arcade

class Fruit(arcade.Sprite):
    def __init__(self, game, png):
        super().__init__(png)
        self.width = 42
        self.height = 42
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.score = 0
        self.size = 0

class Apple(Fruit):
    def __init__(self, game):
        super().__init__(game, "PNGs\Apple.png")
        self.score = 1
        self.size = 1


class Pear(Fruit):
    def __init__(self, game):
        super().__init__(game, 'PNGs\pear.png')
        self.score = 2

class Poo(Fruit):
    def __init__(self, game):
        super().__init__(game, 'PNGs\poo.png')
        self.score = -1
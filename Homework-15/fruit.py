import random
import arcade

# class Fruit(arcade.Sprite):
#     def __init__(self, game, png):
#         super().__init__(png)
#         self.width = 42
#         self.height = 42
#         self.center_x = random.randint(10, game.width - 10)
#         self.center_y = random.randint(10, game.height - 10)
#         self.score = 0
#         self.size = 0

class Apple(arcade.Sprite):
    def __init__(self, game):
        super().__init__('PNGs\Apple.png')
        self.width = 42
        self.height = 42
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.score = 1
        self.size = 1

class Pear(arcade.Sprite):
    def __init__(self, game):
        super().__init__('PNGs\pear.png')
        self.width = 42
        self.height = 42
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.score = 2
        self.size = 0

class Poo(arcade.Sprite):
    def __init__(self, game):
        super().__init__('PNGs\poo.png')
        self.width = 42
        self.height = 42
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.score = -1
        self.size = 0

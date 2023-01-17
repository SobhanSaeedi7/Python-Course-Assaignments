import random
import arcade

class Apple(arcade.Sprite):
    def __init__(self,game):
        super().__init__("PNGs\pngwing.com (1).png")
        self.width = 42
        self.height = 42
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
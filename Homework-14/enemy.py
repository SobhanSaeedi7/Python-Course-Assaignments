import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self,game):
        super().__init__("game pngs\pngwing.com.png")
        self.center_x = random.randint(0, game.width)
        self.center_y = game.height + 24
        self.angle = 270
        self.width = 60
        self.height  = 60

    def move(self, speed):
        self.center_y -= speed
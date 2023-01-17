import arcade

class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__("game pngs\Polish_20230115_193848653.png")
        self.center_x = game.width // 2
        self.center_y = 50
        self.width = 64
        self.height = 64
        self.speed = 8
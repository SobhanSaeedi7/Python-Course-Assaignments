import arcade
from bullet import Bullet

class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__("game pngs\Polish_20230115_193848653.png")
        self.fire_sound = arcade.load_sound(":resources:sounds/laser3.wav")
        self.center_x = game.width // 2
        self.center_y = 50
        self.change_x = 0
        self.change_y = 0 
        self.width = 72
        self.height = 72
        self.speed = 2
        self.game_width = game.width
        self.bullets = []

    def move(self):
        if self.change_x == -1:
            if self.center_x > 0:
                self.center_x = self.center_x - self.speed
        elif self.change_x == 1:
            if self.center_x < self.game_width:
                self.center_x = self.center_x + self.speed



    def fire(self):
        new_bullet = Bullet(self)
        self.bullets.append(new_bullet)
        arcade.play_sound(self.fire_sound)
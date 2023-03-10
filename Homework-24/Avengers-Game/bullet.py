import arcade

class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserBlue01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.angle = 90
        self.change_x = 0
        self.change_y = 1
        self.speed = 3

    def move(self):
        self.center_y += self.speed
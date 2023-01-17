import arcade

class Heart(arcade.Sprite):
    def __init__(self,distance):
        super().__init__("game pngs\pngwing.com (1).png")
        self.center_y = 35
        self.center_x = 45 + distance
        self.width = 30 
        self.height = 30


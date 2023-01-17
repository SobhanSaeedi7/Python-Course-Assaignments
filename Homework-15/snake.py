import arcade

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.RED
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.size = 0
        self.body = []
        self.body_coler = 0

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
        for part in self.body:
            if self.body_coler%2 == 0:
                self.body_coler += 1
                arcade.draw_rectangle_filled(part['x'], part['y'], self.width, self.height, arcade.color.BLUE)
            elif self.body_coler%2 == 1:
                self.body_coler += 1
                arcade.draw_rectangle_filled(part['x'], part['y'], self.width, self.height, arcade.color.RED)
    
    def move(self):
        self.body.append({'x':self.center_x, 'y':self.center_y})
        if len(self.body) > self.size:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def eat(self, food):
        self.size += 1
        del food
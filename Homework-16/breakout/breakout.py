import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self, board):
        super().__init__()
        self.center_x = board.center_x
        self.center_y = board.center_y + self.height
        self.change_x = random.choice([1, -1])
        self.change_y = 1
        self.reduce = 5
        self.height = self.reduce*2
        self.width = self.reduce*2
        self.speed = 4
        self.color = arcade.color.GREEN_YELLOW

        def move(self):
            ...
        
        def draw(self):
            arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)


class Brik(arcade.Sprite):
    def __init__(self, game, x, y, c):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.width = game.width // 10
        self.height = 10
        self.color = c

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

class Board(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width // 2
        self.center_y = 35
        self.change_x = 0
        self.change_y = 0
        self.width = game.width // 10
        self.hieght = 10
        self.color = arcade.color.RED_DEVIL
        self.score = 0

    def move(self):
        ...

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color) 

class heart(arcade.Sprite):
    ...

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=700, title="BreakOut")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.board = Board(self)
        self.ball = Ball(self.board)

    def on_draw(self):
        arcade.start_render()
        self.board.draw()
        self.ball.draw()
        arcade.finish_render()




game = Game()
arcade.run()
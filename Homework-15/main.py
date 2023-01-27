import random
import arcade
import fruit
from snake import Snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake V1")
        arcade.set_background_color(arcade.color.GO_GREEN)
        self.apple = fruit.Apple(self)
        self.pear = fruit.Pear(self)
        self.poo = fruit.Poo(self)
        self.snake = Snake(self)
        self.state = True
        self.started = False

    def on_draw(self):

        arcade.start_render()

        self.apple.draw()
        self.pear.draw()
        self.poo.draw()
        self.snake.draw()
        arcade.draw_text(f'Score: {self.snake.score}', self.width - 100, 10, arcade.color.RED, 15, 1, 'left',"calibri",True)

        if self.state == False:
            self.clear()
            arcade.draw_rectangle_filled(self.width//2, self.height//2, self.width, self.height, arcade.color.BLACK)
            arcade.draw_text('"Game Over"', self.width//2-110, self.height//2, arcade.color.RED, 25, 1,'left', 'calibri', True)

        arcade.finish_render()

    def on_update(self, delta_time):
        self.snake.move()
        
        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat(self.apple)
            self.apple = fruit.Apple(self)
            self.started = True

        if arcade.check_for_collision(self.snake, self.pear):
            self.snake.eat(self.pear)
            self.pear = fruit.Pear(self)
            self.started = True

        if arcade.check_for_collision(self.snake, self.poo):
            self.snake.eat(self.poo)
            self.poo = fruit.Poo(self)
            if self.snake.score < 0:
                self.state = False
            if self.snake.score == 0 and self.started == True:
                self.state = False

        if self.snake.center_x < 0 or self.snake.center_x > self.width or self.snake.center_y < 0 or self.snake.center_y > self.height:
            self.state = False




    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        if symbol == arcade.key.DOWN:
           self.snake.change_x = 0
           self.snake.change_y = -1 
        if symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0


if __name__ == "__main__":
    game = Game()
    arcade.run()
import random
import arcade
from snake import Snake
from apple import Apple


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake V1")
        arcade.set_background_color(arcade.color.GO_GREEN)
        self.score = 0
        self.food_number = random.randint(1, 4)
        self.food = self.food_type
        self.snake = Snake(self)

    def on_draw(self):

        arcade.start_render()

        self.food.draw()
        self.snake.draw()

        arcade.finish_render()

    def on_update(self, delta_time):
        self.snake.move()
        
        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food)
            self.food = Apple(self)


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
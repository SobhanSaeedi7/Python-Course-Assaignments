import random
import arcade
import fruit
from snake import Snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake V1")
        arcade.set_background_color(arcade.color.GO_GREEN)
        self.score = 0
        self.food_number = random.randint(1, 4)
        self.apple = fruit.Apple(self)
        self.pear = fruit.Pear(self)
        self.poo = fruit.Poo(self)
        self.snake = Snake(self)
        self.state = "OKEY"

    def on_draw(self):

        arcade.start_render()

        self.apple.draw()
        self.pear.draw()
        self.poo.draw()
        self.snake.draw()
        arcade.draw_text(f'Score: {self.snake.score}', self.width - 100, 10, arcade.color.RED_VIOLET, 15, 1, 'left',"calibri",True)

        if self.state == "game_over":
            arcade.draw_text("Game Over", self.width//2, self.height//2, arcade.color.RED, 50, 1,'left', 'calibri', True)

        arcade.finish_render()

    def on_update(self, delta_time):
        self.snake.move()
        
        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat(self.apple)
            self.apple = fruit.Apple(self)

        if arcade.check_for_collision(self.snake, self.pear):
            self.snake.eat(self.pear)
            self.pear = fruit.Pear(self)

        if arcade.check_for_collision(self.snake, self.poo):
            self.snake.eat(self.poo)
            self.poo = fruit.Poo(self)
            if self.snake.score == 0:
                self.status = "game_over"

        for body in self.snake.body:
             if self.snake.center_x+30==body['x'] or self.snake.center_x+30==body['x'] or self.snake.center_y+30 ==body['y'] or self.snake.center_y-30==body['y']:
                self.game_status="game_over"

        if self.snake.center_x ==500 or self.snake.center_x==0 or self.snake.center_y==500 or self.snake.center_y==0:
            self.game_status="game_over"


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
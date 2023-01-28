import random
import arcade
import fruit
from snake import Snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake Vai")
        arcade.set_background_color(arcade.color.GO_GREEN)
        self.score = 0
        self.apple = fruit.Apple(self)
        self.pear = fruit.Pear(self)
        self.poo = fruit.Poo(self)
        self.snake = Snake(self)


    def on_draw(self):

        arcade.start_render()

        self.apple.draw()
        self.pear.draw()
        self.poo.draw()
        self.snake.draw()
        arcade.draw_text(f'Score: {self.snake.score}', self.width - 100, 10, arcade.color.RED, 15, 1, 'left',"calibri",True)


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

        dxp=self.snake.center_x - self.pear.center_x
        dyp=self.snake.center_y - self.pear.center_y

        dxa=self.snake.center_x - self.apple.center_x
        dya=self.snake.center_y - self.apple.center_y

        if (abs(dxp)<abs(dxa)) and (abs(dyp)<abs(dya)) :
            
            if dxp>0:
                if dyp>0:
                    self.snake.change_x=-1
                    self.snake.change_y=-1
                elif dyp<0:
                    self.snake.change_x=-1
                    self.snake.change_y=1
                else:
                    self.snake.change_x=-1
                    self.snake.change_y=0

            if dxp<0:
                if dyp>0:
                    self.snake.change_x=1
                    self.snake.change_y=-1
                elif dyp<0:
                    self.snake.change_x=1
                    self.snake.change_y=1
                else:
                    self.snake.change_x=1
                    self.snake.change_y=0   

            if dxp==0:
                if dyp>0:
                    self.snake.change_x=0
                    self.snake.change_y=-1
                elif dyp<0:
                    self.snake.change_x=0
                    self.snake.change_y=1
                else:
                    self.snake.change_x=0
                    self.snake.change_y=0    
        else:   
            if dxa>0:
                if dya>0:
                    self.snake.change_x=-1
                    self.snake.change_y=-1
                elif dya<0:
                    self.snake.change_x=-1
                    self.snake.change_y=1
                else:
                    self.snake.change_x=-1
                    self.snake.change_y=0

            if dxa<0:
                if dya>0:
                    self.snake.change_x=1
                    self.snake.change_y=-1
                elif dya<0:
                    self.snake.change_x=1
                    self.snake.change_y=1
                else:
                    self.snake.change_x=1
                    self.snake.change_y=0   

            if dxa==0:
                if dya>0:
                    self.snake.change_x=0
                    self.snake.change_y=-1
                elif dya<0:
                    self.snake.change_x=0
                    self.snake.change_y=1
                else:
                    self.snake.change_x=0
                    self.snake.change_y=0  




if __name__ == "__main__":
    game = Game()
    arcade.run()
import random
import time
import arcade
from spaceship import Spaceship
from enemy import Enemy
from bullet import Bullet
from heart import Heart

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=700, title="AVENGERS")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.game_over = arcade.load_texture("game pngs\Polish_20230116_214822919 (1).jpg")
        self.explosion_sound = arcade.load_sound(":resources:sounds/hit5.wav")
        self.status = True
        self.score = 0
        self.speed = self.score // 5 + 1
        self.time = time.time()
        self.me = Spaceship(self)
        self.enemies = []
        self.life = 3
        self.hearts = []


    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        for enemy in self.enemies:
            enemy.draw()
        for bullet in self.me.bullets:
            bullet.draw()
        for i in range(self.life):
            self.hearts[i].draw()
        arcade.draw_text(f"Score : {self.score}", self.width - 100, 30, arcade.color.WHITE, 15, 1, "left", "calibri", True)
        if self.status == False:
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.game_over)

        arcade.finish_render()
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.me.change_x = -1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.me.change_x = 1
        elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.me.change_x = 0
        elif symbol == arcade.key.SPACE or symbol == arcade.key.W:
            self.me.fire()

    def on_update(self, delta_time):

        self.me.move()

        for enemy in self.enemies:
            if arcade.check_for_collision(self.me, enemy):
                self.enemies.remove(enemy)
                self.life -= 1
                self.hearts.remove(self.hearts[self.life])

        for enemy in self.enemies:
            for bullet in self.me.bullets:
                if arcade.check_for_collision(enemy, bullet):
                    arcade.play_sound(self.explosion_sound)
                    self.score += 1
                    self.enemies.remove(enemy)
                    self.me.bullets.remove(bullet)
                    

        for enemy in self.enemies:
            enemy.move(self.speed)
            if enemy.center_y < 0 :
                self.enemies.remove(enemy)
                self.life -= 1
                self.hearts.remove(self.hearts[self.life])

        for bullet in self.me.bullets:
            bullet.move()
            if bullet.center_y > self.height :
                self.me.bullets.remove(bullet)

        for i in range(self.life):
            new_heart = Heart(i*30)
            self.hearts.append(new_heart)
        
        if time.time() - self.time > 3 :
            new_enemy = Enemy(self)
            self.enemies.append(new_enemy)
            self.time = time.time()
        
        if self.life == 0:
            self.status = False

window = Game()

arcade.run()



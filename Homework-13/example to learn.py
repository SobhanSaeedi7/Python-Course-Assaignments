
import arcade

SPACING = 20
MARGIN = 100

arcade.open_window(400, 400, "an Example to Learn")

arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()

for row in range(10):
    for column in range(10):
        if (row%2==0 and column%2==0) or (row%2==1 and column%2==1):
            x = column * SPACING + MARGIN
            y = row * SPACING + MARGIN
            arcade.draw_rectangle_filled(x,y,10,10,arcade.color.DARK_BLUE,45)
        elif (row%2==0 and column%2==1) or (row%2==1 and column%2==0):
            x = column * SPACING + MARGIN
            y = row * SPACING + MARGIN
            arcade.draw_rectangle_filled(x,y,10,10,arcade.color.RED_DEVIL,45)

arcade.finish_render()

arcade.run()
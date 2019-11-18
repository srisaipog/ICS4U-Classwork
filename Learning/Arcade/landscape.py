import arcade
from random import randint


WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "some blocky landscape")


def setup():
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    pass


@window.event
def on_draw():
    arcade.start_render()

    # Ground
    arcade.draw_lrtb_rectangle_filled(0, WIDTH, 100, 0, arcade.color.GREEN)

    # sun
    arcade.draw_circle_filled(WIDTH-100, HEIGHT-100, 50, arcade.color.YELLOW)

    draw_tree(175, 100, 150, 50, 10)
    draw_forest(200, 80, 15, 100)
    # draw_forest()


def draw_tree(x: int, y: int, height: int, percent_log: int, width: int):
    if percent_log > 100 or percent_log < 0:
        percent_log = 70
    
    percent_log *= 0.01

    arcade.draw_xywh_rectangle_filled(x, y, width, height * percent_log, arcade.color.BROWN)
    arcade.draw_triangle_filled(x - width,
                                y + percent_log * height,
                                x + width/2,
                                y + height,
                                x + width * 2,
                                y + percent_log * height,
                                arcade.color.GREEN)


def draw_forest(x: int, y: int, width: int, height: int):
    for i in range(0, width * 20, 20):
        # Dancing trees
        draw_tree(x + i, y + randint(-5, 5), height + randint(-50, 50), 70, width)
        # mabye make tree an object
        # and forests an object which uses the trees to make it stop dancing. or something.





if __name__ == '__main__':
    setup()
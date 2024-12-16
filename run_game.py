import turtle
import random
import character
import big_ball
import small_ball


class GameRun:
    def __init__(self):
        # set each variable
        self.num_small_ball = 50
        self.num_big_ball = 2
        self.small_ball_list = []
        self.big_ball_list = []
        self.ball_list = []
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]

        # set up the turtle
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

        # create small balls
        small_radius = 10
        for i in range(self.num_small_ball):
            x = random.uniform(-390, 390)
            y = 290.0
            vx = 0.0
            vy = 2.25
            ball_color1 = (255, 123, 123)
            ball_color2 = (253, 215, 113)
            ball_color3 = (173, 216, 141)
            ball_color4 = (255, 139, 19)
            ball_color5 = (255, 179, 198)
            ball_color_list = [ball_color1, ball_color2, ball_color3,
                               ball_color4, ball_color5]
            ball_color = random.choice(ball_color_list)
            self.small_ball_list.append(small_ball.SmallBall(small_radius,
                                                             x, y, vx, vy,
                                                             ball_color, i))

        # create big balls
        big_radius = 20
        for j in range(self.num_big_ball):
            x = random.uniform(-390, 390)
            y = 270.0
            vx = 0.0
            vy = 2.0
            ball_color = (132, 186, 201)
            self.big_ball_list.append(big_ball.BigBall(big_radius,
                                                       x, y, vx, vy,
                                                       ball_color, j))

        # create and set up our character
        cha_thai = turtle.Turtle()
        self.our_character = character.Character(80, 25, (209, 111, 44),
                                                 cha_thai)
        self.our_character.set_location([0, -282])
        self.screen = turtle.Screen()

    def __draw_border(self):
        # make the turtle draws the border
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

    def move_left(self):
        # make our character move a little bit to the left
        if ((self.our_character.location[0] - self.our_character.width / 2 - 10)
                >= -self.canvas_width):
            self.our_character.set_location([self.our_character.location[0]
                                             - 10,
                                             self.our_character.location[1]])

    def move_right(self):
        # make our character move a little bit to the right
        if ((self.our_character.location[0] + self.our_character.width / 2 + 10)
                <= self.canvas_width):
            self.our_character.set_location([self.our_character.location[0]
                                             + 10,
                                             self.our_character.location[1]])

    def run(self):
        # make our character move according to the keys on the keyboard
        self.screen.listen()
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")

        # set our time to be -1
        dt = -1

        # make the balls (both big and small) move down
        while True:
            turtle.clear()
            self.__draw_border()
            self.our_character.draw()
            for i in range(self.num_small_ball):
                self.small_ball_list[i].draw()
                self.small_ball_list[i].move(dt)
            for j in range(self.num_big_ball):
                self.big_ball_list[j].draw()
                self.big_ball_list[j].move(dt)
                if self.our_character.location[0] == self.big_ball_list[j].x:
                    turtle.bye()
                    print("You got hit by the big ball. You lost.")
            turtle.update()


# run the program
run_game = GameRun()
run_game.run()

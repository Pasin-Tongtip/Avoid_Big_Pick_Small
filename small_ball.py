import turtle


class SmallBall:
    def __init__(self, size, x, y, vx, vy, color, small_id):
        # set each variable
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.id = small_id

        # set other variables
        self.mass = 50 * size ** 2
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]

    def draw(self):
        # draw small balls
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move(self, dt):
        # make small balls move by change the location of the balls
        self.x += self.vx * dt
        self.y += self.vy * dt

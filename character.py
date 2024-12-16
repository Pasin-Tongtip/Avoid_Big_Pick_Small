class Character:
    def __init__(self, width, height, color, my_turtle):
        # set each variable
        self.width = width
        self.height = height
        self.location = [0, -282]
        self.color = color
        self.turtle = my_turtle

        # set up the turtle
        self.turtle.penup()
        self.turtle.setheading(0)
        self.turtle.hideturtle()

    def set_location(self, location):
        # set new location for our turtle.
        self.location = location
        self.turtle.goto(self.location[0], self.location[1])

    def draw(self):
        # set the color of the turtle to be the color we set earlier.
        self.turtle.color(self.color)

        # make the turtle draws our character.
        self.turtle.goto(self.location[0], self.location[1] - self.height/2)
        self.turtle.forward(self.width/2)
        self.turtle.pendown()
        self.turtle.clear()
        self.turtle.begin_fill()
        for _ in range(2):
            self.turtle.left(90)
            self.turtle.forward(self.height)
            self.turtle.left(90)
            self.turtle.forward(self.width)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.goto(self.location[0], self.location[1])

    def clear(self):
        # clear the turtle
        self.turtle.clear()

    def __str__(self):
        return "character"

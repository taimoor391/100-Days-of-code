from turtle import Turtle, Screen
import time
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self,i):
        my_turtle = Turtle('square')
        my_turtle.color('white')
        my_turtle.penup()
        my_turtle.goto(i)
        self.segment.append(my_turtle)

    def extend(self):
        # add a new segment to snake
        self.add_segment(self.segment[-1].position())


    def move(self):

        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)
        self.segment[0].forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



from turtle import Turtle
STARTING_POSITION = [(0, 0), (-8, 0), (-12, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            segment = Turtle("square")
            segment.shapesize(stretch_len=0.8, stretch_wid=0.8)
            segment.penup()
            segment.color("white")
            segment.setposition(position)
            self.segments.append(segment)

    def get_bigger(self):
        segment = Turtle()
        segment.ht
        segment.speed('fastest')
        self.segments.append(segment)
        segment.shapesize(stretch_len=0.8, stretch_wid=0.8)
        segment.penup()
        segment.shape('square')
        segment.color("white")
        segment.st()

    def move(self):
        # moves each segments to it's forward buddy position starting from 3
        # (or last segment shown  as len(segments)-1) up to the first one (the zero)
        # then move the first one to new position
        for segment in range(len(self.segments) - 1, 0, -1):
            new_y = self.segments[segment - 1].ycor()
            new_x = self.segments[segment - 1].xcor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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




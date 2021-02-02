from turtle import Turtle
import time

ALIGNMENT = 'center'
FONT = ('Comic Sans MS', 12, 'normal')
PLAY_TIME = 10


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.play_time = PLAY_TIME
        self.score = 0
        self.ht()
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.goto(0, 285)
        self.write(f'score: {self.score} ', False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align='center', font=ALIGNMENT)

    def score_refresh(self):
        self.clear()
        self.score += 1
        self.write(f'score: {self.score} ', False, 'center', ('Comic Sans MS', 12, 'normal'))

    def timer(self):
        for seconds in range(PLAY_TIME):
            self.goto(0, 0)
            self.write(f'{self.play_time}', False, ALIGNMENT, FONT)
            time.sleep(1)
            self.clear()
            self.play_time -= 1
        # if self.play_time == 0:
        #     game_on = False
        #     self.game_over()

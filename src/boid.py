from numpy.random import random
from numpy.linalg import norm
from p5 import *
from config import height, width

class Boid():
    def __init__(self, x, y):
        vx = (random() - 0.5) * 5
        vy = (random() - 0.5) * 5
        ax = (random() - 0.5) / 2
        ay = (random() - 0.5) / 2

        self.position = Vector(x, y)
        self.velocity = Vector(vx, vy)
        self.acceleration = Vector(ax, ay)

    def checkBorders(self):
        # Left and right borders
        if self.position.x > width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = width

        # Top and bottom borders
        if self.position.y > height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = height

    def show(self):
        stroke(255)
        circle(self.position.x, self.position.y, 10)

    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration

        self.checkBorders()

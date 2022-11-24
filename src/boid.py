from numpy.random import random
from p5 import *

class Boid():
    def __init__(self, x, y, width, height):
        vx = (random() - 0.5) * 5
        vy = (random() - 0.5) * 5
        ax = (random() - 0.5) / 2
        ay = (random() - 0.5) / 2

        self.position = Vector(x, y)
        self.velocity = Vector(vx, vy)
        self.acceleration = Vector(ax, ay)
        self.width = width
        self.height = height

    def show(self):
        stroke(255)
        circle(self.position.x, self.position.y, 10)

    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration

        # Left and right borders
        if self.position.x > self.width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = self.width

        # Top and bottom borders
        if self.position.y > self.height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = self.height
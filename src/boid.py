from numpy.random import random
from p5 import *


class Boid():
    def __init__(self, x, y, width, height):
        self.position = Vector(x, y)

        vx = (random() - 0.5) * 5
        vy = (random() - 0.5) * 5
        self.velocity = Vector(vx, vy)

        ax = (random() - 0.5) / 2
        ay = (random() - 0.5) / 2
        self.acceleration = Vector(ax, ay)

    def show(self):
        stroke(255)
        circle(self.position.x, self.position.y, 10)

    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration
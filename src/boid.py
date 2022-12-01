from numpy import zeros
from numpy.linalg import norm
from numpy.random import random
from p5 import *
from config import height, maxSpeed, perception, width

class Boid():
    def __init__(self, x, y):
        vx = (random() - 0.5) * 5
        vy = (random() - 0.5) * 5
        ax = (random() - 0.5) / 2
        ay = (random() - 0.5) / 2

        self.position = Vector(x, y)
        self.velocity = Vector(vx, vy)
        self.acceleration = Vector(ax, ay)

    # steering = avgVec - self.velocity
    def align(self, boids):
        steering = Vector(*zeros(2))
        avgVec = Vector(*zeros(2))
        total = 0

        for boid in boids:
            if norm(boid.position - self.position) < perception:
                avgVec += boid.velocity
                total += 1

        if total > 0:
            avgVec /= total
            avgVec = Vector(*avgVec)
            avgVec = (avgVec / norm(avgVec)) * maxSpeed
            steering = avgVec - self.velocity

        self.acceleration += steering

    def checkBorders(self):
        # Left and right borders
        self.position.x = self.position.x % width
        # Top and bottom borders
        self.position.y = self.position.y % height

    def checkVelocity(self):
        if norm(self.velocity) > maxSpeed:
            self.velocity = self.velocity / norm(self.velocity) * maxSpeed
            self.acceleration = Vector(0, 0)

    def show(self):
        stroke(255)
        circle(self.position.x, self.position.y, 10)

    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration

        self.checkBorders()
        self.checkVelocity()
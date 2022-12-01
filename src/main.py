from p5 import *
from numpy.random import randint
from boid import Boid
from config import boidNumber, height, width

if __name__ == "__main__":
    boids = []

    for _ in range(boidNumber):
        x = randint(width)
        y = randint(height)
        boids.append(Boid(x, y))

    def setup():
        title("Boids simulation")
        size(width, height)

    def draw():
        background(30, 30, 47)

        for boid in boids:
            boid.show()
            boid.align(boids)
            boid.update()

    run()

from p5 import *
from numpy.random import randint
from boid import Boid

if __name__ == "__main__":
    boidNumber = 30
    boids = []
    height = 500
    width = 500

    for _ in range(boidNumber):
        x = randint(width)
        y = randint(height)
        boids.append(Boid(x, y, width, height))

    def setup():
        title("Boids simulation")
        size(width, height)

    def draw():
        background(30, 30, 47)

        for boid in boids:
            boid.show()
            boid.update()

    run()

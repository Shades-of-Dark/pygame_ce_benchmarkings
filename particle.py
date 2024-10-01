import random

import pygame


class Particle():
    def __init__(self, loc, screen):

        self.loc = loc
        self.display = screen
        self.radius = random.randint(4, 6)
        self.velocity = [random.randint(0, 20) / 10 - 1, -2]


    def draw(self, colour):
        pygame.draw.circle(self.display, colour, self.loc, self.radius)

    def gravity(self):
        self.loc[0] += self.velocity[0]
        self.loc[1] += self.velocity[1]
        self.radius -= 0.1
        self.velocity[1] += 0.1


#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from particle import Particle
import cloth

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('cloth?')
screen = pygame.display.set_mode((500, 500), 0, 32)

rag_data = cloth.load_rags('rags')

my_cloth = cloth.ClothObj(rag_data['vine'])
WHITE = (255, 255, 255)
render_mode = 0
particles = []
# Loop ------------------------------------------------------- #
while True:

    # Background --------------------------------------------- #
    screen.fill((0,0,0))

    # Cloth -------------------------------------------------- #
    mx, my = pygame.mouse.get_pos()

    # move
    my_cloth.move_grounded([200, 200])
    particles.append(Particle([mx, my], screen))
    # process
    my_cloth.update()
    my_cloth.update_sticks()

    # render
    if render_mode:
        my_cloth.render_polygon(screen, (34, 139, 34))
    else:
        my_cloth.render_sticks(screen)

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == K_r:
                if render_mode:
                    render_mode = 0
                else:
                    render_mode = 1

    for particle in particles:
        particle.draw((WHITE))
        particle.gravity()
        if particle.radius <= 0:
            particles.pop(particles.index(particle))

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)

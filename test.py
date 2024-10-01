import sys
import pygame
import time
pygame.init()
res = (500, 600)
display = pygame.display.set_mode(res)
start = time.time()
run = True
FPS = 60
clock = pygame.time.Clock()
s = pygame.Surface((10, 10)).convert()

# 0.008850812911987305  Pygame-ce
# 0.010195493698120117  Pygame

v = pygame.transform.scale(s, (3000, 2000))


print(time.time() - start)
pygame.quit()
sys.exit()

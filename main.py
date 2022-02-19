import pygame
import sys
from pygame.locals import *

pygame.init()

WIDTH = 500
HEIGHT = 400
WINDOW =  pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Hello World")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()

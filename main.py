import pygame
import sys
from pygame.locals import *

pygame.init()

WIDTH = 500
HEIGHT = 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()


def main():
	x, y = 50, 40
	vel = 3

	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
		    x -= vel
		elif keys[pygame.K_RIGHT]:
		 	x += vel
		elif keys[pygame.K_UP]:
			y -= vel
		elif keys[pygame.K_DOWN]:
			y += vel

		WINDOW.fill((0, 65, 123))
		pygame.draw.rect(WINDOW, (204, 204, 204), (x, y, 100, 100))

		pygame.display.update()


if __name__ == '__main__':
	main()

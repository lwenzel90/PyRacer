import pygame

pygame.init()
displayWidth = 1200
displayHeight = 800

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')
carImg = pygame.transform.scale(carImg, (100, 80))
def car(x,y):
	gameDisplay.blit(carImg, (x,y))#blit shows image 

x = displayWidth * 0.4
y = displayHeight * 0.2
xChange = 0

crashed = False

while not crashed:
	for event in pygame.event.get():#event loop 
		if event.type == pygame.QUIT:
			crashed = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				xChange += -5
			elif event.key == pygame.K_RIGHT:
				xChange += 5

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				xChange = 0
'''
 if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                change_x += 5
            if event.key == pygame.K_RIGHT:
                change_x += -5﻿
'''
	x += xChange
	gameDisplay.fill(white)
	car(x ,y)
	pygame.display.flip()#updates based on changes if given a parameter
	clock.tick(60)


pygame.quit()
quit()
import pygame
from pygame.locals import *
import math

pygame.init()

windowWidth,windowHeight = (1000,1000)

screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Robotic Kinematics")


BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

background = GRAY

robotJoint1Angle = 90
robotArm1Length = 500

running = True
while running:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
            if event.key == pygame.K_KP_0:
                robotJoint1Angle += 1
                print(Arm1.x)

    screen.fill(background)
    Arm1 = pygame.draw.line(screen, BLACK, (windowWidth/2,windowHeight/2), 
            (((windowWidth/2) + (robotArm1Length*math.cos(robotJoint1Angle))), 
             ((windowHeight/2) + (robotArm1Length*math.sin(robotJoint1Angle)))),
            10)
    

    pygame.display.update()

pygame.quit()
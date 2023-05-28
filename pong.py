#import pygame and initialize the pygame engine.
from re import X
import pygame
import random
from pygame.locals import *
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((600,600))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")
color = ((255,255,255))
clock = pygame.time.Clock()
#The Game Loop”
def score(msg, x, y, color, size):
    fontobj= pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))
x = 300
y = 300
x1 = 30
y1 = 0
x2 = 550
y2 = 0
turn = 0
up = False
down = False
up1 = False
down1 = False
movementrandomx = 5
movementrandomy = -5
scoreL = 0
scoreR = 0
while True:
    x = x + movementrandomx
    y = y + movementrandomy
    clock.tick(100)
    screen.fill((0,0,0))
    score (str(scoreL), 50,50 ,(255,255,255), 50)
    score (str(scoreR), 550,550 ,(255,255,255), 50)
    ball = pygame.draw.circle(screen, color, (x, y), 5)
    paddleL = pygame.draw.rect(screen, color, (x1, y1,10,120),0)
    paddleR = pygame.draw.rect(screen, color, (x2, y2,10,120),0)
    if ball.colliderect(paddleL):
        movementrandomx = random.randint(1,5)
        movementrandomy = random.randint(-3,3)
    if ball.colliderect(paddleR):
        movementrandomx = random.randint(-5,-1)
        movementrandomy = random.randint(-3,3)
    if x <= 0:
        x = 300
        scoreR = scoreR + 1
    if y1 >= 480:
        y1 = 480
    if y2 >= 480:
        y2 = 480
    if y1 <= 0:
        y1 = 0
    if y2 <= 0:
        y2 = 0
    if x >= 600:
        scoreL = scoreL + 1
        x = 300
        y = 300
    if y <= 0:
        movementrandomy = 5
    if y >= 600:
        movementrandomy = -5
    if scoreL == 50:
        score ("Left paddle wins", 150,50 ,(255,255,255), 50)
        break
    if scoreR == 50:
        score ("Right paddle wins", 150,50 ,(255,255,255), 50)
        break
    #Most of our game logic goes here
    #Continuously update the screen
    if up == True:
        y1 = y1 - 10
    if down == True:
        y1 = y1 + 10
    if up1 == True:
        y2 = y2 - 10
    if down1 == True:
        y2 = y2 + 10
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                up1 = True
            if event.key == K_DOWN:
                down1 = True
            if event.key == K_w:
                up = True
            if event.key == K_s:
                down = True
        if event.type == KEYUP:
            if event.key == K_UP:
                up1 = False
            if event.key == K_DOWN:
                down1 = False
            if event.key == K_w:
                up = False
            if event.key == K_s:
                down = False
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
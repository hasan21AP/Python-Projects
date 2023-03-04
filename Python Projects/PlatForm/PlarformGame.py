import pygame
import math 
import random
import os
from os.path import isfile,join
from os import listdir

pygame.init()

WIDTH,HEIGHT = 1366,768
FBS = 60 
PLAYER_VEL = 5

pygame.display.set_caption("Platform Game")
window = pygame.display.set_mode((WIDTH,HEIGHT))

class Player(pygame.sprite.Sprite):
    COLOR = (0,0,0)
    def __init__(self,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
    def move(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
    def move_left(self,vel):
        self.x_vel = vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
    def move_right(self,vel):
        self.x_vel = -vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
    def loop(self,fps):
        self.move(self.x_vel,self.y_vel)
    def draw(self,win):
        pygame.draw.rect(win,self.COLOR,self.rect)

def get_background(image_name):
    image = pygame.image.load(join("background",image_name))
    _,_,width,height = image.get_rect()
    tiles = []
    for row in range(WIDTH//width+1):
        for column in range(HEIGHT//height+1):
            pos = (row*width,column*height)
            tiles.append(pos)
    print(width,height)
    print(tiles)
    return tiles,image

def draw(window,background,bg_image,player):
    for tile in background:
        window.blit(bg_image,tile)
    player.draw(window)
    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    run = True
    background,bg_image = get_background("Yellow.png")
    player = Player(100,100,80,80)
    while run:
        clock.tick(FBS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw(window,background,bg_image,player)
    pygame.quit()


if __name__ == "__main__":
    main(window)



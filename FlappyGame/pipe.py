import pygame
import random
from defs import *

class Pipe():
    def __init__(self, screen, x, y, pipeType):
        self.screen = screen
        self.state = pipeMoving
        self.pipeType = pipeType
        self.img = pygame.image.load(pipeFileName)
        self.rect = self.img.get_rect()
        self.setPosition(x, y)
        print('pipeMoving')

    def setPosition(self, x, y):
        self.rect.left = x
        self.rect.top = y

    def movePosition(self, dx, dy):
        self.rect.centerx += dx
        self.rect.centery += dy

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def checkStatus(self):
        if self.rect.right < 0:
            self.state = pipeDone
            print('pipeDone')
    def update(self, dt):
        if self.state == pipeMoving:
            self.movePosition(-(pipeSpeed * dt), 0)
            self.draw()
            self.checkStatus()

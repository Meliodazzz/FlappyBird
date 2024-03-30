import pygame
import random
from settings import *

class Pipe():
    def __init__(self, screen, x, y, pipeType):
        self.screen = screen
        self.state = pipeMoving
        self.pipeType = pipeType
        self.img = pygame.image.load(pipeFileName)
        self.rect = self.img.get_rect()
        if pipeType == pipeUpper:
            y = y - self.rect.height
        self.setPosition(x, y)

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

    def update(self, dt):
        if self.state == pipeMoving:
            self.movePosition(-(pipeSpeed * dt), 0)
            self.draw()
            self.checkStatus()

class pipeCollection():
    def __init__(self, screen):
        self.screen = screen
        self.pipes = []

    def addNewPipePair(self, x):
        topY = random.randint(pipeMin, pipeMax - pipeGapSize)
        bottomY = topY + pipeGapSize

        p1 = Pipe(self.screen, x, topY, pipeUpper)
        p2 = Pipe(self.screen, x, bottomY, pipeLower)

        self.pipes.append(p1)
        self.pipes.append(p2)

    def createNewSet(self):
        self.pipes = []
        placed = pipeFirst

        while placed < displayWidth:
            self.addNewPipePair(placed)
            placed += pipeAddGap

    def update(self, dt):
        rightMost = 0

        for p in self.pipes:
            p.update(dt)
            if p.pipeType == pipeUpper:
                if p.rect.left > rightMost:
                    rightMost = p.rect.left

        if rightMost < (displayWidth - pipeAddGap):
            self.addNewPipePair(displayWidth)

        self.pipes = [p for p in self.pipes if p.state == pipeMoving]
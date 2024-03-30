import pygame
from settings import *
from pipe import pipeCollection



def update_label(data, title, font, x, y, screen):
    label = font.render('{}: {}'.format(title, data), 1, dataFontColor)
    screen.blit(label, (x, y))
    return y

def update_data_labels(screen, dt, gameTime, font):
    yPos = 10
    xPos = 10
    gap = 20
    yPos = update_label(round(1000/dt, 2), 'FPS', font, xPos, yPos + gap, screen)
    yPos = update_label(round(gameTime/1000, 2), 'Game Time', font, xPos, yPos + gap, screen)

def runGame():
    pygame.init()
    screen = pygame.display.set_mode((displayWidth, displayHeight))
    pygame.display.set_caption("Flappy Bird")

    running = True
    bgImage = pygame.image.load(bgFileName)
    pipes = pipeCollection(screen)
    pipes.createNewSet()

    label_font = pygame.font.SysFont("monospace", dataFontSize)

    clock = pygame.time.Clock()
    dt = 0
    gameTime = 0


    while running:
        dt = clock.tick(FPS)
        gameTime += dt

        screen.blit(bgImage, (0,0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False

        update_data_labels(screen, dt, gameTime, label_font)
        pipes.update(dt)

        pygame.display.update()

if __name__ == "__main__":
    runGame()


pygame.quit()
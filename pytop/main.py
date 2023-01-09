import pygame
from pygame.locals import *
from color import *
from keymanager import Keymanager
from spawner import Spavner
from object import ObjectOM
from ui import UiText, DisplayPosition
from settings import *
from road import Road



#
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT), RESIZABLE)
pygame.display.set_caption(NAME)

clock = pygame.time.Clock()

road = Road(screen)

manager = Keymanager()
spavner = Spavner(screen)
spavner.setLines(road.getLines())

# player
box = ObjectOM(screen)
box.setRed()
box.setLines(road.getLines())
box.playerInitPosition()

isActive = True
count = 0

#score text
score = UiText()
score.setColor(DARKORANGE2)

#game_over text
game_over = UiText('Game Over', DisplayPosition.CENTER)
game_over.setColor(RED4)
game_over.setFontSize(120)


while isActive:
    #lock fps
    clock.tick(fps)

    #events
    for event in pygame.event.get():
        if event.type == QUIT:
            isActive = False

        if event.type == VIDEORESIZE:
            if event.h > HEIGHT_MIN and event.h < HEIGHT_MAX:
                HEIGHT = event.h
            if event.w > WIDTH_MIN and event.w < WIDTH_MAX:
                WIDTH = event.w
            screen = pygame.display.set_mode((WIDTH,HEIGHT), RESIZABLE)
            screen.fill(COLOR)
            pygame.display.flip()
            continue

        if event.type == add_score and box.alive == True:
            count += 1
            if count % 5 == 0:
                road.appendSpeed()

        if event.type == KEYDOWN:
            manager.event(event)
            if event.key == K_1:
                box.setRed()
            if event.key == K_2:
                box.setBlue()
            if event.key == K_3:
                box.setYellow()

            # cheats
            if event.key == K_b:
                box.bordered = not box.bordered
            if event.key == K_f:
                road.appendSpeed()
            if event.key == K_UP:
                count += 1

            # player move
            if event.key == K_d or event.key == K_RIGHT:
                box.move('right')
            if event.key == K_a or event.key == K_LEFT:
                box.move('left')
            
            if event.key == K_ESCAPE:
                isActive = False
    # fill background color
    screen.fill(COLOR)
    score_text = 'Score: ' + str(count)
    score.setText(score_text)

    road.render()

    box.draw()
    spavner.invoke()
    spavner.draw()
    is_crash = spavner.collisions(box.collision)
    if is_crash:
        box.alive = False

    score.render(screen)
    if box.alive == False:
        game_over.render(screen)

    pygame.display.update()

pygame.quit()
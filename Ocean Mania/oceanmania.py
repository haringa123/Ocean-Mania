import pygame as pg
import sys
from pygame.locals import *
# from pygame import display, time, mixer, Surface, MOUSEBUTTONDOWN
from os import path
pg.mixer.pre_init(44100, 16, 2, 4096)
pg.init()
clock = pg.time.Clock()

#=====================================================================================================================
#screen 
screen = pg.display.set_mode((1000,800))
pg.display.set_caption("Ocean Mania")
mainbg = pg.image.load('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/2248.jpg')
mainbg = pg.transform.scale(mainbg, (1000,800))
bg = pg.image.load('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/Seabed Free Vector2.jpg')
bg = pg.transform.scale(bg, (2800,2583))
title = pg.image.load('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/title.png')
title = pg.transform.scale(title, (650,650))
# game_icon = pygame.image.load('coin.png')
# pygame.display.set_icon(game_icon)

#buttons
start_button = pg.image.load('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/Start.png')
scores_button = pg.image.load('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/Scores.png')
start_button2 = pg.image.load('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/Start2.png')
scores_button2 = pg.image.load('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/Scores2.png')

#Playerfish
PL15 = pg.image.load('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/player/L1.png').convert()
PL24 =pg.image.load('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/player/L2.png').convert()
PL3 =pg.image.load('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/player/L3.png').convert()
PL6=pg.image.load('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/player/L6.png').convert()
PL15 = pg.transform.scale(PL15, (222,70))
PL24 = pg.transform.scale(PL24, (222,70))
PL3 = pg.transform.scale(PL3, (222,70))
PL6 = pg.transform.scale(PL6, (222,70))
PR15 = pg.transform.flip(PL15,True,False)
PR24 =pg.transform.flip(PL24,True,False)
PR3 =pg.transform.flip(PL3,True,False)
PR6= pg.transform.flip(PL6,True,False)
#LONGER, BUT FASTER?
# PR15.set_colorkey((0, 0, 0))
# PR24.set_colorkey((0, 0, 0))
# PR3.set_colorkey((0, 0, 0))
# PR24.set_colorkey((0, 0, 0))
# PR6.set_colorkey((0, 0, 0))
# PL15.set_colorkey((0, 0, 0))
# PL24.set_colorkey((0, 0, 0))
# PL3.set_colorkey((0, 0, 0))
# PL24.set_colorkey((0, 0, 0))
# PL6.set_colorkey((0, 0, 0))
swimright = [PR15,PR24,PR3,PR24,PR15,PR6]
swimleft = [PL15,PL24,PL3,PL24,PL15,PL6]
#SHORTER BUT SLOWER :(
for a in swimright:
    a.set_colorkey((0,0,0))
for a in swimleft:
    a.set_colorkey((0,0,0))
swimframe = 0
facing = ""

#But when calling the function it desn't work
# def swim():
#     global swimframe, facing, mx,my
    # if swimframe + 1 >= 12:
    #     swimframe = 0
    # pg.display.update()
    # if facing == "right":
    #     screen.blit(swimright[swimframe//3], (mx-150,my-50))
    #     swimframe += 1
    # elif facing == "left":
    #     screen.blit(swimleft[swimframe//3], (mx-150,my-50))
    #     swimframe += 1

#stats
score = 0000
lives = 10
growthlevel = 0

#Fonts
Titlefont = pg.font.Font('fonts/Sketch 3D.otf', 20)
Statsfont = pg.font.Font('fonts/Hanged Letters.ttf', 40)
GameOverfont = pg.font.Font('fonts/Corrupted File.ttf', 20)
NumbersWordsfont = pg.font.Font('fonts/YesterdayDream.otf', 20)
stats = Statsfont.render(("Score: " + str(score) + "                 " + "Lives: x" + str(lives) + "                 " + "Growth level: " + str(growthlevel)), True, (0,0,0))

#Sounds
# woosh = pg.mixer.Sound('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/sounds/whip-whoosh-03.wav')

#scrolling stuff
bgy=0
bgx=0
boost = 0
bgrect = bg.get_rect()
mx, my = pg.mouse.get_pos()
#=====================================================================================================================

#Main menu
def main_menu():
    main = True
    while main:
        pg.time.delay(100)
        mx, my = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        screen.fill((0,128,128))
        screen.blit(mainbg, (0,0))
        screen.blit(title, (100, 50))
        screen.blit(start_button, (750, 300))
        screen.blit(scores_button, (750, 400))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        #start button
        if start_button.get_rect(center = (850,340)).collidepoint(mx,my):
            if click[0] ==  1:
               game()
            screen.blit(start_button2, (750,300))
        else:
            screen.blit(start_button, (750, 300))
        #score button
        if scores_button.get_rect(center = (850,440)).collidepoint(mx,my):
            screen.blit(scores_button2, (750,400))
            # if click[0] ==  1:
        else:
            screen.blit(scores_button, (750, 400))

        pg.display.update()
        clock.tick(60)

#Game loop
def game():
    running = True
    while running:
        global bgy, bgx, boost, bgrectx, bgrecty, facing, swimframe
        clock.tick(60)
        mx, my = pg.mouse.get_pos()

        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                boost = 15
            if event.type == MOUSEBUTTONUP:
                boost = 0

        #Player and animation
        x,y = pg.mouse.get_rel()
        x2,y2 = pg.mouse.get_rel()
        if swimframe + 1 >= 60:
            swimframe = 0
        if x2 <= x:
            facing == "right"
            screen.blit(swimright[swimframe//10], (mx-150,my-50))
            swimframe += 1
            pg.display.update()
        elif x2 >= x:
            facing == "left"
            screen.blit(swimleft[swimframe//10], (mx-150,my-50))
            swimframe += 1
            pg.display.update()
        


        # print(bgrectx, bgrecty)
        # if bgrectx > 1400:
        #     bgx += 1 
        #     # print("too far left")
        # elif bgrectx <1000:
        #     bgx -= -1
        #     # print("too far right")
        # if bgrecty <800:
        #     bgy += 1
        #     # print("too far down")
        # elif bgrecty>1671:
        #     bgy += -1
        #     # print("too far up")

        #Scroll Limits
        bgrectx = 2800 + bgx
        bgrecty = 2483 + bgy
        #scrolly
        if my < 350 and bgrecty<2483:
            bgy += 6 + boost
        elif my > 450 and bgrecty>800:
            bgy += -6 - boost
                #scrollx
        if mx < 350 and bgrectx <2800:
            bgx += 6 + boost
        elif mx > 650 and bgrectx >1000:
            bgx += -6 - boost


        screen.fill((0,0,0))
        screen.blit(bg, (bgx,bgy))
        screen.blit(stats, (40,0))
        pg.display.update()
        # clock.tick(60)
        

main_menu()
import sys, pygame, os, time, random
from math import pi

class Button:
    def __init__(msg,x,y,w,h,pictureIdle,pictureHover,pictureClick,action):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(click)
        #print(mouse)
        if x+w > mouse[0] > x and y+h > mouse[1]:
            #Hover button
            screen.blit(pictureHover,(x,y,w,h))
            if click[0] == 1:
                #pressed button
                #print(msg,x,y,w,h)
                screen.blit(pictureClick,(x,y,w,h))
                action()       
        else:
            #print("no click") Idle button
            screen.blit(pictureIdle,(x,y,w,h))

        pixelText = pygame.font.Font("BACKTO1982.ttf",20)
        textSurf, textRect = text_objects(msg, pixelText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)
        
    def text_objects(text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()
    
    #example button
    #button("START",320, 500, 100, 50, buttonStartIdle,buttonStartHover,buttonStartClick,start)



import sys, pygame, os, time, random
from math import pi

print (os.getcwd())

# Initialize the game engine
pygame.init()
 

# Set the height and width of the screen
size = [1280, 704]
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Example code for the draw module")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

#Main loop
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
     
    for event in pygame.event.get(): # User did something
        
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background and import images
    #background must draw at first
    background = pygame.image.load('background.png')
    buttonStartIdle = pygame.image.load('buttonIdle.png')
    buttonStartHover = pygame.image.load('buttonHover.png')
    buttonStartClick = pygame.image.load('buttonClick.png')


    screen.blit(background, [0,0])
##    screen.blit(buttonStart,[200,200,1000,1000])
##    pygame.display.flip()



    def start():
        pygame.draw.rect(screen,GREEN,[100,100,100,100])
        if True:
            print("0")
        #this is a example for main game loop
        
    def levelSelect():
        None



    #all about button


    
    def button(msg,x,y,w,h,pictureIdle,pictureHover,pictureClick,action):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(click)
        print(mouse)
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            #hover button
            print("Hover")
            screen.blit(pictureHover,(x,y,w,h))
            if click[0] == 1:
                #pressed button
                #print(msg,x,y,w,h)
                screen.blit(pictureClick,(x,y,w,h))
                action()
        #Idle button
                
        else:
            #print("no click")
            screen.blit(pictureIdle,(x,y,w,h))

        pixelText = pygame.font.Font("BACKTO1982.ttf",20)
        textSurf, textRect = text_objects(msg, pixelText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)




        

    def text_objects(text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()
    
    def mousePositionChecker(lis):
        if lis[0] + lis[2] > lis[0] > lis[0] and lis[1] + lis[3] > mouse[1] > lis[3]:
            return True
        else:
            return False 
        
    
    def highlighter(colorTup):
        light_list = [x+25 for x in list(colorTup)]
        vaild_list = [max(min(x, 255), 0) for x in light_list]       
        return tuple(vaild_list)
    
    button("START",220, 500, 200, 100, buttonStartIdle,buttonStartHover,buttonStartClick,start)
    button("QUIT",540, 500, 200, 100, buttonStartIdle,buttonStartHover,buttonStartClick,quit)
    button("LEVEL",860, 500,200,100, buttonStartIdle,buttonStartHover,buttonStartClick,levelSelect)
    






    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()


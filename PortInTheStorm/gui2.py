
import sys, pygame, os, time, random
from math import pi

print (os.getcwd())

# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 250)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [1280, 704]
screen = pygame.display.set_mode(size)
# Set the position and the size for the button
position1 = [640, 300, 100, 50]
 
pygame.display.set_caption("Example code for the draw module")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

#Main loop
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    background = pygame.image.load('example.jpg').convert()
    screen.blit(background, [0,0])









    #all about button
    def button(msg,x,y,w,h,ic,ac):
        mouse = pygame.mouse.get_pos()
        print(mouse)
        lis = [x,y,w,h]
        if x+w > mouse[0] > x and y+h > mouse[1]:
            pygame.draw.rect(screen, ac,(x,y,w,h))
        else:
            pygame.draw.rect(screen, ic,(x,y,w,h))

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
    
    button("go!",640, 300, 100, 50, BLUE,highlighter(BLUE))       











    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()


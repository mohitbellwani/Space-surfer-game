import random, pygame, sys
from random import *
from pygame.locals import *
import time

def play_end_animation():
    for i in range(4):
        DISPLAYSURF.fill(WHITE)
        pygame.display.update()
        pygame.time.wait(200)
        DISPLAYSURF.fill(BLACK)
        pygame.display.update()
        pygame.time.wait(200)
    done = "Game over! Your survived for %s seconds." % (counting_time)
    fontObj = pygame.font.SysFont('Ravie', 25)
    textSurfaceObj = fontObj.render(done , True, WHITE, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (760,400)
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    

def play_start_animation(filename, restart):
    if restart == True:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1)
    DISPLAYSURF.fill(BLACK)
    pygame.display.update()
    DISPLAYSURF.blit(three, (600,340))
    pygame.display.update()
    pygame.time.wait(1000)
    DISPLAYSURF.fill(BLACK)
    pygame.display.update()
    DISPLAYSURF.blit(two, (600,340))
    pygame.display.update()
    pygame.time.wait(1000)
    DISPLAYSURF.blit(one, (600,340))
    pygame.display.update()
    pygame.time.wait(1000)


    

FPS = 30
WINDOWWIDTH = 1520
WINDOWHEIGHT = 800
BOXSIZE = 50


RED = (255, 0, 0 )
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0 , 0 ,0 )
highscore = 0

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Space_Music.mp3')
pygame.mixer.music.play(-1)
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
three = pygame.image.load('3.jpg')
two = pygame.image.load('2.jpg')
one = pygame.image.load('1.jpg')




pygame.display.set_caption("Astroid Field!")
DISPLAYSURF.fill(WHITE)
box = []
coords = []
i = 0
click = False
restart = False
mouse = pygame.image.load('space.jpg')
mouse = pygame.transform.scale(mouse, (50, 50))
boom = pygame.image.load('BOOM.jpg')
boom = pygame.transform.scale(boom, (100,100))



start = "Using your mouse, you must navigate through the astroid"
start1= "field without hitting any of the incoming astroids."
start2 = "Click the screen to begin"
name = "created by        -Mohit Bellwani"
name1= "Computer Science Depaertment"
name2 = "Created using Python (Pygame)"
fontObj = pygame.font.SysFont('Ravie', 25)
fontObj1 = pygame.font.SysFont('Ravie', 40)
textSurfaceObj = fontObj.render(start , True, WHITE, BLACK)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (760,400)
DISPLAYSURF.blit(textSurfaceObj,textRectObj)
textSurfaceObj1 = fontObj.render(start1 , True, WHITE, BLACK)
textRectObj1 = textSurfaceObj.get_rect()
textRectObj1.center = (760,430)
DISPLAYSURF.blit(textSurfaceObj1,textRectObj1)
textSurfaceObj2 = fontObj.render(start2 , True, WHITE, BLACK)
textRectObj2 = textSurfaceObj2.get_rect()
textRectObj2.center = (760,460)
DISPLAYSURF.blit(textSurfaceObj2,textRectObj2)
textSurfaceObj3 = fontObj.render(name , True, WHITE, BLACK)
textRectObj3 = textSurfaceObj3.get_rect()
textRectObj3.center = (760,100)
DISPLAYSURF.blit(textSurfaceObj3,textRectObj3)
textSurfaceObj4 = fontObj1.render(name1 , True, WHITE, BLACK)
textRectObj4 = textSurfaceObj4.get_rect()
textRectObj4.center = (760,25)
DISPLAYSURF.blit(textSurfaceObj4,textRectObj4)
textSurfaceObj5 = fontObj1.render(name2 , True, WHITE, BLACK)
textRectObj5 = textSurfaceObj4.get_rect()
textRectObj5.center = (760,250)
DISPLAYSURF.blit(textSurfaceObj5,textRectObj5)


# Game starts here

pygame.display.update()

# to wait for mouse click to start
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            click = True
    if click == True:
        break


mousex = 400
mousey = 550
j = 0


play_start_animation('Space_Music.mp3', restart)
start_time = pygame.time.get_ticks()
while True:

    if restart == True:
        box = []
        coords = []
        i = 0
        click = False
        restart = False
        start_time = pygame.time.get_ticks()
        
    
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(mouse, (mousex-20, mousey))
    counting_time = (pygame.time.get_ticks() - start_time)/1000
    string = "Time: %s" % (counting_time)
    fontObj = pygame.font.SysFont('Bahaus 93', 35)
    textSurfaceObj = fontObj.render( string , True, WHITE, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (75,75)

    if highscore == 0:
        string1 = "Highscore: %s" % (counting_time)
    elif counting_time > highscore:
        string1 = 'Highscore %s' % (counting_time)
    else:
        string1 = "Highscore: %s" % (highscore)
        
    fontObj1 = pygame.font.SysFont('Bahaus 93', 35)
    textSurfaceObj1 = fontObj1.render(string1 , True, WHITE, BLACK)
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj1.center = (100,100)
    x = randrange(0,1540)
    y = randrange(0,1)

    # this loop prevents the degredation of performance. When the lists were getting
    # too big (around 15 seconds) the program began running slowly. 
    if i%100 == 0 and i!= 0:
        del coords [:30]
        del box [:30]
        i -= 30
        j -= 30
        
    
    box.append(pygame.Rect(x, y, BOXSIZE, BOXSIZE))

    point1 = list(box[i].bottomleft)
    point2 = list(box[i].bottomright)
    coords.append([point1,point2])
    
    pygame.time.wait(10)
    for j in range(len(box)):

        if restart == True:
            break
    
        pygame.draw.rect(DISPLAYSURF, BLUE, box[j])
        box[j].centery +=10
        coords[j][0][1] +=10

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        DISPLAYSURF.blit(textSurfaceObj1,textRectObj1)
        if ( (coords[j][0][0]-15<= mousex <=coords[j][1][0]+7) and (coords[j][0][1]-10 <= mousey+30 <= coords[j][0][1])):
            pygame.mixer.music.stop()
            DISPLAYSURF.blit(boom, (mousex-20, mousey))
            pygame.mixer.music.load('explode1.mp3')
            pygame.mixer.music.play(-1)
            pygame.display.update()
            time.sleep(1.5) # wait and let the sound play for 1 second
            pygame.mixer.music.stop()
            
            play_end_animation()
            click = False
            while 1 and restart == False:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEMOTION:
                        mousex, mousey = event.pos

                again = "Play Again?" 
                fontObj1 = pygame.font.SysFont('Ravie', 25)
                textSurfaceObj1 = fontObj1.render(again , True, WHITE, BLACK)
                textRectObj1 = textSurfaceObj1.get_rect()
                textRectObj1.center = (760,480)
                DISPLAYSURF.blit(textSurfaceObj1,textRectObj1)
                pygame.display.update()
                
                while (700<= mousex <= 1000 and 410<=mousey <=500) and restart == False:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == MOUSEMOTION:
                            mousex, mousey = event.pos
                        elif event.type == MOUSEBUTTONUP:
                            click = True
                            
                    again = "Play Again?" 
                    fontObj1 = pygame.font.SysFont('Ravie', 25)         
                    textSurfaceObj1 = fontObj1.render(again , True, WHITE, BLUE)
                    textRectObj1 = textSurfaceObj1.get_rect()
                    textRectObj1.center = (760,480)
                    DISPLAYSURF.blit(textSurfaceObj1,textRectObj1)
                    pygame.display.update()

                    if click == True:
                        restart = True
                        highscore = counting_time
                        play_start_animation('Space_Music.mp3', restart)
                        start_time = 0
                        break
                    
                    else:
                        
                        continue
                   
            
             #pygame.quit()
             #sys.exit()
        
    i+=1
    #pygame.time.wait(500)
    pygame.display.update()
    FPSCLOCK.tick(FPS)




        

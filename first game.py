import pygame
import time
import random


pygame.init()
width=23232
height=2323


black=(0,0,0)
red=(252,0,0)
white=(252,252,252)

gamedisplay=pygame.display.set_mode((width,height))
pygame.display.set-caption("ya ya yay")
clock=pygame.time.Clock()
gamedisplay.fill(white)

carimage=pygame.image.load("  ")

def score_display(score):
    how=pygame.font.sysfont(None,30)
    scoreimage=how.render("SCORE:  "+str(score),true,black)
    gamedisplay.blit(scoreimage,(0,0))

def object(xposi,yposi,width,height,colour):
    pygame.draw.rect(gamedisplay,colour,[xposi,yposi,width,height])

def car(x,y):
    gamedisplay.blit(carimage,(x,y))


def finallldisplay(text,font):
    display=font.render(text,true,black)
    return display,display.get_rect()

def mess_display(text):
    textstyle=pygame.font.Font("type of font",size of font)
    mess_surface,mess_rectangle=finalldisplay(text,textstyle)
    mess_rectangle.center=((width/2),(height/2))
    gamedisplay.blit(mess_surface,mess_rectangle)
    pygame.display.update()


    time.sleep(2)
    carloop()



def crash():
    mess_display("You crashed")


def carloop():

    x=width*something
    y=height*something
    xposi=random.randrange(0,width)
    yposi=-500
    widthobj=100
    heightobj=100
    objspeed=7

    score=0

    gameexit=False

    while not gameexit:
            for event in pygame.event.get:
                if event.type == event.QUIT:
                   pygame.quit()
                   quit()


                if event.type ==pygame.KEYDOWN:
                    if event.type == pygame.K_LEFT:
                        x_change= -5
                    if event.type == pygame.K_RIGHT:
                        x_change= +5

                if event.type ==pygame.KEYUP:
                    if event.type == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                        x_change= 0

        x+ =x_change
        car(x,y)
        object(xposi,yposi,widthobj,heightobj,black)
        yposi+=objspeed

        if x <0 or x>width-carwidth:
                    crash()


        if yposi>height:
            yposi=0-heightobj
            xposi=random.randrange(0,width)
            score+=1

        if y<yposi+height:
            if x<xposi+widthobj and x+widthobj>xposi:
                crash()

    


        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

        

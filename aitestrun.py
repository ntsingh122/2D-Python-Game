#Game y Me <)
#ant w*h=150*250
#things w*h=180*100


import pygame
import time
import random

pygame.init()

crsound=pygame.mixer.Sound('sound/wallhit.wav')
lane=pygame.mixer.Sound('sound/lane.wav')
pygame.mixer.music.load('sound/main.wav')

white= (204, 230, 255)
kaala=(20, 20, 12)
red=(255,0,0)
w=800
h=600
cw=150
ch=250
tw=180
th=100


gameDis=pygame.display.set_mode((w,h))
pygame.display.set_caption('Idiot AnB')
#ITS like refreshing rate
clk=pygame.time.Clock()
pause=True

img= pygame.image.load('images/ant.png')
over= pygame.image.load('images/gover.png')
gwd=150
#characters image array
thing=[pygame.image.load('images/im (1).png'),pygame.image.load('images/im (2).png'),pygame.image.load('images/im (3).png'),pygame.image.load('images/im (4).png'),pygame.image.load('images/im (5).png'),pygame.image.load('images/im (6).png'),pygame.image.load('images/im (7).png')]

def gameHd(caption):
    pygame.display.set_caption(caption)    

def tdodge(count):
    strin='SCORE : '+str(count)
    msg(strin,0,0,30,red)
    

def msg(text,posx,posy,f_size,clr):
    font =pygame.font.SysFont(None,f_size)
    text1=font.render(text,True,clr)
    gameDis.blit(text1,(posx,posy))
    pygame.display.update()
    
#def pause():
#    while pause:
        
#        msg=('Game paused press space again to start!',50,h/2

def idiot(x,y):
    gameDis.blit(img,(x,y))
    
def things(thingx,thingy,thingty): #tn=thing numer
    gameDis.blit(thingty,(thingx,thingy))
    
    

def gameOver(typeof,dodge):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crsound)
    time.sleep(1)
    text="You Crashed into "+typeof+"! Your score :  "+str(dodge)
    msg(text,20,h/2,55,red)
    gameHd("GAme Over !"+"\U0001F622")
    time.sleep(1)
    msg('Do you want to Play again?press Y or N',10,h/4,40,red)
    time.sleep(3)
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_y:
                game()
            if event.key==pygame.K_n:
                gameDis.blit(over,(0,0))
                pygame.display.update()
                time.sleep(1)
                #game()
                pygame.quit()
                quit()
	

def game():
    fll=w/16            #first left limit for rectangular strip
    sll= (6*w)/16       #second left limit for same
    tll=(11*w)/16
    pygame.mixer.music.play(-1)
    #x and y co ordinates of girl character
    x= sll+50
    y=h*0.8
    dodge=0
    thingstartx=random.choice([sll,fll,sll,tll])
    thingstarty=-600
    thingspeed=3
    thingnum=random.choice(thing)

    crashed= False
    while not crashed:
        #pygame.mixer.music.play(-1) 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed= True
            #print(event)
            if event.type==pygame.KEYDOWN:
                #pygame.mixer.Sound.play(lane)
                if event.key==pygame.K_LEFT:
                    pygame.mixer.Sound.play(lane)
                    x-=250
                if event.key==pygame.K_RIGHT:
                    pygame.mixer.Sound.play(lane)
                    x+=250

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x=x

        gameDis.fill(white)  #use to display the white ackground
        pygame.draw.rect(gameDis, kaala, [fll, 0, w/4,h], 0)
        pygame.draw.rect(gameDis, kaala, [sll, 0, w/4,h], 0)
        pygame.draw.rect(gameDis, kaala, [tll, 0, w/4,h], 0)
        #things(thingx,thingy,tn)
        things(thingstartx,thingstarty,thingnum)
        thingstarty += thingspeed


        idiot(x,y)
        tdodge(dodge)

        if x<-50 or x>w-(gwd/2):
            #msg(text,posx,posy,f_size,clr):
            gameOver(" Wall",dodge)

        if thingstarty > h:
            dodge+=1
            thingspeed+=0.3
            thingstarty = 0-th
            thingstartx=random.choice([fll,sll,tll])
            thingnum=random.choice(thing)
            #print(thingspeed)
            
        if thingstarty+th-20 > y and x==thingstartx+50 :
            if thingstartx==fll :
                x+=250
            if thingstartx==sll:
                x=random.choice([x+250,x-250])
            if thingstartx==tll:
                x-=250
            gameOver(" enemy",dodge)
                
        pygame.display.update()
        clk.tick(120)
game()
event=pygame.event.get()
print (event)
pygame.quit()
quit()

        

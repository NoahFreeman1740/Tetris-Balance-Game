from html import escape
from numpy import disp, pi
import pygame, random
pygame.init()

#Setup
white = (255,255,255)
whiteshaded = (230,230,230)
black = (0,0,0)
gray = (120,120,120)
green = (21,209,24)
greenshaded = (30,179,33)
piecered = (230,21,59)
pieceorange = (252,149,23)
pieceyellow = (237,201,21)
piecegreen = (30,209,27)
piecelightblue = (46,169,240)
pieceblue = (46,56,240)
piecepurple = (217,46,240)
whiteshaded = (210,210,210)

bigfont = pygame.font.SysFont('impact', 100)    #font
midfont = pygame.font.SysFont('impact', 75)    #menufont
smallfont = pygame.font.SysFont('impact', 40)  #datefont
size = (900, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris Balance")
clock = pygame.time.Clock()
mouse = pygame.mouse.get_pos()
startbuttonrect = pygame.Rect(350,400,200,100)
playagainbuttonrect = pygame.Rect(200,400,200,100)
endbuttonrect = pygame.Rect(500,400,200,100)
onebuttonrect = pygame.Rect(300, 300, 50, 50)
twobuttonrect = pygame.Rect(500, 300, 50, 50)
threebuttonrect = pygame.Rect(300, 500, 50, 50)
fourbuttonrect = pygame.Rect(500, 500, 50, 50)
startcirclerect = pygame.Rect(350,250,200,200)
nextbuttonrect = pygame.Rect(650, 300, 200, 75)
topplebuttonrect = pygame.Rect(25, 300, 200, 75)
running = True
running2 = True





#Functions

def homescreengraphics():
    startimg = pygame.image.load("Blue_Background.jpg")
    startimg = pygame.transform.scale(startimg,(900,600)) 
    screen.blit(startimg, (0,0))
    titlestartx = 150
    screen.blit(bigfont.render('T', True, piecered),(titlestartx,10))
    screen.blit(bigfont.render('e', True, pieceorange),(titlestartx+40,10))
    screen.blit(bigfont.render('t', True, pieceyellow),(titlestartx+90,10))
    screen.blit(bigfont.render('r', True, piecegreen),(titlestartx+120,10))
    screen.blit(bigfont.render('i', True, piecelightblue),(titlestartx+155,10))
    screen.blit(bigfont.render('s', True, piecepurple),(titlestartx+180,10))
    screen.blit(bigfont.render('Balance', True, white),(titlestartx+250,10))
    pygame.display.flip()

def startbutton(backgroundcolor):
    pygame.draw.rect(screen, backgroundcolor, pygame.Rect(350, 400, 200, 100),  0, 5)
    pygame.draw.rect(screen, black, pygame.Rect(350, 400, 200, 100),  3, 5)
    screen.blit(midfont.render('Start', True, black),(373,405))

def playagainbutton(backgroundcolor):
    pygame.draw.rect(screen, backgroundcolor, pygame.Rect(200, 400, 200, 100),  0, 5)
    pygame.draw.rect(screen, black, pygame.Rect(200, 400, 200, 100),  3, 5)
    screen.blit(smallfont.render('Play Again', True, black),(215,423))

def endbutton(backgroundcolor):
    pygame.draw.rect(screen, backgroundcolor, pygame.Rect(500, 400, 200, 100),  0, 5)
    pygame.draw.rect(screen, black, pygame.Rect(500, 400, 200, 100),  3, 5)
    screen.blit(smallfont.render('End', True, black),(570,423))

def onebutton(backgroundcolor):
    pygame.draw.rect(screen, backgroundcolor, pygame.Rect(300, 300, 50, 50),  0, 5)
    pygame.draw.rect(screen, black, pygame.Rect(300, 300, 50, 50),  3, 5)
    screen.blit(smallfont.render('1', True, black),(315,300))

def twobutton(backgroundcolor):
    pygame.draw.rect(screen, backgroundcolor, pygame.Rect(500, 300, 50, 50),  0, 5)
    pygame.draw.rect(screen, black, pygame.Rect(500, 300, 50, 50),  3, 5)
    screen.blit(smallfont.render('2', True, black),(515,300))

def threebutton(backgroundcolor):
    pygame.draw.rect(screen, backgroundcolor, pygame.Rect(300, 500, 50, 50),  0, 5)
    pygame.draw.rect(screen, black, pygame.Rect(300, 500, 50, 50),  3, 5)
    screen.blit(smallfont.render('3', True, black),(315,500))

def fourbutton(backgroundcolor):
    pygame.draw.rect(screen, backgroundcolor, pygame.Rect(500, 500, 50, 50),  0, 5)
    pygame.draw.rect(screen, black, pygame.Rect(500, 500, 50, 50),  3, 5)
    screen.blit(smallfont.render('4', True, black),(515,500))

def startcircle(backgroundcolor):
    pygame.draw.circle(screen, backgroundcolor, (450,350), 100, 100)
    pygame.draw.circle(screen, gray, (450,350), 110, 10)
    screen.blit(midfont.render('Start!', True, white),(365,300))

def nextbutton(backgroundcolor):
    pygame.draw.rect(screen, backgroundcolor, pygame.Rect(650, 300, 200, 75),  0, 5)
    pygame.draw.rect(screen, black, pygame.Rect(650, 300, 200, 75),  3, 5)
    screen.blit(smallfont.render('Next Piece', True, black),(665,309))

def topplebutton(backgroundcolor):
    pygame.draw.rect(screen, backgroundcolor, pygame.Rect(25, 300, 200, 75),  0, 5)
    pygame.draw.rect(screen, black, pygame.Rect(25, 300, 200, 75),  3, 5)
    screen.blit(smallfont.render('Toppled!', True, black),(50,309))

def addpiece(piecetype):
    if piecetype == 0:
        pygame.draw.rect(screen, piecepurple, pygame.Rect(325,325,150,50))
        pygame.draw.rect(screen, piecepurple, pygame.Rect(375,375,50,50))
    elif piecetype == 1:
        pygame.draw.rect(screen, pieceyellow, pygame.Rect(350,325,100,100))
    elif piecetype == 2:
        pygame.draw.rect(screen, piecelightblue, pygame.Rect(375,275,50,200))
    elif piecetype == 3:
        pygame.draw.rect(screen, piecegreen, pygame.Rect(325,375,100,50))
        pygame.draw.rect(screen, piecegreen, pygame.Rect(375,325,100,50))
    elif piecetype == 4:
        pygame.draw.rect(screen, piecered, pygame.Rect(325,325,100,50))
        pygame.draw.rect(screen, piecered, pygame.Rect(375,375,100,50))
    elif piecetype == 5:
        pygame.draw.rect(screen, pieceorange, pygame.Rect(350,300,50,150))
        pygame.draw.rect(screen, pieceorange, pygame.Rect(400,400,50,50))
    elif piecetype == 6:
        pygame.draw.rect(screen, pieceblue, pygame.Rect(400,300,50,150))
        pygame.draw.rect(screen, pieceblue, pygame.Rect(350,400,50,50))



def tetrisgame():
    homescreengraphics()
    screen.blit(smallfont.render('How many of each piece?', True, white),(225,200))
    normimg = pygame.image.load("normal.png")
    normimg = pygame.transform.scale(normimg,(50,50)) 
    screen.blit(normimg, (240,300))
    hardimg = pygame.image.load("hard.png")
    hardimg = pygame.transform.scale(hardimg,(50,50)) 
    screen.blit(hardimg, (560,300))
    harderimg = pygame.image.load("harder.png")
    harderimg = pygame.transform.scale(harderimg,(50,50)) 
    screen.blit(harderimg, (240,500))
    insaneimg = pygame.image.load("insane.png")
    insaneimg = pygame.transform.scale(insaneimg,(50,50)) 
    screen.blit(insaneimg, (560,500))
    running4 = True
    while running4 == True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 <= mouse[0] <= 350 and 300 <= mouse[1] <= 350:
                    piececount = 1
                    running4 = False
                if 500 <= mouse[0] <= 550 and 300 <= mouse[1] <= 350:
                    piececount = 2
                    running4 = False
                if 300 <= mouse[0] <= 350 and 500 <= mouse[1] <= 550:
                    piececount = 3
                    running4 = False
                if 500 <= mouse[0] <= 550 and 500 <= mouse[1] <= 550:
                    piececount = 4
                    running4 = False

        if onebuttonrect.collidepoint(mouse):
            onebutton(whiteshaded)
        else:
            onebutton(white)
        
        if twobuttonrect.collidepoint(mouse):
            twobutton(whiteshaded)
        else:
            twobutton(white)
        
        if threebuttonrect.collidepoint(mouse):
            threebutton(whiteshaded)
        else:
            threebutton(white)

        if fourbuttonrect.collidepoint(mouse):
            fourbutton(whiteshaded)
        else:
            fourbutton(white)
        
        pygame.display.flip()
        clock.tick(30)
    
    homescreengraphics()
    running5 = True
    while running5 == True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 350 <= mouse[0] <= 550 and 250 <= mouse[1] <= 450:
                    running5 = False
        
        if startcirclerect.collidepoint(mouse):
            startcircle(greenshaded)
        else:
            startcircle(green)
        
        pygame.display.flip()
        clock.tick(30)
    
    
    running6 = True
    if piececount == 4:
        piecelist = [4,4,4,4,4,4,4]
    elif piececount == 3:
        piecelist = [3,3,3,3,3,3,3]
    elif piececount == 2:
        piecelist = [2,2,2,2,2,2,2]
    else:
        piecelist = [1,1,1,1,1,1,1]
    piecetotal = piececount * 7
    currentpiece = 1
    mindig = 0
    secdig = 0
    seccount = 0
    startticks = pygame.time.get_ticks()
    piecetype = random.randint(0,6)
    while piecetype == 2:
        piecetype = random.randint(0,6)
    piecelist[piecetype] -= 1
    while running6 == True:
        homescreengraphics()
        mouse = pygame.mouse.get_pos()
        gamepercent = int(100*(currentpiece/piecetotal))
        screen.blit(midfont.render(str(gamepercent)+'%', True, white),(685,450))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 25 <= mouse[0] <= 225 and 300 <= mouse[1] <= 375:
                    running6 = False
                    win = False
                elif 650 <= mouse[0] <= 850 and 300 <= mouse[1] <= 375:
                    if piecelist.count(0) == 7:
                        running6 = False
                        win = True
                    else:
                        pygame.draw.rect(screen, whiteshaded, pygame.Rect(250, 175, 300, 400),  0, 5)
                        pygame.draw.rect(screen, black, pygame.Rect(250, 175, 300, 400),  3, 5)
                        nextbutton(whiteshaded)
                        topplebutton(white)
                        screen.blit(midfont.render(str(gamepercent)+'%', True, white),(685,450))
                        if secdig<10:
                            screen.blit(smallfont.render(str(mindig)+':0'+str(secdig),True, white), (90,200))
                        else:
                            screen.blit(smallfont.render(str(mindig)+':'+str(secdig), True, white), (90,200))
                        pygame.draw.rect(screen, piecegreen, pygame.Rect(0,585,(int(900*(currentpiece/piecetotal))),10))
                        pygame.display.flip()
                        pygame.time.wait(250)
                        currentpiece += 1
                        randint = random.randint(0,6)
                        while piecelist[randint] == 0:
                            randint = random.randint(0,6)
                        piecetype = randint
                        piecelist[piecetype] -= 1

        if nextbuttonrect.collidepoint(mouse):
            nextbutton(whiteshaded)
        else:
            nextbutton(white)
        
        if topplebuttonrect.collidepoint(mouse):
            topplebutton(whiteshaded)
        else:
            topplebutton(white)

        pygame.draw.rect(screen, piecegreen, pygame.Rect(0,585,(int(900*(currentpiece/piecetotal))),10))

        pygame.draw.rect(screen, white, pygame.Rect(250, 175, 300, 400),  0, 5)
        pygame.draw.rect(screen, black, pygame.Rect(250, 175, 300, 400),  3, 5)
        addpiece(piecetype)

        
        seccount = int(((pygame.time.get_ticks())-startticks)/1000)
        secdig = seccount%60
        mindig = int(seccount/60)
        if secdig<10:
            screen.blit(smallfont.render(str(mindig)+':0'+str(secdig),True, white), (90,200))
        else:
            screen.blit(smallfont.render(str(mindig)+':'+str(secdig), True, white), (90,200))

        pygame.display.flip()
        clock.tick(30)
    return(win,seccount)



#Main
homescreengraphics()
while running == True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 350 <= mouse[0] <= 550 and 400 <= mouse[1] <= 500:
                    running = False
    
    if startbuttonrect.collidepoint(mouse):
        startbutton(whiteshaded)
    else:
        startbutton(white)

    pygame.display.flip()
    mouse = pygame.mouse.get_pos()
    clock.tick(30)

homescreengraphics()
while running2 == True:
    running3 = True

    results = tetrisgame()
    win = results[0]
    seccount = results[1]
    secdig = seccount%60
    mindig = int(seccount/60)
    homescreengraphics()
    if secdig<10:
        screen.blit(smallfont.render('Your time was '+str(mindig)+':0'+str(secdig),True, white), (298,310))
    else:
        screen.blit(smallfont.render('Your time was '+str(mindig)+':'+str(secdig), True, white), (298,310))
    if win:
        screen.blit(midfont.render('You won!', True, white),(315,200))
        
    else:
        screen.blit(midfont.render('Better luck next time!', True, white),(120,200))

    while running3 == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 200 <= mouse[0] <= 400 and 400 <= mouse[1] <= 500:
                    running3 = False
                if 500 <= mouse[0] <= 700 and 400 <= mouse[1] <= 500:
                    quit()
        
        if playagainbuttonrect.collidepoint(mouse):
            playagainbutton(whiteshaded)
        else:
            playagainbutton(white)

        if endbuttonrect.collidepoint(mouse):
            endbutton(whiteshaded)
        else:
            endbutton(white)

        pygame.display.flip()
        mouse = pygame.mouse.get_pos()
        clock.tick(30)
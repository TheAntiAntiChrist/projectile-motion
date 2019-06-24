import pygame
import suvat

sX,uX,vX,sY,uY,vY,aY,t = suvat.genDebugValues()
init_uY = uY
print("sX,uX,vX,sY,uY,vY,aY,t")
print(sX,uX,vX,sY,uY,vY,aY,t)

fontSize = 18
skyBlue = [100,100,180]
white = [255,255,255]
black = [0,0,0]
red = [255,50,50]

pygame.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("Projectile Motion")
myFont = pygame.font.SysFont("Consolas", fontSize)
axisFont = pygame.font.SysFont("Consolas", 10)

Done = False
clock = pygame.time.Clock()
debug = False

currentPos = [100,100] #[X,Y]

screen.fill(skyBlue)

def writeStats():
    vertVelText = myFont.render(("vertical velocity: " + str(round(uY,2))), True, black)
    horiVelText = myFont.render(("horizontal velocity: " + str(round(uX,2))), True, black)
    vertAclText = myFont.render(("vertical acceleration: " + str(round(aY,2))), True, black)
    initVerVelText = myFont.render(("initial vert velocity: " + str(round(init_uY, 2))), True, black)
    timerText = myFont.render(("time: " + str(round(timer,2))), True, black)
    return vertVelText,horiVelText,vertAclText,initVerVelText,timerText

def isWithinBounds():
    if (currentPos[0] + uX/60) >= 100 and (currentPos[0] + uX/60) <= 500:
        if (currentPos[1] + uY/60) >= 100 and (currentPos[1] + uY/60) <= 500:
            return True
        else:
            return False
    else:
        return False
    #return True
timer = 0
pastPos = []
while not Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Done = True
            elif event.key == pygame.K_r:
                Done = True
    screen.fill(skyBlue)
    pygame.draw.line(screen, black, [100,100],[100,500]) #y-axis
    for y in range(5,26):
        pygame.draw.line(screen, black,[100,20*y],[90,20*y])
        yAxVals = axisFont.render(str(400-(20*y-100)), True, black)
        screen.blit(yAxVals, [65, 20*y-5])
    pygame.draw.line(screen, black, [100,500],[500,500]) #x-axis
    for x in range(5,26):
        pygame.draw.line(screen, black, [20*x,500],[20*x,510])
        xAxVals = axisFont.render(str(20*x-100), True, black)
        screen.blit(xAxVals, [20*x-5, 520])

    pastPos.append([round(currentPos[0]),round(600-currentPos[1])])
    if pastPos:
        counter = 0
        for coords in pastPos:
            counter += 1
            if counter == 20:
                pygame.draw.circle(screen, red, coords, 2, 0)
                counter = 0
    pygame.draw.circle(screen, white, [round(currentPos[0]),round(600-currentPos[1])], 4, 0)

    if debug is True:
        currentPos = [120,480]
    else:
        if isWithinBounds():
            currentPos[0] += uX/60 #60 to get movement per frame as program is capped @ 60fps
            currentPos[1] += uY/60
            uY += aY/60
            timer += 1/60

    y=0
    for values in writeStats():
        screen.blit(values, (0,y))
        y+=fontSize
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

from math import sqrt, cos, sin, radians

def genDebugValues():
    uM = 50
    angleM = radians(45)
    uX = uM*cos(angleM)
    uY = uM*sin(angleM)
    aY = -9.81
    vX = uX #No horizontal forces so the projectile's horizontal velocity doesn't change
    sY = 0 #No overall change in height
    t = uY/aY
    sX = uX * t
    vY = uY + aY*t

    return sX,uX,vX,sY,uY,vY,aY,t

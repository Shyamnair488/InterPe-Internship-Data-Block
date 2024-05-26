colors={"white":(255,255,255),
        "blue":(0,0,255),
        "red":(255,0,0),
        "green":(0,255,0)}


(widht,height)=(100,100)


def setup():
    global screen
    pygame.init()
    screen=pygame.display.set_mode((widht,height))
    pygame.display.set_caption("Finkel Circle")
    pygame.display.update()
        
def drawCircle(c):
    pygame.draw.circle(screen,
                       colors[c.color],
                       (c.coords.x,c.Coords.y),
                       c.radius,
                       not c.filled)
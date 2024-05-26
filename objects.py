import pygame

import Circle as c 

import drawCircles as d

running =True
d.setup()
while running:
    ev=pygame.event.get()
    
    for event in ev:
        
        if event.type == pygame.MOUSEBUTTONUP:
            
            pos=pygame.mouse.get_pos()
            
            c1=c.Circle()
            c1.radius=25
            c1.coords.x=pos[0]
            c1.coords.y=pos[1]
            c1.color="white"
            c1.filled=False
            
            d.drawCircle(c1)
            pygame.display.update()
            
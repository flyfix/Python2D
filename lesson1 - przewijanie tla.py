import sys, pygame, random, thread
pygame.init()


size = width, height = 800, 600
speedtlo = [-5, 0]

screen = pygame.display.set_mode(size)
 
tlo1 = pygame.image.load("files/tlo.bmp")
tlorect1 = tlo1.get_rect()
tlo2 = pygame.image.load("files/tlo.bmp")
tlorect2 = tlo2.get_rect()
tlorect2 = tlorect2.move([3000,0])

pygame.mouse.set_visible(0)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #### scrolling tla
    tlorect1 = tlorect1.move(speedtlo)
    tlorect2 = tlorect2.move(speedtlo)

    if tlorect2.left==-3000:
       tlorect2 = tlorect2.move([6000,0])
    if tlorect1.left==-3000:
       tlorect1 = tlorect1.move([6000,0])

    #### osadzanie obiektow na ekranie
    screen.blit(tlo1, tlorect1)
    screen.blit(tlo2, tlorect2)
    pygame.display.flip()
    

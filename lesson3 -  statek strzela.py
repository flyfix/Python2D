import sys, pygame, random, thread
pygame.init()

def graj(x):
   if not pygame.mixer.music.get_busy(): 
      pygame.mixer.music.load(x)
      pygame.mixer.music.play() 






size = width, height = 800, 600

speedtlo = [-5, 0]
speedstrz = [4, 0]
speed = [0,0]
strzalist=[]

screen = pygame.display.set_mode(size)
 
tlo1 = pygame.image.load("files/tlo.bmp")
tlorect1 = tlo1.get_rect()
tlo2 = pygame.image.load("files/tlo.bmp")
tlorect2 = tlo2.get_rect()
tlorect2 = tlorect2.move([3000,0])
statek = pygame.image.load("files/statek.gif")
statekrect = statek.get_rect()
statekrect = statekrect.move([200,200])

strzal = pygame.image.load("files/strzal.gif")
strzalrect = strzal.get_rect()


pygame.mouse.set_pos([1,400])
pygame.mouse.set_visible(0)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #### ruch klawiszy

        if event.type == pygame.KEYUP and event.key==pygame.K_SPACE:
             if len(strzalist) < 10:
                graj(r"sound/strzal.wav")
                pom = strzal
                pom1= strzalrect
                pom1=pom1.move([statekrect.right,statekrect.bottom-30])
                strzalist.insert(-1,(pom,pom1))
             else:
                graj(r"sound/pusty.wav")

    #### scrolling tla
    tlorect1 = tlorect1.move(speedtlo)
    tlorect2 = tlorect2.move(speedtlo)
    statekrect = statekrect.move(speed)
    if tlorect2.left==-3000:
       tlorect2 = tlorect2.move([6000,0])
    if tlorect1.left==-3000:
       tlorect1 = tlorect1.move([6000,0])
     
    ### ruch pociskow
    pomlista=[]
    for i in strzalist:
      pom=i[0]
      pom1=i[1].move(speedstrz)
      pomlista.insert(-1,(pom,pom1))
    strzalist=pomlista
    

    ### sprawdzanie pociskow za ekranem
    ii=0
    for i in strzalist:
      pom=i[0]
      pom1=i[1]
      if pom1.left>width:
        strzalist.pop(ii)
      ii=ii+1

    #### osadzanie obiektow na ekranie
    screen.blit(tlo1, tlorect1)
    screen.blit(tlo2, tlorect2)
    screen.blit(statek, statekrect)

    for i in strzalist:
       screen.blit(i[0],i[1])

    pygame.display.flip()
    

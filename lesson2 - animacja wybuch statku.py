import sys, pygame, random, thread
pygame.init()

def graj(x):
   if not pygame.mixer.music.get_busy(): 
      pygame.mixer.music.load(x)
      pygame.mixer.music.play() 



size = width, height = 800, 600

speedtlo = [-5, 0]

speed = [0,0]

kolizja=0
wybuchlista=[]
wybuchpomlista=[]





screen = pygame.display.set_mode(size)
 
tlo1 = pygame.image.load("files/tlo.bmp")
tlorect1 = tlo1.get_rect()
tlo2 = pygame.image.load("files/tlo.bmp")
tlorect2 = tlo2.get_rect()
tlorect2 = tlorect2.move([3000,0])
###################################################################
#### Wczytenie staku

statek = pygame.image.load("files/statek.gif")
statekrect = statek.get_rect()
statekrect = statekrect.move([200,200])
###################################################################

#### wczytanie animacji wybuchu
for i in range(9,42):
   pomnazwa="wybuch\wyb"+str(i)+".gif"
   pom = pygame.image.load(pomnazwa)
   pom=pom.convert()
   pom1= pom.get_rect()
   wybuchlista.insert(-1,(pom,pom1))  #### wlasciwie pom1 niepotrzebne
###################################################################

koniec = pygame.image.load("files/koniec.gif")
koniecrect = koniec.get_rect()
koniecrect = koniecrect.move([40,200])   

pygame.mouse.set_pos([1,400])
pygame.mouse.set_visible(0)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        ########### wymuszenie kolizji gdy naciskamu ESC
        if event.type == pygame.KEYUP and event.key==pygame.K_ESCAPE:
            kolizja = 1
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
    ########## osadzaj na ekranie statek lub animacje wybuchu

    if kolizja==0:
      screen.blit(statek, statekrect)
    else:
      if wybuchlista<>[]:
         pom=wybuchlista.pop(0)
         screen.blit(pom[0], statekrect)
         graj("sound/wybuch.wav")
      else:
         screen.blit(koniec, koniecrect)
    pygame.display.flip()
    

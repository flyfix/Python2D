import sys, pygame, random, thread
pygame.init()

def aaplayer():
    import pymedia.audio.acodec as acodec
    import pymedia.muxer as muxer
    f= open( sName, 'rb' ) 
    s= f.read( 200000 )
    frames= dm.parse( s )
    frame= frames[ 0 ]
    dec= acodec.Decoder( dm.streams[ 0 ] )

    r= dec.decode( s )
    import pymedia.audio.sound as sound
    snd= sound.Output( r.sample_rate, r.channels, sound.AFMT_S16_LE )
    while len(s)>0:
        if r:
            snd.play( r.data )
            s= f.read( 512 )
            r= dec.decode( s )
    import time
    while snd.isPlaying():
        time.sleep( .05 )


def graj(x):
   if not pygame.mixer.music.get_busy(): 
      pygame.mixer.music.load(x)
      pygame.mixer.music.play() 

thread.start_new_thread(aaplayer,())

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 22,"true")
myfontWin = pygame.font.SysFont("monospace", 45,"true")

size = width, height = 1366, 768
speedtlo = [-10, 0]
speedstrz = [4, 0]
speed = [0,0]
#l_kamien=10

l_kaczynski= 3;
l_tusk = 3;

#speedkam=[-4,0]
speed_tusk = [-10,0]
speed_kaczynski = [-10,0]

#lista=[]
lista=[]
koniec=0

pomlista=[]
strzalist=[]
kolizja=0
wybuchlista=[]
wybuchpomlista=[]
ilosc_zyc = 2
screen = pygame.display.set_mode(size)
czy_zliczac_kolizcje = 1
liczbaPunktow=0

tlo1 = pygame.image.load("files/tlo.bmp")
tlorect1 = tlo1.get_rect()
tlo2 = pygame.image.load("files/tlo.bmp")
tlorect2 = tlo2.get_rect()
tlorect2 = tlorect2.move([3000,0])
statek = pygame.image.load("files/statek.gif")
statekrect = statek.get_rect()
statekrect = statekrect.move([200,200])
koniec = pygame.image.load("files/koniec.png")
koniecrect = koniec.get_rect()
koniecrect = koniecrect.move([40,200])

strzal = pygame.image.load("files/strzal.png")
strzalrect = strzal.get_rect()

def inicjalizuj_przeciwnikow(pomlista):
    lista_tusk=[]
    lista_kaczynski=[]
    ##Lista Tuskow
    for i in range(1,l_tusk+2):
            tusk_gif = pygame.image.load("files/tusk.png")
            tusk_rect = tusk_gif.get_rect()
            tusk_pos = (random.randint(850,1500),random.randint(51,550))
            lista_tusk.insert(-1,(tusk_gif,tusk_rect,tusk_pos))

    #Lista Kaczynskich
    for i in range(1,l_kaczynski+2):
            kaczynski_gif = pygame.image.load("files/kaczynski.png")
            kaczynski_rect = kaczynski_gif.get_rect()
            kaczynski_pos = (random.randint(850,1500),random.randint(100,1300))
            #kaczynski_pos =(300,300)
            lista_kaczynski.insert(-1,(kaczynski_gif,kaczynski_rect,kaczynski_pos))

    for i in lista_kaczynski:
        pom=i[0]
        pom2=i[2]
        x1=pom2[0]
        y1=pom2[1]
        pom1=i[1].move(x1,y1)
        pomlista.insert(-1,(pom,pom1,pom2))
    lista_kaczynski=pomlista
    pomlista=[]
    
    for i in lista_tusk:
        pom=i[0]
        pom2=i[2]
        x1=pom2[0]
        y1=pom2[1]
        pom1=i[1].move(x1,y1)
        pomlista.insert(-1,(pom,pom1,pom2))
    lista_tusk=pomlista
    pomlista=[]
    lista = lista_tusk + lista_kaczynski  
    return lista


############# wczytujemy wybuch 
    for i in range(9,42):
       pomnazwa="wybuch\wyb"+str(i)+".gif"
       pom = pygame.image.load(pomnazwa)
       pom1= pom.get_rect()
       ###pom2=(300,300)
       wybuchlista.insert(-1,(pom,pom1,pom2))


    pygame.mouse.set_pos([1,400])
    pygame.mouse.set_visible(0)
lista = inicjalizuj_przeciwnikow(pomlista)

while ilosc_zyc > 0:
    if liczbaPunktow < 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            #### ruch klawiszy
            if event.type == pygame.KEYDOWN and event.key==pygame.K_LEFT:
                 speed[0] = -2
            if event.type == pygame.KEYDOWN and event.key==pygame.K_RIGHT:
                 speed[0] = 2             
            if event.type == pygame.KEYDOWN and event.key==pygame.K_UP:
                 speed[1] = -2
            if event.type == pygame.KEYDOWN and event.key==pygame.K_DOWN:
                 speed[1] = 2 
            if event.type == pygame.KEYUP and event.key==pygame.K_LEFT:
                 speed[0] = 0
            if event.type == pygame.KEYUP and event.key==pygame.K_RIGHT:
                 speed[0] = 0             
            if event.type == pygame.KEYUP and event.key==pygame.K_UP:
                 speed[1] = 0
            if event.type == pygame.KEYUP and event.key==pygame.K_DOWN:
                 speed[1] = 0 
            if event.type == pygame.KEYUP and event.key==pygame.K_ESCAPE and kolizja==1:
                 czy_zliczac_kolizcje = 1
                 graj(r"sound/powrot.wav")
                 kolizja=0 
                 for i in range(9,42):
                     pomnazwa="wybuch\wyb"+str(i)+".gif"
                     pom = pygame.image.load(pomnazwa)
                     pom1= pom.get_rect()
                     wybuchlista.insert(-1,(pom,pom1,pom2))
            if event.type == pygame.KEYUP and event.key==pygame.K_SPACE and czy_zliczac_kolizcje == 1:
                 if len(strzalist) < 10:
                    graj(r"sound/strzal.wav")
                    pom = strzal
                    pom1= strzalrect
                    pom1=pom1.move([statekrect.right,statekrect.bottom-30])
                    strzalist.insert(-1,(pom,pom1,pom2))
                 else:
                    graj(r"sound/pusty.wav")

        ########### kolizja statku z kamieniami
        for i in lista:
          if statekrect.collidelistall([i[1]]) and czy_zliczac_kolizcje == 1:
            czy_zliczac_kolizcje = 0
            kolizja=1
            ilosc_zyc-=1
            lista = inicjalizuj_przeciwnikow(pomlista)
            graj("sound/wybuch.wav")
            sys.stdout.write("Kolizja\n")
            sys.stdout.flush()


        ### kolizja strzalow z kamieniami
        ii=0
        for i in lista:
           jj=0
           for j in strzalist:
             if j[1].collidelistall([i[1]]):
                liczbaPunktow +=1
                strzalist.pop(jj)
                lista.pop(ii)
             jj+=1   
           ii+=1
           
        ### sprawdz czy statek nie wyszedl za ekran
        if statekrect.left < 0:
            speed[0] = 1
        if statekrect.right > width:
            speed[0] = -1
        if statekrect.top < 0: 
            speed[1] = 1
        if statekrect.bottom > height: 
            speed[1] = -1


        #### scrolling tla
        tlorect1 = tlorect1.move(speedtlo)
        tlorect2 = tlorect2.move(speedtlo)
        statekrect = statekrect.move(speed)
        if tlorect2.left==-3000:
           tlorect2 = tlorect2.move([6000,0])
        if tlorect1.left==-3000:
           tlorect1 = tlorect1.move([6000,0])

        #### ruch kamieni
        for i in lista:
          pom=i[0]
          pom1=i[1].move(-5,0)
          pom2=i[2]
          pomlista.insert(-1,(pom,pom1,pom2))
        lista=pomlista
        pomlista=[]

        ### ruch pociskow
        for i in strzalist:
          pom=i[0]
          pom1=i[1].move(speedstrz)
          pom2=i[2]
          pomlista.insert(-1,(pom,pom1,pom2))
        strzalist=pomlista
        pomlista=[]    

        ### sprawdzanie pociskow za ekranem
        ii=0
        for i in strzalist:
          pom=i[0]
          pom1=i[1]
          pom2=i[2]
          if pom1.left>width:
            strzalist.pop(ii)
          ii+=1

        ### sprawdzenie czy kamienie za ekranem
        for i in lista:
          pom=i[0]
          if i[1].left < -30:
            pom1=i[1].move(0,-i[1].bottom)
            pom1=pom1.move(random.randint(850,1500),random.randint(1,600))
            
          else:
            pom1=i[1]
          pom2=i[2]
          pomlista.insert(-1,(pom,pom1,pom2))
        lista=pomlista
        pomlista=[]


        #### osadzanie obiektow na ekranie
            #### osadzanie obiektow na ekranie
        screen.blit(tlo1, tlorect1)
        screen.blit(tlo2, tlorect2)
        if kolizja==0:
          screen.blit(statek, statekrect)
        else:
          sys.stdout.write("ilosc_zyc:" + str(ilosc_zyc) + "\n")
          if wybuchlista<>[]:
             pom=wybuchlista.pop(0)
             screen.blit(pom[0], statekrect)
          if ilosc_zyc<=0:
             sys.stdout.write("ilosc_zyc==0")
             sys.stdout.flush()
             screen.blit(koniec, koniecrect)
        for i in lista:
           screen.blit(i[0],i[1])
        for i in strzalist:
           screen.blit(i[0],i[1])
           
        label = myfont.render("Zycia:" + str(ilosc_zyc), 1, (255,0,0))
        scoreLabel = myfont.render("Punkty:" + str(liczbaPunktow), 1, (255,0,0))
        screen.blit(label, (10, 10))
        screen.blit(scoreLabel, (10, 30))
    else:

         label2 = myfontWin.render("Wygrales !!!", 1, (255,0,0))
         screen.blit(label2, (500, 300))
        

    pygame.display.flip()
    

import pygame
pygame.init()

win = pygame.display.set_mode((1000,800))
walkRight = [pygame.image.load('hr1.png'),pygame.image.load('hr2.png'),pygame.image.load('hr3.png'),pygame.image.load('hr4.png'),pygame.image.load('hr5.png'),pygame.image.load('hr6.png'),pygame.image.load('hr7.png'),pygame.image.load('hr8.png'),pygame.image.load('hr9.png')]
walkLeft = [pygame.image.load('hl1.png'),pygame.image.load('hl2.png'),pygame.image.load('hl3.png'),pygame.image.load('hl4.png'),pygame.image.load('hl5.png'),pygame.image.load('hl6.png'),pygame.image.load('hl7.png'),pygame.image.load('hl8.png'),pygame.image.load('hl9.png')]
walkUp = [pygame.image.load('hu1.png'),pygame.image.load('hu2.png'),pygame.image.load('hu3.png'),pygame.image.load('hu4.png'),pygame.image.load('hu5.png'),pygame.image.load('hu6.png'),pygame.image.load('hu7.png'),pygame.image.load('hu8.png'),pygame.image.load('hu9.png')]
walkDown = [pygame.image.load('hd1.png'),pygame.image.load('hd2.png'),pygame.image.load('hd3.png'),pygame.image.load('hd4.png'),pygame.image.load('hd5.png'),pygame.image.load('hd6.png'),pygame.image.load('hd7.png'),pygame.image.load('hd8.png'),pygame.image.load('hd9.png')]
shootup = pygame.image.load('hsu1.png')
shootdown = pygame.image.load('hsd1.png')

shootleft = pygame.image.load('hsl1.png')
shootright = pygame.image.load('hsr1.png')
pygame.display.set_caption("Shooting")
bg = pygame.image.load('bg.png')
    #reloadsound = pygame.mixer.Sound('reload.wav')
clock = pygame.time.Clock()
global score
score = 0
mag = 10
def dead():
    font =pygame.font.SysFont ('comicsans', 50,True)
    w = pygame.display.set_mode((1000,800))
    scoree = score
    game = font.render("Score : "+str(scoree),1,(0,0,220))
    win.blit(game,(300,400))
    pygame.display.set_caption("Last room")
    bg3 = pygame.image.load('Over.png')
    bt001=pygame.image.load('menu4.png')
    bt0011=pygame.image.load('menu42.png')
    bt002=pygame.image.load('menu34.png')
    bt0022=pygame.image.load('menu32.png')
    
    run = True
    def over():
        w.blit(bg3, (0,0))
        pygame.display.update()
    def btt():
            mouse=pygame.mouse.get_pos()
            if 200<mouse[0]<405 and 620<mouse[1]<725:
                w.blit(bt0011,(200,650,600,400))
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running()
                
            else:
                w.blit(bt001,(200,650,600,400))
                pygame.display.update()
    def bttq():
        mouse=pygame.mouse.get_pos()
        if 625<mouse[0]<735 and 620<mouse[1]<725:
            w.blit(bt0022,(600,650,500,400))
            pygame.display.update()
        else:
            w.blit(bt002,(600,650,500,400))
            pygame.display.update()
    while run:
        
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
            if pygame.event == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if 625<mx<735 and 620<my<725:
                    pygame.quit()
        over()
        btt()
        bttq()

def running():
    
    win = pygame.display.set_mode((1000,800))
    walkRight = [pygame.image.load('hr1.png'),pygame.image.load('hr2.png'),pygame.image.load('hr3.png'),pygame.image.load('hr4.png'),pygame.image.load('hr5.png'),pygame.image.load('hr6.png'),pygame.image.load('hr7.png'),pygame.image.load('hr8.png'),pygame.image.load('hr9.png')]
    walkLeft = [pygame.image.load('hl1.png'),pygame.image.load('hl2.png'),pygame.image.load('hl3.png'),pygame.image.load('hl4.png'),pygame.image.load('hl5.png'),pygame.image.load('hl6.png'),pygame.image.load('hl7.png'),pygame.image.load('hl8.png'),pygame.image.load('hl9.png')]
    walkUp = [pygame.image.load('hu1.png'),pygame.image.load('hu2.png'),pygame.image.load('hu3.png'),pygame.image.load('hu4.png'),pygame.image.load('hu5.png'),pygame.image.load('hu6.png'),pygame.image.load('hu7.png'),pygame.image.load('hu8.png'),pygame.image.load('hu9.png')]
    walkDown = [pygame.image.load('hd1.png'),pygame.image.load('hd2.png'),pygame.image.load('hd3.png'),pygame.image.load('hd4.png'),pygame.image.load('hd5.png'),pygame.image.load('hd6.png'),pygame.image.load('hd7.png'),pygame.image.load('hd8.png'),pygame.image.load('hd9.png')]
    shootup = pygame.image.load('hsu1.png')
    shootdown = pygame.image.load('hsd1.png')

    shootleft = pygame.image.load('hsl1.png')
    shootright = pygame.image.load('hsr1.png')
    pygame.display.set_caption("Shooting")
    bg = pygame.image.load('bg.png')
        #reloadsound = pygame.mixer.Sound('reload.wav')
    clock = pygame.time.Clock()
    global score
    score = 0
    mag = 10
    class player(object):
        
        
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 14
            self.isJump = False
            self.left = False
            self.right = True
            self.up = False
            self.down = False
            self.walkCount = 9
            self.standing = True
            self.shooting = False
            self.hitbox = (self.x,self.y,64,64)
            self.hp = 1000

        def draw(self, win):
            #print("self.walkCount ==== :",self.walkCount)
            #print(self.walkCount//9)
            if self.walkCount + 1 >=10:
                self.walkCount = 0
            #print("standing ===== ",self.standing)
            #print("walkup ==== ",self.up)
            #print("walkdown === ",self.down)
            #print("walkleft == ",self.left)
            #print("walkright = ",self.right)
            #print("shooting =================",self.shooting)
                  
            if self.shooting:
                if self.up:
                    win.blit(shootup,(self.x,self.y))
                if self.down:
                    win.blit(shootdown,(self.x,self.y))
                if self.left:
                    win.blit(shootleft,(self.x,self.y))
                if self.right:
                    win.blit(shootright,(self.x,self.y))
            elif not(self.standing):
                if self.left:
                    win.blit(walkLeft[self.walkCount], (self.x,self.y))
                    self.walkCount+=1
                elif self.right:
                    win.blit(walkRight[self.walkCount], (self.x,self.y))
                    self.walkCount+=1
                elif self.up:
                    win.blit(walkUp[self.walkCount],(self.x,self.y))
                    self.walkCount+=1
                elif self.down:
                    win.blit(walkDown[self.walkCount],(self.x,self.y))
                    self.walkCount+=1
            elif self.standing:
                if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
                elif self.left:
                    win.blit(walkLeft[0], (self.x, self.y))
                elif self.up:
                    win.blit(walkUp[0],(self.x,self.y))
                elif self.down:
                    win.blit(walkDown[0],(self.x,self.y))
            
                
            
            self.hitbox = (self.x +17,self.y+11,29,52)
        def hit1(self):
            if self.hp >0:
                self.hp-=6
                #print("hit1")
            else :
                print ("die")
                self.hp = 1000
                dead()
        def hit2(self):
            if self.hp >0:
                self.hp-=3
                #print("hit2")
            else :
                print ("die")
                self.hp = 1000
                dead()
        def hit3(self):
            if self.hp>0:
                self.hp-=25
                #print("hit3")
            else:
                print("die")
                self.hp = 1000
                dead()
        def hit4(self):
            if self.hp>0:
                self.hp-=40
                #print("hit4")
            else:
                print("die")
                self.hp = 1000
                dead()
        def getmz(self):
            print("Get")
        def getmd(self):
            print("Getttttttttmd")
            self.hp = 1000
        


    class projectile(object):
        def __init__(self,x,y,radius,color,facing):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing
            self.vel =  80* facing

        def draw(self,win):
            pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
    class magazine(object):
        magaZine = pygame.image.load("m1.png")
        def __init__(self,x,y):
            self.x = x
            self.y = y
        def draw(self,win):
            win.blit(self.magaZine,(self.x,self.y))
    class medic(object):
        meDic = pygame.image.load("md1.png")
        
        def __init__(self,x,y):
            self.x = x
            self.y = y
            self.hitbox = (self.x,self.y,20,20)
            self.visible = True
            
        def draw(self,win):
            if self.visible:
                win.blit(self.meDic,(self.x,self.y))
                self.hitbox = (self.x,self.y,20,20)

    class enemy(object):
        walkRight = [pygame.image.load('z1r1.png'),pygame.image.load('z1r2.png'),pygame.image.load('z1r3.png'),pygame.image.load('z1r4.png'),pygame.image.load('z1r5.png'),pygame.image.load('z1r6.png'),pygame.image.load('z1r7.png'),pygame.image.load('z1r8.png'),pygame.image.load('z1r9.png')]
        walkLeft = [pygame.image.load('z1l1.png'),pygame.image.load('z1l2.png'),pygame.image.load('z1l3.png'),pygame.image.load('z1l4.png'),pygame.image.load('z1l5.png'),pygame.image.load('z1l6.png'),pygame.image.load('z1l7.png'),pygame.image.load('z1l8.png'),pygame.image.load('z1l9.png')]
        
        def __init__(self, x, y, width, height,vel):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.walkCount = 0
            self.vel = vel
            self.hitbox = (self.x ,self.y,64,64)
            self.health = 40
            self.visible = True
            

        def draw(self, win):
            self.move()
            if self.visible:
                if self.walkCount + 1 >= 33:
                    self.walkCount = 0
            
                #อย่าลืมทำหน้าzombie ขึ้นลงซ้ายขวา
                if self.x <= man.x: 
                    win.blit(self.walkRight[self.walkCount//9], (self.x,self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.walkLeft[self.walkCount//9], (self.x,self.y))
                    self.walkCount += 1
                pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,self.hitbox[2],10))
                pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,self.hitbox[3] - (40-self.health)*1.5,10))
                self.hitbox = (self.x ,self.y,64,64)
                #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
                
        def move(self):
                if self.x < man.x:
                    self.x += self.vel
                else :
                    self.x -= self.vel
                if self.y < man.y:
                    self.y += self.vel
                else:
                    self.y -= self.vel
        def hit(self):
            if self.health>0:
                self.health -=10
            else:
                self.visible = False
                global score
                score+=2
                
            


    class enemy2(object):
        walkRight = [pygame.image.load('z2r1.png'),pygame.image.load('z2r2.png'),pygame.image.load('z2r3.png')]
        walkLeft = [pygame.image.load('z2l1.png'),pygame.image.load('z2l2.png'),pygame.image.load('z2l3.png')]
        
        #walkUP
        #walkDown
        
        def __init__(self, x, y, width, height,vel):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.walkCount = 0
            self.vel = vel
            self.hitbox = (self.x ,self.y,50,50)
            self.health = 15
            self.visible = True

        def draw(self, win):
            self.move()
            if self.visible:
                if self.walkCount + 1 >= 9:
                    self.walkCount = 0
            
                
                if self.x <= man.x: 
                    win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,self.hitbox[3],10))
                pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,self.hitbox[3] - ((self.hitbox[3]/20)*(15-self.health)),10))
                self.hitbox = (self.x ,self.y,50,50)
                #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
                
        def move(self):
                if self.x < man.x:
                    self.x += self.vel
                else :
                    self.x -= self.vel
                if self.y < man.y:
                    self.y += self.vel
                else:
                    self.y -= self.vel
        def hit(self):
            if self.health>0:
                self.health -=5
            else:
                self.visible = False
                global score
                score = score+1
                
            
    class enemy3(object):
        walkRight = [pygame.image.load('z3r1.png'),pygame.image.load('z3r2.png'),pygame.image.load('z3r3.png')]
        walkLeft = [pygame.image.load('z3l1.png'),pygame.image.load('z3l2.png'),pygame.image.load('z3l3.png')]
        
        #walkUP
        #walkDown
        
        def __init__(self, x, y, width, height,vel):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.walkCount = 0
            self.vel = vel
            self.hitbox = (self.x ,self.y,100,100)
            self.health = 120
            self.visible = True

        def draw(self, win):
            self.move()
            
            if self.visible:
                if self.walkCount + 1 >= 19:
                    self.walkCount = 0
            
                
                if self.x <= man.x: 
                    win.blit(self.walkRight[self.walkCount//6], (self.x,self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.walkLeft[self.walkCount//6], (self.x,self.y))
                    self.walkCount += 1
                pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,self.hitbox[3],10))
                pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,self.hitbox[3] - ((self.hitbox[3]/119)*(120-self.health)),10))
                self.hitbox = (self.x ,self.y,100,100)
                #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
                
        def move(self):
                if self.x < man.x:
                    self.x += self.vel
                else :
                    self.x -= self.vel
                if self.y < man.y:
                    self.y += self.vel
                else:
                    self.y -= self.vel
        def hit(self):
            if self.health>0:
                self.health -=5
            else:
                self.visible = False
                global score
                score = score+5
                
            


    class enemy4(object):
        walkRight = [pygame.image.load('z4r1.png'),pygame.image.load('z4r2.png'),pygame.image.load('z4r3.png'),pygame.image.load('z4r4.png'),pygame.image.load('z4r5.png'),pygame.image.load('z4r6.png'),pygame.image.load('z4r7.png')]
        walkLeft = [pygame.image.load('z4l1.png'),pygame.image.load('z4l2.png'),pygame.image.load('z4l3.png'),pygame.image.load('z4l4.png'),pygame.image.load('z4l5.png'),pygame.image.load('z4l6.png'),pygame.image.load('z4l7.png')]
        
        #walkUP
        #walkDown
        
        def __init__(self, x, y, width, height,vel):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.walkCount = 0
            self.vel = vel
            self.hitbox = (self.x ,self.y,128,128)
            self.health = 200
            self.visible = True

        def draw(self, win):
            self.move()
            if self.visible:
                if self.walkCount + 1 >= 35:
                    self.walkCount = 0
            
                
                if self.x <= man.x: 
                    win.blit(self.walkRight[self.walkCount//7], (self.x,self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.walkLeft[self.walkCount//7], (self.x,self.y))
                    self.walkCount += 1
                pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,self.hitbox[3],10))
                pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,self.hitbox[3] - ((self.hitbox[3]/200)*(200-self.health)),10))
                self.hitbox = (self.x ,self.y,128,128)
                #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
                
        def move(self):
                if self.x < man.x:
                    self.x += self.vel
                else :
                    self.x -= self.vel
                if self.y < man.y:
                    self.y += self.vel
                else:
                    self.y -= self.vel
        def hit(self):
            if self.health>0:
                self.health -=5
            else:
                self.visible = False
                global score
                score = score+20
                
            


                
        



        


    def redrawGameWindow():
        win.blit(bg, (0,0))
        text = font.render('Score: '+str(score),1,(200,0,0))
        text2 = font.render('Health: '+str(man.hp),1,(0,200,0))
        text3 = font.render("Mag : "+str(r),1,(0,0,200))
        win.blit(text,(850,10))
        win.blit(text2,(10,10))
        win.blit(text3,(400,10))
        man.draw(win)
        for bullet in bullets:
            bullet.draw(win)
        #mz1.draw(win)
        #md1.draw(win)
        #z11.draw(win)
        #z21.draw(win)
        #z31.draw(win)
        #z41.draw(win)
        for z in round1:
           z.draw(win)
        if j >=300:
            for z in round2:
                z.draw(win)
        if j>= 700:
            for z in round3:
                z.draw(win)
        if j>= 1200:
           for z in round4:
               z.draw(win)
        if j>= 1700:
            for z in round5:
                z.draw(win)
        
        pygame.display.update()

    #30 = size
    #mainloop
    font =pygame.font.SysFont ('comicsans', 30,True)
    man = player(200, 410, 64,64)
    z11 =enemy(1000,0,64,64,3)
    z12 = enemy(3000,0,64,64,3.25)
    z13 = enemy(5000,0,64,64,3.5)
    z14 = enemy(7000,0,64,64,3.75)
    z15 = enemy(0,1000,64,64,4)
    z16 = enemy(0,3000,64,64,4.25)
    z17 = enemy(0,5000,64,64,4.5)
    z18 = enemy(0,7000,64,64,4.75)
    z19 = enemy(8000,0,64,64,5)
    z110 = enemy(800,3000,64,64,5.25)

    z111 =enemy(1000,0,64,64,3)
    z112 = enemy(3000,0,64,64,3.25)
    z113 = enemy(5000,0,64,64,3.5)
    z114 = enemy(7000,0,64,64,3.75)
    z115 = enemy(0,1000,64,64,4)
    z116 = enemy(0,3000,64,64,4.25)
    z117 = enemy(0,5000,64,64,4.5)
    z118 = enemy(0,7000,64,64,4.75)
    z119 = enemy(1000,0,64,64,5)
    z120 = enemy(1200,300,64,64,5.25)

    z121 =enemy(1000,0,64,64,3)
    z122 = enemy(0,1500,64,64,3.25)
    z123 = enemy(1200,0,64,64,3.5)
    z124 = enemy(1300,0,64,64,3.75)
    z125 = enemy(0,13000,64,64,4)
    z126 = enemy(0,3000,64,64,4.25)
    z127 = enemy(0,1400,64,64,4.5)
    z128 = enemy(0,1500,64,64,4.75)
    z129 = enemy(1800,0,64,64,5)
    z130 = enemy(1900,400,64,64,5.25)

    z131 =enemy(1000,0,64,64,3)
    z132 = enemy(1400,0,64,64,3.25)
    z133 = enemy(1500,0,64,64,3.5)
    z134 = enemy(1300,0,64,64,3.75)
    z135 = enemy(0,1000,64,64,4)
    z136 = enemy(0,2000,64,64,4.25)
    z137 = enemy(0,1500,64,64,4.5)
    z138 = enemy(0,1700,64,64,4.75)
    z139 = enemy(1800,0,64,64,5)
    z140 = enemy(1800,300,64,64,5.25)

    z141 = enemy(1000,0,64,64,3)
    z142 = enemy(1300,100,64,64,3.25)
    z143 = enemy(1500,0,64,64,3.5)
    z144 = enemy(1700,0,64,64,3.75)
    z145 = enemy(0,1600,64,64,4)
    z146 = enemy(0,1300,64,64,4.25)
    z147 = enemy(0,1500,64,64,4.5)
    z148 = enemy(0,1700,64,64,4.75)
    z149 = enemy(1800,0,64,64,5)
    z150 = enemy(1800,300,64,64,5.25)



    z21 = enemy2(1000,100,50,50,6)
    z22 = enemy2(1000,200,50,50,6.25)
    z23 = enemy2(1200,300,50,50,6.5)
    z24 = enemy2(1400,400,50,50,6.75)
    z25 = enemy2(1500,0,50,50,7)
    z26 = enemy2(1500,0,50,50,7.25)
    z27 = enemy2(1700,0,50,50,7.5)
    z28 = enemy2(1900,0,50,50,7.75)
    z29 = enemy2(1200,600,50,50,8)
    z210 = enemy2(1400,600,50,50,8.25)

    z211 = enemy2(1200,100,50,50,6)
    z212 = enemy2(1300,200,50,50,6.25)
    z213 = enemy2(1400,300,50,50,6.5)
    z214 = enemy2(1600,400,50,50,6.75)
    z215 = enemy2(1700,500,50,50,7)
    z216 = enemy2(1400,600,50,50,7.25)
    z217 = enemy2(1300,600,50,50,7.5)
    z218 = enemy2(1700,600,50,50,7.75)
    z219 = enemy2(1800,600,50,50,8)
    z220 = enemy2(1100,600,50,50,8.25)

    z221 = enemy2(1700,100,50,50,6)
    z222 = enemy2(1800,200,50,50,6.25)
    z223 = enemy2(1400,300,50,50,6.5)
    z224 = enemy2(1600,1400,50,50,6.75)
    z225 = enemy2(1300,1500,50,50,7)
    z226 = enemy2(1500,1600,50,50,7.25)
    z227 = enemy2(1700,600,50,50,7.5)
    z228 = enemy2(1800,600,50,50,7.75)
    z229 = enemy2(1100,600,50,50,8)
    z230 = enemy2(100,1600,50,50,8.25)

    z231 = enemy2(1200,100,50,50,6)
    z232 = enemy2(1300,200,50,50,6.25)
    z233 = enemy2(1600,300,50,50,6.5)
    z234 = enemy2(1700,400,50,50,6.75)
    z235 = enemy2(1600,500,50,50,7)
    z236 = enemy2(1800,600,50,50,7.25)
    z237 = enemy2(1600,600,50,50,7.5)
    z238 = enemy2(1500,600,50,50,7.75)
    z239 = enemy2(100,1600,50,50,8)
    z240 = enemy2(100,1600,50,50,8.25)

    z31 = enemy3(1000,0,100,100,2)
    z32 = enemy3(1400,0,100,100,2.25)
    z33 = enemy3(1700,0,100,100,2.5)
    z34 = enemy3(0,1200,100,100,2.75)
    z35 = enemy3(0,1500,100,100,3)

    z36 = enemy3(0,0,1300,100,2)
    z37 = enemy3(500,12000,100,100,2.25)
    z38 = enemy3(0,1700,100,100,2.5)
    z39 = enemy3(1000,0,100,100,2.75)
    z310 = enemy3(1200,0,100,100,3)

    z311 = enemy3(0,1700,100,100,2)
    z312 = enemy3(1200,0,100,100,2.25)
    z313 = enemy3(0,1600,100,100,2.5)
    z314 = enemy3(1500,600,100,100,2.75)
    z315 = enemy3(1300,700,100,100,3)

    z41 = enemy4(1500,0,100,100,6)





    mz1 = magazine(300,300)
    md1 = medic(400,400)
    md2 = medic(200,600)
    md3 = medic(800,700)
    slow = 0
    round1=[z11,z12,z13,z14,z15,z16,z17,z18,z19,z110,md1]
    round2 =[z111,z112,z113,z114,z115,z116,z117,z118,z119,z120,z21,z22,z23,z24,z25,z26,z27,z28,z29,z210]
    round3 = [z121,z122,z123,z124,z125,z126,z127,z128,z129,z130,z211,z212,z213,z214,z215,z216,z217,z218,z219,z220,z31,z32,z33,z34,z35]
    round4 = [z131,z132,z133,z134,z135,z136,z137,z138,z139,z140,z221,z222,z223,z224,z225,z226,z227,z228,z229,z230,z36,z37,z38,z39,z310,md2]
    round5 = [z141,z142,z143,z144,z145,z146,z147,z148,z149,z150,z231,z232,z233,z234,z235,z236,z237,z238,z239,z240,z311,z312,z313,z314,z315,z41,md3]
    bullets = []
    r=100
    reload = False
    run = True
    j=0
    #z1 = 50
    #z2 = 40
    #z3 = 15
    #z4 = 1
    while run:
        clock.tick(27)
        if z11.visible == True:
            if man.hitbox[1]  < z11.hitbox[1]+z11.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z11.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z11.hitbox[0] and man.hitbox[0] < z11.hitbox[0] + z11.hitbox[2]:
                    man.hit1()
        if z12.visible == True:
            if man.hitbox[1]  < z12.hitbox[1]+z12.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z12.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z12.hitbox[0] and man.hitbox[0] < z12.hitbox[0] + z12.hitbox[2]:
                    man.hit1()
        if z13.visible == True:
            if man.hitbox[1]  < z13.hitbox[1]+z13.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z13.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z13.hitbox[0] and man.hitbox[0] < z13.hitbox[0] + z13.hitbox[2]:
                    man.hit1()
        if z14.visible == True:
            if man.hitbox[1]  < z14.hitbox[1]+z14.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z14.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z14.hitbox[0] and man.hitbox[0] < z14.hitbox[0] + z14.hitbox[2]:
                    man.hit1()
        if z15.visible == True:
            if man.hitbox[1]  < z15.hitbox[1]+z15.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z15.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z15.hitbox[0] and man.hitbox[0] < z15.hitbox[0] + z15.hitbox[2]:
                    man.hit1()
        if z16.visible == True:
            if man.hitbox[1]  < z16.hitbox[1]+z16.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z16.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z16.hitbox[0] and man.hitbox[0] < z16.hitbox[0] + z16.hitbox[2]:
                    man.hit1()
        if z17.visible == True:
            if man.hitbox[1]  < z17.hitbox[1]+z17.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z17.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z17.hitbox[0] and man.hitbox[0] < z17.hitbox[0] + z17.hitbox[2]:
                    man.hit1()
        if z18.visible == True:
            if man.hitbox[1]  < z18.hitbox[1]+z18.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z18.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z18.hitbox[0] and man.hitbox[0] < z18.hitbox[0] + z18.hitbox[2]:
                    man.hit1()
        if z19.visible == True:
            if man.hitbox[1]  < z19.hitbox[1]+z19.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z19.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z19.hitbox[0] and man.hitbox[0] < z19.hitbox[0] + z19.hitbox[2]:
                    man.hit1()
        if z110.visible == True:
            if man.hitbox[1]  < z110.hitbox[1]+z110.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z110.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z110.hitbox[0] and man.hitbox[0] < z110.hitbox[0] + z110.hitbox[2]:
                    man.hit1()
        if z111.visible == True:
            if man.hitbox[1]  < z111.hitbox[1]+z111.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z111.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z111.hitbox[0] and man.hitbox[0] < z111.hitbox[0] + z111.hitbox[2]:
                    man.hit1()
        if z112.visible == True:
            if man.hitbox[1]  < z112.hitbox[1]+z112.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z112.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z112.hitbox[0] and man.hitbox[0] < z112.hitbox[0] + z112.hitbox[2]:
                    man.hit1()
        if z113.visible == True:
            if man.hitbox[1]  < z113.hitbox[1]+z113.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z113.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z113.hitbox[0] and man.hitbox[0] < z113.hitbox[0] + z113.hitbox[2]:
                    man.hit1()
        if z114.visible == True:
            if man.hitbox[1]  < z114.hitbox[1]+z114.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z114.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z114.hitbox[0] and man.hitbox[0] < z114.hitbox[0] + z114.hitbox[2]:
                    man.hit1()
        if z115.visible == True:
            if man.hitbox[1]  < z115.hitbox[1]+z115.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z115.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z115.hitbox[0] and man.hitbox[0] < z115.hitbox[0] + z115.hitbox[2]:
                    man.hit1()
        if z116.visible == True:
            if man.hitbox[1]  < z116.hitbox[1]+z116.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z116.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z116.hitbox[0] and man.hitbox[0] < z116.hitbox[0] + z116.hitbox[2]:
                    man.hit1()
        if z117.visible == True:
            if man.hitbox[1]  < z117.hitbox[1]+z117.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z117.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z117.hitbox[0] and man.hitbox[0] < z117.hitbox[0] + z117.hitbox[2]:
                    man.hit1()
        if z118.visible == True:
            if man.hitbox[1]  < z118.hitbox[1]+z118.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z118.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z118.hitbox[0] and man.hitbox[0] < z118.hitbox[0] + z118.hitbox[2]:
                    man.hit1()
        if z119.visible == True:
            if man.hitbox[1]  < z119.hitbox[1]+z119.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z119.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z119.hitbox[0] and man.hitbox[0] < z119.hitbox[0] + z119.hitbox[2]:
                    man.hit1()
        if z120.visible == True:
            if man.hitbox[1]  < z120.hitbox[1]+z120.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z120.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z120.hitbox[0] and man.hitbox[0] < z120.hitbox[0] + z120.hitbox[2]:
                    man.hit1()
        if z121.visible == True:
            if man.hitbox[1]  < z121.hitbox[1]+z121.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z121.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z121.hitbox[0] and man.hitbox[0] < z121.hitbox[0] + z121.hitbox[2]:
                    man.hit1()
        if z122.visible == True:
            if man.hitbox[1]  < z122.hitbox[1]+z122.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z122.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z122.hitbox[0] and man.hitbox[0] < z122.hitbox[0] + z122.hitbox[2]:
                    man.hit1()
        if z123.visible == True:
            if man.hitbox[1]  < z123.hitbox[1]+z123.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z123.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z123.hitbox[0] and man.hitbox[0] < z123.hitbox[0] + z123.hitbox[2]:
                    man.hit1()
        if z124.visible == True:
            if man.hitbox[1]  < z124.hitbox[1]+z124.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z124.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z124.hitbox[0] and man.hitbox[0] < z124.hitbox[0] + z124.hitbox[2]:
                    man.hit1()
        if z125.visible == True:
            if man.hitbox[1]  < z125.hitbox[1]+z125.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z125.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z125.hitbox[0] and man.hitbox[0] < z125.hitbox[0] + z125.hitbox[2]:
                    man.hit1()
        if z126.visible == True:
            if man.hitbox[1]  < z126.hitbox[1]+z126.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z126.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z126.hitbox[0] and man.hitbox[0] < z126.hitbox[0] + z126.hitbox[2]:
                    man.hit1()
        if z127.visible == True:
            if man.hitbox[1]  < z127.hitbox[1]+z127.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z127.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z127.hitbox[0] and man.hitbox[0] < z127.hitbox[0] + z127.hitbox[2]:
                    man.hit1()
        if z128.visible == True:
            if man.hitbox[1]  < z128.hitbox[1]+z128.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z128.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z128.hitbox[0] and man.hitbox[0] < z128.hitbox[0] + z128.hitbox[2]:
                    man.hit1()
        if z129.visible == True:
            if man.hitbox[1]  < z129.hitbox[1]+z129.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z129.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z129.hitbox[0] and man.hitbox[0] < z129.hitbox[0] + z129.hitbox[2]:
                    man.hit1()
        if z130.visible == True:
            if man.hitbox[1]  < z130.hitbox[1]+z130.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z130.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z130.hitbox[0] and man.hitbox[0] < z130.hitbox[0] + z130.hitbox[2]:
                    man.hit1()
        if z131.visible == True:
            if man.hitbox[1]  < z131.hitbox[1]+z131.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z131.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z131.hitbox[0] and man.hitbox[0] < z131.hitbox[0] + z131.hitbox[2]:
                    man.hit1()
        if z132.visible == True:
            if man.hitbox[1]  < z132.hitbox[1]+z132.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z132.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z132.hitbox[0] and man.hitbox[0] < z132.hitbox[0] + z132.hitbox[2]:
                    man.hit1()
        if z133.visible == True:
            if man.hitbox[1]  < z133.hitbox[1]+z133.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z133.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z133.hitbox[0] and man.hitbox[0] < z133.hitbox[0] + z133.hitbox[2]:
                    man.hit1()
        if z134.visible == True:
            if man.hitbox[1]  < z134.hitbox[1]+z134.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z134.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z134.hitbox[0] and man.hitbox[0] < z134.hitbox[0] + z134.hitbox[2]:
                    man.hit1()
        if z135.visible == True:
            if man.hitbox[1]  < z135.hitbox[1]+z135.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z135.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z135.hitbox[0] and man.hitbox[0] < z135.hitbox[0] + z135.hitbox[2]:
                    man.hit1()
        if z136.visible == True:
            if man.hitbox[1]  < z136.hitbox[1]+z136.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z136.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z136.hitbox[0] and man.hitbox[0] < z136.hitbox[0] + z136.hitbox[2]:
                    man.hit1()
        if z137.visible == True:
            if man.hitbox[1]  < z137.hitbox[1]+z137.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z137.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z137.hitbox[0] and man.hitbox[0] < z137.hitbox[0] + z137.hitbox[2]:
                    man.hit1()
        if z138.visible == True:
            if man.hitbox[1]  < z138.hitbox[1]+z138.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z138.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z138.hitbox[0] and man.hitbox[0] < z138.hitbox[0] + z138.hitbox[2]:
                    man.hit1()
        if z139.visible == True:
            if man.hitbox[1]  < z139.hitbox[1]+z139.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z139.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z139.hitbox[0] and man.hitbox[0] < z139.hitbox[0] + z139.hitbox[2]:
                    man.hit1()
        if z140.visible == True:
            if man.hitbox[1]  < z140.hitbox[1]+z140.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z140.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z140.hitbox[0] and man.hitbox[0] < z140.hitbox[0] + z140.hitbox[2]:
                    man.hit1()
        if z141.visible == True:
            if man.hitbox[1]  < z141.hitbox[1]+z141.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z141.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z141.hitbox[0] and man.hitbox[0] < z141.hitbox[0] + z141.hitbox[2]:
                    man.hit1()
        if z142.visible == True:
            if man.hitbox[1]  < z142.hitbox[1]+z142.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z142.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z142.hitbox[0] and man.hitbox[0] < z142.hitbox[0] + z142.hitbox[2]:
                    man.hit1()
        if z143.visible == True:
            if man.hitbox[1]  < z143.hitbox[1]+z143.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z143.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z143.hitbox[0] and man.hitbox[0] < z143.hitbox[0] + z143.hitbox[2]:
                    man.hit1()
        if z144.visible == True:
            if man.hitbox[1]  < z144.hitbox[1]+z144.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z144.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z144.hitbox[0] and man.hitbox[0] < z144.hitbox[0] + z144.hitbox[2]:
                    man.hit1()
        if z145.visible == True:
            if man.hitbox[1]  < z145.hitbox[1]+z145.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z145.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z145.hitbox[0] and man.hitbox[0] < z145.hitbox[0] + z145.hitbox[2]:
                    man.hit1()
        if z146.visible == True:
            if man.hitbox[1]  < z146.hitbox[1]+z146.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z146.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z146.hitbox[0] and man.hitbox[0] < z146.hitbox[0] + z146.hitbox[2]:
                    man.hit1()
        if z147.visible == True:
            if man.hitbox[1]  < z147.hitbox[1]+z147.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z147.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z147.hitbox[0] and man.hitbox[0] < z147.hitbox[0] + z147.hitbox[2]:
                    man.hit1()
        if z148.visible == True:
            if man.hitbox[1]  < z148.hitbox[1]+z148.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z148.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z148.hitbox[0] and man.hitbox[0] < z148.hitbox[0] + z148.hitbox[2]:
                    man.hit1()
        if z149.visible == True:
            if man.hitbox[1]  < z149.hitbox[1]+z149.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z149.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z149.hitbox[0] and man.hitbox[0] < z149.hitbox[0] + z149.hitbox[2]:
                    man.hit1()
        if z150.visible == True:
            if man.hitbox[1]  < z150.hitbox[1]+z150.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z150.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z150.hitbox[0] and man.hitbox[0] < z150.hitbox[0] + z150.hitbox[2]:
                    man.hit1()



                    
        if z21.visible == True:
            if man.hitbox[1]  < z21.hitbox[1]+z21.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z21.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z21.hitbox[0] and man.hitbox[0] < z21.hitbox[0] + z21.hitbox[2]:
                    man.hit2()
        if z22.visible == True:
            if man.hitbox[1]  < z22.hitbox[1]+z22.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z22.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z22.hitbox[0] and man.hitbox[0] < z22.hitbox[0] + z22.hitbox[2]:
                    man.hit2()
        if z23.visible == True:
            if man.hitbox[1]  < z23.hitbox[1]+z23.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z23.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z23.hitbox[0] and man.hitbox[0] < z23.hitbox[0] + z23.hitbox[2]:
                    man.hit2()
        if z24.visible == True:
            if man.hitbox[1]  < z24.hitbox[1]+z24.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z24.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z24.hitbox[0] and man.hitbox[0] < z24.hitbox[0] + z24.hitbox[2]:
                    man.hit2()
        if z25.visible == True:
            if man.hitbox[1]  < z25.hitbox[1]+z25.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z25.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z25.hitbox[0] and man.hitbox[0] < z25.hitbox[0] + z25.hitbox[2]:
                    man.hit2()
        if z26.visible == True:
            if man.hitbox[1]  < z26.hitbox[1]+z26.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z26.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z26.hitbox[0] and man.hitbox[0] < z26.hitbox[0] + z26.hitbox[2]:
                    man.hit2()
        if z27.visible == True:
            if man.hitbox[1]  < z27.hitbox[1]+z27.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z27.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z27.hitbox[0] and man.hitbox[0] < z27.hitbox[0] + z27.hitbox[2]:
                    man.hit2()
        if z28.visible == True:
            if man.hitbox[1]  < z28.hitbox[1]+z28.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z28.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z28.hitbox[0] and man.hitbox[0] < z28.hitbox[0] + z28.hitbox[2]:
                    man.hit2()
        if z29.visible == True:
            if man.hitbox[1]  < z29.hitbox[1]+z29.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z29.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z29.hitbox[0] and man.hitbox[0] < z29.hitbox[0] + z29.hitbox[2]:
                    man.hit2()
        if z210.visible == True:
            if man.hitbox[1]  < z210.hitbox[1]+z210.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z210.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z210.hitbox[0] and man.hitbox[0] < z210.hitbox[0] + z210.hitbox[2]:
                    man.hit2()
        if z211.visible == True:
            if man.hitbox[1]  < z211.hitbox[1]+z211.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z211.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z211.hitbox[0] and man.hitbox[0] < z211.hitbox[0] + z211.hitbox[2]:
                    man.hit2()
        if z212.visible == True:
            if man.hitbox[1]  < z212.hitbox[1]+z212.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z212.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z212.hitbox[0] and man.hitbox[0] < z212.hitbox[0] + z212.hitbox[2]:
                    man.hit2()
        if z213.visible == True:
            if man.hitbox[1]  < z213.hitbox[1]+z213.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z213.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z213.hitbox[0] and man.hitbox[0] < z213.hitbox[0] + z213.hitbox[2]:
                    man.hit2()
        if z214.visible == True:
            if man.hitbox[1]  < z214.hitbox[1]+z214.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z214.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z214.hitbox[0] and man.hitbox[0] < z214.hitbox[0] + z214.hitbox[2]:
                    man.hit2()
        if z215.visible == True:
            if man.hitbox[1]  < z215.hitbox[1]+z215.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z215.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z215.hitbox[0] and man.hitbox[0] < z215.hitbox[0] + z215.hitbox[2]:
                    man.hit2()
        if z216.visible == True:
            if man.hitbox[1]  < z216.hitbox[1]+z216.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z216.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z216.hitbox[0] and man.hitbox[0] < z216.hitbox[0] + z216.hitbox[2]:
                    man.hit2()
        if z217.visible == True:
            if man.hitbox[1]  < z217.hitbox[1]+z217.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z217.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z217.hitbox[0] and man.hitbox[0] < z217.hitbox[0] + z217.hitbox[2]:
                    man.hit2()
        if z218.visible == True:
            if man.hitbox[1]  < z218.hitbox[1]+z218.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z218.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z218.hitbox[0] and man.hitbox[0] < z218.hitbox[0] + z218.hitbox[2]:
                    man.hit2()
        if z219.visible == True:
            if man.hitbox[1]  < z219.hitbox[1]+z219.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z219.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z219.hitbox[0] and man.hitbox[0] < z219.hitbox[0] + z219.hitbox[2]:
                    man.hit2()
        if z220.visible == True:
            if man.hitbox[1]  < z220.hitbox[1]+z220.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z220.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z220.hitbox[0] and man.hitbox[0] < z220.hitbox[0] + z220.hitbox[2]:
                    man.hit2()
        if z221.visible == True:
            if man.hitbox[1]  < z221.hitbox[1]+z221.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z221.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z221.hitbox[0] and man.hitbox[0] < z221.hitbox[0] + z221.hitbox[2]:
                    man.hit2()
        if z222.visible == True:
            if man.hitbox[1]  < z222.hitbox[1]+z222.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z222.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z222.hitbox[0] and man.hitbox[0] < z222.hitbox[0] + z222.hitbox[2]:
                    man.hit2()
        if z223.visible == True:
            if man.hitbox[1]  < z223.hitbox[1]+z223.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z223.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z223.hitbox[0] and man.hitbox[0] < z223.hitbox[0] + z223.hitbox[2]:
                    man.hit2()
        if z224.visible == True:
            if man.hitbox[1]  < z224.hitbox[1]+z224.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z224.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z224.hitbox[0] and man.hitbox[0] < z224.hitbox[0] + z224.hitbox[2]:
                    man.hit2()
        if z225.visible == True:
            if man.hitbox[1]  < z225.hitbox[1]+z225.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z225.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z225.hitbox[0] and man.hitbox[0] < z225.hitbox[0] + z225.hitbox[2]:
                    man.hit2()
        if z226.visible == True:
            if man.hitbox[1]  < z226.hitbox[1]+z226.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z226.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z226.hitbox[0] and man.hitbox[0] < z226.hitbox[0] + z226.hitbox[2]:
                    man.hit2()
        if z227.visible == True:
            if man.hitbox[1]  < z227.hitbox[1]+z227.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z227.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z227.hitbox[0] and man.hitbox[0] < z227.hitbox[0] + z227.hitbox[2]:
                    man.hit2()
        if z228.visible == True:
            if man.hitbox[1]  < z228.hitbox[1]+z228.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z228.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z228.hitbox[0] and man.hitbox[0] < z228.hitbox[0] + z228.hitbox[2]:
                    man.hit2()
        if z229.visible == True:
            if man.hitbox[1]  < z229.hitbox[1]+z229.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z229.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z229.hitbox[0] and man.hitbox[0] < z229.hitbox[0] + z229.hitbox[2]:
                    man.hit2()
        if z230.visible == True:
            if man.hitbox[1]  < z230.hitbox[1]+z230.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z230.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z230.hitbox[0] and man.hitbox[0] < z230.hitbox[0] + z230.hitbox[2]:
                    man.hit2()
        if z231.visible == True:
            if man.hitbox[1]  < z231.hitbox[1]+z231.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z231.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z231.hitbox[0] and man.hitbox[0] < z231.hitbox[0] + z231.hitbox[2]:
                    man.hit2()
        if z232.visible == True:
            if man.hitbox[1]  < z232.hitbox[1]+z232.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z232.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z232.hitbox[0] and man.hitbox[0] < z232.hitbox[0] + z232.hitbox[2]:
                    man.hit2()
        if z233.visible == True:
            if man.hitbox[1]  < z233.hitbox[1]+z233.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z233.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z233.hitbox[0] and man.hitbox[0] < z233.hitbox[0] + z233.hitbox[2]:
                    man.hit2()
        if z234.visible == True:
            if man.hitbox[1]  < z234.hitbox[1]+z234.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z234.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z234.hitbox[0] and man.hitbox[0] < z234.hitbox[0] + z234.hitbox[2]:
                    man.hit2()
        if z235.visible == True:
            if man.hitbox[1]  < z235.hitbox[1]+z235.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z235.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z235.hitbox[0] and man.hitbox[0] < z235.hitbox[0] + z235.hitbox[2]:
                    man.hit2()
        if z236.visible == True:
            if man.hitbox[1]  < z236.hitbox[1]+z236.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z236.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z236.hitbox[0] and man.hitbox[0] < z236.hitbox[0] + z236.hitbox[2]:
                    man.hit2()
        if z237.visible == True:
            if man.hitbox[1]  < z237.hitbox[1]+z237.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z237.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z237.hitbox[0] and man.hitbox[0] < z237.hitbox[0] + z237.hitbox[2]:
                    man.hit2()
        if z238.visible == True:
            if man.hitbox[1]  < z238.hitbox[1]+z238.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z238.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z238.hitbox[0] and man.hitbox[0] < z238.hitbox[0] + z238.hitbox[2]:
                    man.hit2()
        if z239.visible == True:
            if man.hitbox[1]  < z239.hitbox[1]+z239.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z239.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z239.hitbox[0] and man.hitbox[0] < z239.hitbox[0] + z239.hitbox[2]:
                    man.hit2()
        if z240.visible == True:
            if man.hitbox[1]  < z240.hitbox[1]+z240.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z240.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z240.hitbox[0] and man.hitbox[0] < z240.hitbox[0] + z240.hitbox[2]:
                    man.hit2()


        if z31.visible == True:
            if man.hitbox[1]  < z31.hitbox[1]+z31.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z31.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z31.hitbox[0] and man.hitbox[0] < z31.hitbox[0] + z31.hitbox[2]:
                    man.hit3()
        if z32.visible == True:
            if man.hitbox[1]  < z32.hitbox[1]+z32.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z32.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z32.hitbox[0] and man.hitbox[0] < z32.hitbox[0] + z32.hitbox[2]:
                    man.hit3()
        if z33.visible == True:
            if man.hitbox[1]  < z33.hitbox[1]+z33.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z33.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z33.hitbox[0] and man.hitbox[0] < z33.hitbox[0] + z33.hitbox[2]:
                    man.hit3()
        if z34.visible == True:
            if man.hitbox[1]  < z34.hitbox[1]+z34.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z34.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z34.hitbox[0] and man.hitbox[0] < z34.hitbox[0] + z34.hitbox[2]:
                    man.hit3()
        if z35.visible == True:
            if man.hitbox[1]  < z35.hitbox[1]+z35.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z35.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z35.hitbox[0] and man.hitbox[0] < z35.hitbox[0] + z35.hitbox[2]:
                    man.hit3()
        if z36.visible == True:
            if man.hitbox[1]  < z36.hitbox[1]+z36.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z36.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z36.hitbox[0] and man.hitbox[0] < z36.hitbox[0] + z36.hitbox[2]:
                    man.hit3()
        if z37.visible == True:
            if man.hitbox[1]  < z37.hitbox[1]+z37.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z37.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z37.hitbox[0] and man.hitbox[0] < z37.hitbox[0] + z37.hitbox[2]:
                    man.hit3()
        if z38.visible == True:
            if man.hitbox[1]  < z38.hitbox[1]+z38.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z38.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z38.hitbox[0] and man.hitbox[0] < z38.hitbox[0] + z38.hitbox[2]:
                    man.hit3()
        if z39.visible == True:
            if man.hitbox[1]  < z39.hitbox[1]+z39.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z39.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z39.hitbox[0] and man.hitbox[0] < z39.hitbox[0] + z39.hitbox[2]:
                    man.hit3()
        if z310.visible == True:
            if man.hitbox[1]  < z310.hitbox[1]+z310.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z310.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z310.hitbox[0] and man.hitbox[0] < z310.hitbox[0] + z310.hitbox[2]:
                    man.hit3()
        if z311.visible == True:
            if man.hitbox[1]  < z311.hitbox[1]+z311.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z311.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z311.hitbox[0] and man.hitbox[0] < z311.hitbox[0] + z311.hitbox[2]:
                    man.hit3()
        if z312.visible == True:
            if man.hitbox[1]  < z312.hitbox[1]+z312.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z312.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z312.hitbox[0] and man.hitbox[0] < z312.hitbox[0] + z312.hitbox[2]:
                    man.hit3()
        if z313.visible == True:
            if man.hitbox[1]  < z313.hitbox[1]+z313.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z313.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z313.hitbox[0] and man.hitbox[0] < z313.hitbox[0] + z313.hitbox[2]:
                    man.hit3()
        if z314.visible == True:
            if man.hitbox[1]  < z314.hitbox[1]+z314.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z314.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z314.hitbox[0] and man.hitbox[0] < z314.hitbox[0] + z314.hitbox[2]:
                    man.hit3()
        if z315.visible == True:
            if man.hitbox[1]  < z315.hitbox[1]+z315.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z315.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z315.hitbox[0] and man.hitbox[0] < z315.hitbox[0] + z315.hitbox[2]:
                    man.hit3()
        






        if z41.visible == True:
            if man.hitbox[1]  < z41.hitbox[1]+z41.hitbox[3] and man.hitbox[1] + man.hitbox[3] > z41.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > z41.hitbox[0] and man.hitbox[0] < z41.hitbox[0] + z41.hitbox[2]:
                    man.hit4()

                    
        if md1.visible ==True:
            if man.hitbox[1]  < md1.hitbox[1]+md1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > md1.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > md1.hitbox[0] and man.hitbox[0] < md1.hitbox[0] + md1.hitbox[2]:
                    man.getmd()
                    md1.visible=False
        if md2.visible ==True:
            if man.hitbox[1]  <  md2.hitbox[1]+md2.hitbox[3] and man.hitbox[1] + man.hitbox[3] > md2.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > md2.hitbox[0] and man.hitbox[0] < md2.hitbox[0] + md2.hitbox[2]:
                    man.getmd()
                    md2.visible=False
        if md3.visible ==True:
            if man.hitbox[1]  < md3.hitbox[1]+md3.hitbox[3] and man.hitbox[1] + man.hitbox[3] > md3.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > md3.hitbox[0] and man.hitbox[0] < md3.hitbox[0] + md3.hitbox[2]:
                    man.getmd()
                    md3.visible=False



        
        if slow >0:
            slow+=1
        if slow>2:
            slow = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for bullet in bullets:
        
            if z11.visible == True:
                if bullet.y - bullet.radius < z11.hitbox[1]+z11.hitbox[3] and bullet.y + bullet.radius > z11.hitbox[1]:
                    if bullet.x + bullet.radius > z11.hitbox[0] and bullet.x - bullet.radius< z11.hitbox[0] + z11.hitbox[2]:
                        z11.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z12.visible == True:
                if bullet.y - bullet.radius < z12.hitbox[1]+z11.hitbox[3] and bullet.y + bullet.radius > z12.hitbox[1]:
                    if bullet.x + bullet.radius > z12.hitbox[0] and bullet.x - bullet.radius< z12.hitbox[0] + z12.hitbox[2]:
                        z12.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z13.visible == True:
                if bullet.y - bullet.radius < z13.hitbox[1]+z13.hitbox[3] and bullet.y + bullet.radius > z13.hitbox[1]:
                    if bullet.x + bullet.radius > z13.hitbox[0] and bullet.x - bullet.radius< z13.hitbox[0] + z13.hitbox[2]:
                        z13.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z14.visible == True:
                if bullet.y - bullet.radius < z14.hitbox[1]+z14.hitbox[3] and bullet.y + bullet.radius > z14.hitbox[1]:
                    if bullet.x + bullet.radius > z14.hitbox[0] and bullet.x - bullet.radius< z14.hitbox[0] + z14.hitbox[2]:
                        z14.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z15.visible == True:
                if bullet.y - bullet.radius < z15.hitbox[1]+z15.hitbox[3] and bullet.y + bullet.radius > z15.hitbox[1]:
                    if bullet.x + bullet.radius > z15.hitbox[0] and bullet.x - bullet.radius< z15.hitbox[0] + z15.hitbox[2]:
                        z15.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z16.visible == True:
                if bullet.y - bullet.radius < z16.hitbox[1]+z16.hitbox[3] and bullet.y + bullet.radius > z16.hitbox[1]:
                    if bullet.x + bullet.radius > z16.hitbox[0] and bullet.x - bullet.radius< z16.hitbox[0] + z16.hitbox[2]:
                        z16.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z17.visible == True:
                if bullet.y - bullet.radius < z17.hitbox[1]+z17.hitbox[3] and bullet.y + bullet.radius > z17.hitbox[1]:
                    if bullet.x + bullet.radius > z17.hitbox[0] and bullet.x - bullet.radius< z17.hitbox[0] + z17.hitbox[2]:
                        z17.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z18.visible == True:
                if bullet.y - bullet.radius < z18.hitbox[1]+z18.hitbox[3] and bullet.y + bullet.radius > z18.hitbox[1]:
                    if bullet.x + bullet.radius > z18.hitbox[0] and bullet.x - bullet.radius< z18.hitbox[0] + z18.hitbox[2]:
                        z18.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z19.visible == True:
                if bullet.y - bullet.radius < z19.hitbox[1]+z19.hitbox[3] and bullet.y + bullet.radius > z19.hitbox[1]:
                    if bullet.x + bullet.radius > z19.hitbox[0] and bullet.x - bullet.radius< z19.hitbox[0] + z19.hitbox[2]:
                        z19.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z110.visible == True:
                if bullet.y - bullet.radius < z110.hitbox[1]+z110.hitbox[3] and bullet.y + bullet.radius > z110.hitbox[1]:
                    if bullet.x + bullet.radius > z110.hitbox[0] and bullet.x - bullet.radius< z110.hitbox[0] + z110.hitbox[2]:
                        z110.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z111.visible == True:
                if bullet.y - bullet.radius < z111.hitbox[1]+z111.hitbox[3] and bullet.y + bullet.radius > z111.hitbox[1]:
                    if bullet.x + bullet.radius > z111.hitbox[0] and bullet.x - bullet.radius< z111.hitbox[0] + z111.hitbox[2]:
                        z111.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z112.visible == True:
                if bullet.y - bullet.radius < z112.hitbox[1]+z112.hitbox[3] and bullet.y + bullet.radius > z112.hitbox[1]:
                    if bullet.x + bullet.radius > z112.hitbox[0] and bullet.x - bullet.radius< z112.hitbox[0] + z112.hitbox[2]:
                        z112.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z113.visible == True:
                if bullet.y - bullet.radius < z113.hitbox[1]+z113.hitbox[3] and bullet.y + bullet.radius > z113.hitbox[1]:
                    if bullet.x + bullet.radius > z113.hitbox[0] and bullet.x - bullet.radius< z113.hitbox[0] + z113.hitbox[2]:
                        z113.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z114.visible == True:
                if bullet.y - bullet.radius < z114.hitbox[1]+z114.hitbox[3] and bullet.y + bullet.radius > z114.hitbox[1]:
                    if bullet.x + bullet.radius > z114.hitbox[0] and bullet.x - bullet.radius< z114.hitbox[0] + z114.hitbox[2]:
                        z114.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z115.visible == True:
                if bullet.y - bullet.radius < z115.hitbox[1]+z115.hitbox[3] and bullet.y + bullet.radius > z115.hitbox[1]:
                    if bullet.x + bullet.radius > z115.hitbox[0] and bullet.x - bullet.radius< z115.hitbox[0] + z115.hitbox[2]:
                        z115.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z116.visible == True:
                if bullet.y - bullet.radius < z116.hitbox[1]+z116.hitbox[3] and bullet.y + bullet.radius > z116.hitbox[1]:
                    if bullet.x + bullet.radius > z116.hitbox[0] and bullet.x - bullet.radius< z116.hitbox[0] + z116.hitbox[2]:
                        z116.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z117.visible == True:
                if bullet.y - bullet.radius < z117.hitbox[1]+z117.hitbox[3] and bullet.y + bullet.radius > z117.hitbox[1]:
                    if bullet.x + bullet.radius > z117.hitbox[0] and bullet.x - bullet.radius< z117.hitbox[0] + z117.hitbox[2]:
                        z117.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z118.visible == True:
                if bullet.y - bullet.radius < z118.hitbox[1]+z118.hitbox[3] and bullet.y + bullet.radius > z118.hitbox[1]:
                    if bullet.x + bullet.radius > z118.hitbox[0] and bullet.x - bullet.radius< z118.hitbox[0] + z118.hitbox[2]:
                        z118.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z119.visible == True:
                if bullet.y - bullet.radius < z119.hitbox[1]+z119.hitbox[3] and bullet.y + bullet.radius > z119.hitbox[1]:
                    if bullet.x + bullet.radius > z119.hitbox[0] and bullet.x - bullet.radius< z119.hitbox[0] + z119.hitbox[2]:
                        z119.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z120.visible == True:
                if bullet.y - bullet.radius < z120.hitbox[1]+z120.hitbox[3] and bullet.y + bullet.radius > z120.hitbox[1]:
                    if bullet.x + bullet.radius > z120.hitbox[0] and bullet.x - bullet.radius< z120.hitbox[0] + z120.hitbox[2]:
                        z120.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z121.visible == True:
                if bullet.y - bullet.radius < z121.hitbox[1]+z121.hitbox[3] and bullet.y + bullet.radius > z121.hitbox[1]:
                    if bullet.x + bullet.radius > z121.hitbox[0] and bullet.x - bullet.radius< z121.hitbox[0] + z121.hitbox[2]:
                        z121.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z122.visible == True:
                if bullet.y - bullet.radius < z122.hitbox[1]+z122.hitbox[3] and bullet.y + bullet.radius > z122.hitbox[1]:
                    if bullet.x + bullet.radius > z122.hitbox[0] and bullet.x - bullet.radius< z122.hitbox[0] + z122.hitbox[2]:
                        z122.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z123.visible == True:
                if bullet.y - bullet.radius < z123.hitbox[1]+z123.hitbox[3] and bullet.y + bullet.radius > z123.hitbox[1]:
                    if bullet.x + bullet.radius > z123.hitbox[0] and bullet.x - bullet.radius< z123.hitbox[0] + z123.hitbox[2]:
                        z123.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z124.visible == True:
                if bullet.y - bullet.radius < z124.hitbox[1]+z124.hitbox[3] and bullet.y + bullet.radius > z124.hitbox[1]:
                    if bullet.x + bullet.radius > z124.hitbox[0] and bullet.x - bullet.radius< z124.hitbox[0] + z124.hitbox[2]:
                        z124.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z125.visible == True:
                if bullet.y - bullet.radius < z125.hitbox[1]+z125.hitbox[3] and bullet.y + bullet.radius > z125.hitbox[1]:
                    if bullet.x + bullet.radius > z125.hitbox[0] and bullet.x - bullet.radius< z125.hitbox[0] + z125.hitbox[2]:
                        z125.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z126.visible == True:
                if bullet.y - bullet.radius < z126.hitbox[1]+z126.hitbox[3] and bullet.y + bullet.radius > z126.hitbox[1]:
                    if bullet.x + bullet.radius > z126.hitbox[0] and bullet.x - bullet.radius< z126.hitbox[0] + z126.hitbox[2]:
                        z126.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z127.visible == True:
                if bullet.y - bullet.radius < z127.hitbox[1]+z127.hitbox[3] and bullet.y + bullet.radius > z127.hitbox[1]:
                    if bullet.x + bullet.radius > z127.hitbox[0] and bullet.x - bullet.radius< z127.hitbox[0] + z127.hitbox[2]:
                        z127.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z128.visible == True:
                if bullet.y - bullet.radius < z128.hitbox[1]+z128.hitbox[3] and bullet.y + bullet.radius > z128.hitbox[1]:
                    if bullet.x + bullet.radius > z128.hitbox[0] and bullet.x - bullet.radius< z128.hitbox[0] + z128.hitbox[2]:
                        z128.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z129.visible == True:
                if bullet.y - bullet.radius < z129.hitbox[1]+z129.hitbox[3] and bullet.y + bullet.radius > z129.hitbox[1]:
                    if bullet.x + bullet.radius > z129.hitbox[0] and bullet.x - bullet.radius< z129.hitbox[0] + z129.hitbox[2]:
                        z129.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z130.visible == True:
                if bullet.y - bullet.radius < z130.hitbox[1]+z130.hitbox[3] and bullet.y + bullet.radius > z130.hitbox[1]:
                    if bullet.x + bullet.radius > z130.hitbox[0] and bullet.x - bullet.radius< z130.hitbox[0] + z130.hitbox[2]:
                        z130.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z131.visible == True:
                if bullet.y - bullet.radius < z131.hitbox[1]+z131.hitbox[3] and bullet.y + bullet.radius > z131.hitbox[1]:
                    if bullet.x + bullet.radius > z131.hitbox[0] and bullet.x - bullet.radius< z131.hitbox[0] + z131.hitbox[2]:
                        z131.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z132.visible == True:
                if bullet.y - bullet.radius < z132.hitbox[1]+z132.hitbox[3] and bullet.y + bullet.radius > z132.hitbox[1]:
                    if bullet.x + bullet.radius > z132.hitbox[0] and bullet.x - bullet.radius< z132.hitbox[0] + z132.hitbox[2]:
                        z132.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z133.visible == True:
                if bullet.y - bullet.radius < z133.hitbox[1]+z133.hitbox[3] and bullet.y + bullet.radius > z133.hitbox[1]:
                    if bullet.x + bullet.radius > z133.hitbox[0] and bullet.x - bullet.radius< z133.hitbox[0] + z133.hitbox[2]:
                        z133.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z134.visible == True:
                if bullet.y - bullet.radius < z134.hitbox[1]+z134.hitbox[3] and bullet.y + bullet.radius > z134.hitbox[1]:
                    if bullet.x + bullet.radius > z134.hitbox[0] and bullet.x - bullet.radius< z134.hitbox[0] + z134.hitbox[2]:
                        z134.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z135.visible == True:
                if bullet.y - bullet.radius < z135.hitbox[1]+z135.hitbox[3] and bullet.y + bullet.radius > z135.hitbox[1]:
                    if bullet.x + bullet.radius > z135.hitbox[0] and bullet.x - bullet.radius< z135.hitbox[0] + z135.hitbox[2]:
                        z135.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z136.visible == True:
                if bullet.y - bullet.radius < z136.hitbox[1]+z136.hitbox[3] and bullet.y + bullet.radius > z136.hitbox[1]:
                    if bullet.x + bullet.radius > z136.hitbox[0] and bullet.x - bullet.radius< z136.hitbox[0] + z136.hitbox[2]:
                        z136.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z137.visible == True:
                if bullet.y - bullet.radius < z137.hitbox[1]+z137.hitbox[3] and bullet.y + bullet.radius > z137.hitbox[1]:
                    if bullet.x + bullet.radius > z137.hitbox[0] and bullet.x - bullet.radius< z137.hitbox[0] + z137.hitbox[2]:
                        z137.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z138.visible == True:
                if bullet.y - bullet.radius < z138.hitbox[1]+z138.hitbox[3] and bullet.y + bullet.radius > z138.hitbox[1]:
                    if bullet.x + bullet.radius > z138.hitbox[0] and bullet.x - bullet.radius< z138.hitbox[0] + z138.hitbox[2]:
                        z138.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z139.visible == True:
                if bullet.y - bullet.radius < z139.hitbox[1]+z139.hitbox[3] and bullet.y + bullet.radius > z139.hitbox[1]:
                    if bullet.x + bullet.radius > z139.hitbox[0] and bullet.x - bullet.radius< z139.hitbox[0] + z139.hitbox[2]:
                        z139.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z140.visible == True:
                if bullet.y - bullet.radius < z140.hitbox[1]+z140.hitbox[3] and bullet.y + bullet.radius > z140.hitbox[1]:
                    if bullet.x + bullet.radius > z140.hitbox[0] and bullet.x - bullet.radius< z140.hitbox[0] + z140.hitbox[2]:
                        z140.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z141.visible == True:
                if bullet.y - bullet.radius < z141.hitbox[1]+z141.hitbox[3] and bullet.y + bullet.radius > z141.hitbox[1]:
                    if bullet.x + bullet.radius > z141.hitbox[0] and bullet.x - bullet.radius< z141.hitbox[0] + z141.hitbox[2]:
                        z141.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z142.visible == True:
                if bullet.y - bullet.radius < z142.hitbox[1]+z142.hitbox[3] and bullet.y + bullet.radius > z142.hitbox[1]:
                    if bullet.x + bullet.radius > z142.hitbox[0] and bullet.x - bullet.radius< z142.hitbox[0] + z142.hitbox[2]:
                        z142.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z143.visible == True:
                if bullet.y - bullet.radius < z143.hitbox[1]+z143.hitbox[3] and bullet.y + bullet.radius > z143.hitbox[1]:
                    if bullet.x + bullet.radius > z143.hitbox[0] and bullet.x - bullet.radius< z143.hitbox[0] + z143.hitbox[2]:
                        z143.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z144.visible == True:
                if bullet.y - bullet.radius < z144.hitbox[1]+z144.hitbox[3] and bullet.y + bullet.radius > z144.hitbox[1]:
                    if bullet.x + bullet.radius > z144.hitbox[0] and bullet.x - bullet.radius< z144.hitbox[0] + z144.hitbox[2]:
                        z144.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z145.visible == True:
                if bullet.y - bullet.radius < z145.hitbox[1]+z145.hitbox[3] and bullet.y + bullet.radius > z145.hitbox[1]:
                    if bullet.x + bullet.radius > z145.hitbox[0] and bullet.x - bullet.radius< z145.hitbox[0] + z145.hitbox[2]:
                        z145.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z146.visible == True:
                if bullet.y - bullet.radius < z146.hitbox[1]+z146.hitbox[3] and bullet.y + bullet.radius > z146.hitbox[1]:
                    if bullet.x + bullet.radius > z146.hitbox[0] and bullet.x - bullet.radius< z146.hitbox[0] + z146.hitbox[2]:
                        z146.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z147.visible == True:
                if bullet.y - bullet.radius < z147.hitbox[1]+z147.hitbox[3] and bullet.y + bullet.radius > z147.hitbox[1]:
                    if bullet.x + bullet.radius > z147.hitbox[0] and bullet.x - bullet.radius< z147.hitbox[0] + z147.hitbox[2]:
                        z147.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z148.visible == True:
                if bullet.y - bullet.radius < z148.hitbox[1]+z148.hitbox[3] and bullet.y + bullet.radius > z148.hitbox[1]:
                    if bullet.x + bullet.radius > z148.hitbox[0] and bullet.x - bullet.radius< z148.hitbox[0] + z148.hitbox[2]:
                        z148.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z149.visible == True:
                if bullet.y - bullet.radius < z149.hitbox[1]+z149.hitbox[3] and bullet.y + bullet.radius > z149.hitbox[1]:
                    if bullet.x + bullet.radius > z149.hitbox[0] and bullet.x - bullet.radius< z149.hitbox[0] + z149.hitbox[2]:
                        z149.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z150.visible == True:
                if bullet.y - bullet.radius < z150.hitbox[1]+z150.hitbox[3] and bullet.y + bullet.radius > z150.hitbox[1]:
                    if bullet.x + bullet.radius > z150.hitbox[0] and bullet.x - bullet.radius< z150.hitbox[0] + z150.hitbox[2]:
                        z150.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))



                            
            if z21.visible == True:
                if bullet.y - bullet.radius < z21.hitbox[1]+z21.hitbox[3] and bullet.y + bullet.radius > z21.hitbox[1]:
                    if bullet.x + bullet.radius > z21.hitbox[0] and bullet.x - bullet.radius< z21.hitbox[0] + z21.hitbox[2]:
                        z21.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z22.visible == True:
                if bullet.y - bullet.radius < z22.hitbox[1]+z21.hitbox[3] and bullet.y + bullet.radius > z22.hitbox[1]:
                    if bullet.x + bullet.radius > z22.hitbox[0] and bullet.x - bullet.radius< z22.hitbox[0] + z22.hitbox[2]:
                        z22.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z23.visible == True:
                if bullet.y - bullet.radius < z23.hitbox[1]+z23.hitbox[3] and bullet.y + bullet.radius > z23.hitbox[1]:
                    if bullet.x + bullet.radius > z23.hitbox[0] and bullet.x - bullet.radius< z23.hitbox[0] + z23.hitbox[2]:
                        z23.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z24.visible == True:
                if bullet.y - bullet.radius < z24.hitbox[1]+z24.hitbox[3] and bullet.y + bullet.radius > z24.hitbox[1]:
                    if bullet.x + bullet.radius > z24.hitbox[0] and bullet.x - bullet.radius< z24.hitbox[0] + z24.hitbox[2]:
                        z24.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z25.visible == True:
                if bullet.y - bullet.radius < z25.hitbox[1]+z25.hitbox[3] and bullet.y + bullet.radius > z25.hitbox[1]:
                    if bullet.x + bullet.radius > z25.hitbox[0] and bullet.x - bullet.radius< z25.hitbox[0] + z25.hitbox[2]:
                        z25.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z26.visible == True:
                if bullet.y - bullet.radius < z21.hitbox[1]+z21.hitbox[3] and bullet.y + bullet.radius > z21.hitbox[1]:
                    if bullet.x + bullet.radius > z21.hitbox[0] and bullet.x - bullet.radius< z21.hitbox[0] + z21.hitbox[2]:
                        z26.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z27.visible == True:
                if bullet.y - bullet.radius < z27.hitbox[1]+z27.hitbox[3] and bullet.y + bullet.radius > z27.hitbox[1]:
                    if bullet.x + bullet.radius > z27.hitbox[0] and bullet.x - bullet.radius< z27.hitbox[0] + z27.hitbox[2]:
                        z27.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z28.visible == True:
                if bullet.y - bullet.radius < z28.hitbox[1]+z28.hitbox[3] and bullet.y + bullet.radius > z28.hitbox[1]:
                    if bullet.x + bullet.radius > z28.hitbox[0] and bullet.x - bullet.radius< z28.hitbox[0] + z28.hitbox[2]:
                        z28.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z29.visible == True:
                if bullet.y - bullet.radius < z29.hitbox[1]+z29.hitbox[3] and bullet.y + bullet.radius > z29.hitbox[1]:
                    if bullet.x + bullet.radius > z29.hitbox[0] and bullet.x - bullet.radius< z29.hitbox[0] + z29.hitbox[2]:
                        z29.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z210.visible == True:
                if bullet.y - bullet.radius < z210.hitbox[1]+z210.hitbox[3] and bullet.y + bullet.radius > z210.hitbox[1]:
                    if bullet.x + bullet.radius > z210.hitbox[0] and bullet.x - bullet.radius< z210.hitbox[0] + z210.hitbox[2]:
                        z210.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z211.visible == True:
                if bullet.y - bullet.radius < z211.hitbox[1]+z211.hitbox[3] and bullet.y + bullet.radius > z211.hitbox[1]:
                    if bullet.x + bullet.radius > z211.hitbox[0] and bullet.x - bullet.radius< z211.hitbox[0] + z211.hitbox[2]:
                        z211.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z212.visible == True:
                if bullet.y - bullet.radius < z212.hitbox[1]+z212.hitbox[3] and bullet.y + bullet.radius > z212.hitbox[1]:
                    if bullet.x + bullet.radius > z212.hitbox[0] and bullet.x - bullet.radius< z212.hitbox[0] + z212.hitbox[2]:
                        z212.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z213.visible == True:
                if bullet.y - bullet.radius < z213.hitbox[1]+z213.hitbox[3] and bullet.y + bullet.radius > z213.hitbox[1]:
                    if bullet.x + bullet.radius > z213.hitbox[0] and bullet.x - bullet.radius< z213.hitbox[0] + z213.hitbox[2]:
                        z213.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z214.visible == True:
                if bullet.y - bullet.radius < z214.hitbox[1]+z214.hitbox[3] and bullet.y + bullet.radius > z214.hitbox[1]:
                    if bullet.x + bullet.radius > z214.hitbox[0] and bullet.x - bullet.radius< z214.hitbox[0] + z214.hitbox[2]:
                        z214.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z215.visible == True:
                if bullet.y - bullet.radius < z215.hitbox[1]+z215.hitbox[3] and bullet.y + bullet.radius > z215.hitbox[1]:
                    if bullet.x + bullet.radius > z215.hitbox[0] and bullet.x - bullet.radius< z215.hitbox[0] + z215.hitbox[2]:
                        z215.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z216.visible == True:
                if bullet.y - bullet.radius < z216.hitbox[1]+z216.hitbox[3] and bullet.y + bullet.radius > z216.hitbox[1]:
                    if bullet.x + bullet.radius > z216.hitbox[0] and bullet.x - bullet.radius< z216.hitbox[0] + z216.hitbox[2]:
                        z216.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z217.visible == True:
                if bullet.y - bullet.radius < z217.hitbox[1]+z217.hitbox[3] and bullet.y + bullet.radius > z217.hitbox[1]:
                    if bullet.x + bullet.radius > z217.hitbox[0] and bullet.x - bullet.radius< z217.hitbox[0] + z217.hitbox[2]:
                        z217.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z218.visible == True:
                if bullet.y - bullet.radius < z218.hitbox[1]+z218.hitbox[3] and bullet.y + bullet.radius > z218.hitbox[1]:
                    if bullet.x + bullet.radius > z218.hitbox[0] and bullet.x - bullet.radius< z218.hitbox[0] + z218.hitbox[2]:
                        z218.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z219.visible == True:
                if bullet.y - bullet.radius < z219.hitbox[1]+z219.hitbox[3] and bullet.y + bullet.radius > z219.hitbox[1]:
                    if bullet.x + bullet.radius > z219.hitbox[0] and bullet.x - bullet.radius< z219.hitbox[0] + z219.hitbox[2]:
                        z219.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z220.visible == True:
                if bullet.y - bullet.radius < z220.hitbox[1]+z220.hitbox[3] and bullet.y + bullet.radius > z220.hitbox[1]:
                    if bullet.x + bullet.radius > z220.hitbox[0] and bullet.x - bullet.radius< z210.hitbox[0] + z220.hitbox[2]:
                        z220.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
        
            if z221.visible == True:
                if bullet.y - bullet.radius < z221.hitbox[1]+z221.hitbox[3] and bullet.y + bullet.radius > z221.hitbox[1]:
                    if bullet.x + bullet.radius > z221.hitbox[0] and bullet.x - bullet.radius< z221.hitbox[0] + z221.hitbox[2]:
                        z221.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z222.visible == True:
                if bullet.y - bullet.radius < z222.hitbox[1]+z222.hitbox[3] and bullet.y + bullet.radius > z222.hitbox[1]:
                    if bullet.x + bullet.radius > z222.hitbox[0] and bullet.x - bullet.radius< z222.hitbox[0] + z222.hitbox[2]:
                        z222.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z223.visible == True:
                if bullet.y - bullet.radius < z223.hitbox[1]+z223.hitbox[3] and bullet.y + bullet.radius > z223.hitbox[1]:
                    if bullet.x + bullet.radius > z223.hitbox[0] and bullet.x - bullet.radius< z223.hitbox[0] + z223.hitbox[2]:
                        z223.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z224.visible == True:
                if bullet.y - bullet.radius < z224.hitbox[1]+z224.hitbox[3] and bullet.y + bullet.radius > z224.hitbox[1]:
                    if bullet.x + bullet.radius > z224.hitbox[0] and bullet.x - bullet.radius< z224.hitbox[0] + z224.hitbox[2]:
                        z224.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z225.visible == True:
                if bullet.y - bullet.radius < z225.hitbox[1]+z225.hitbox[3] and bullet.y + bullet.radius > z225.hitbox[1]:
                    if bullet.x + bullet.radius > z225.hitbox[0] and bullet.x - bullet.radius< z225.hitbox[0] + z225.hitbox[2]:
                        z225.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z226.visible == True:
                if bullet.y - bullet.radius < z226.hitbox[1]+z226.hitbox[3] and bullet.y + bullet.radius > z226.hitbox[1]:
                    if bullet.x + bullet.radius > z226.hitbox[0] and bullet.x - bullet.radius< z226.hitbox[0] + z226.hitbox[2]:
                        z226.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z227.visible == True:
                if bullet.y - bullet.radius < z227.hitbox[1]+z227.hitbox[3] and bullet.y + bullet.radius > z227.hitbox[1]:
                    if bullet.x + bullet.radius > z227.hitbox[0] and bullet.x - bullet.radius< z227.hitbox[0] + z227.hitbox[2]:
                        z227.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z228.visible == True:
                if bullet.y - bullet.radius < z228.hitbox[1]+z228.hitbox[3] and bullet.y + bullet.radius > z228.hitbox[1]:
                    if bullet.x + bullet.radius > z228.hitbox[0] and bullet.x - bullet.radius< z228.hitbox[0] + z228.hitbox[2]:
                        z228.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z229.visible == True:
                if bullet.y - bullet.radius < z229.hitbox[1]+z229.hitbox[3] and bullet.y + bullet.radius > z229.hitbox[1]:
                    if bullet.x + bullet.radius > z229.hitbox[0] and bullet.x - bullet.radius< z229.hitbox[0] + z229.hitbox[2]:
                        z229.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z230.visible == True:
                if bullet.y - bullet.radius < z230.hitbox[1]+z230.hitbox[3] and bullet.y + bullet.radius > z230.hitbox[1]:
                    if bullet.x + bullet.radius > z230.hitbox[0] and bullet.x - bullet.radius< z230.hitbox[0] + z230.hitbox[2]:
                        z230.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z231.visible == True:
                if bullet.y - bullet.radius < z231.hitbox[1]+z231.hitbox[3] and bullet.y + bullet.radius > z231.hitbox[1]:
                    if bullet.x + bullet.radius > z231.hitbox[0] and bullet.x - bullet.radius< z231.hitbox[0] + z231.hitbox[2]:
                        z231.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z232.visible == True:
                if bullet.y - bullet.radius < z232.hitbox[1]+z232.hitbox[3] and bullet.y + bullet.radius > z232.hitbox[1]:
                    if bullet.x + bullet.radius > z232.hitbox[0] and bullet.x - bullet.radius< z232.hitbox[0] + z232.hitbox[2]:
                        z232.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z233.visible == True:
                if bullet.y - bullet.radius < z233.hitbox[1]+z233.hitbox[3] and bullet.y + bullet.radius > z233.hitbox[1]:
                    if bullet.x + bullet.radius > z233.hitbox[0] and bullet.x - bullet.radius< z233.hitbox[0] + z233.hitbox[2]:
                        z233.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z234.visible == True:
                if bullet.y - bullet.radius < z214.hitbox[1]+z214.hitbox[3] and bullet.y + bullet.radius > z214.hitbox[1]:
                    if bullet.x + bullet.radius > z214.hitbox[0] and bullet.x - bullet.radius< z214.hitbox[0] + z214.hitbox[2]:
                        z234.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z235.visible == True:
                if bullet.y - bullet.radius < z215.hitbox[1]+z215.hitbox[3] and bullet.y + bullet.radius > z215.hitbox[1]:
                    if bullet.x + bullet.radius > z215.hitbox[0] and bullet.x - bullet.radius< z215.hitbox[0] + z215.hitbox[2]:
                        z235.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z236.visible == True:
                if bullet.y - bullet.radius < z236.hitbox[1]+z236.hitbox[3] and bullet.y + bullet.radius > z236.hitbox[1]:
                    if bullet.x + bullet.radius > z236.hitbox[0] and bullet.x - bullet.radius< z236.hitbox[0] + z236.hitbox[2]:
                        z236.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z237.visible == True:
                if bullet.y - bullet.radius < z237.hitbox[1]+z237.hitbox[3] and bullet.y + bullet.radius > z237.hitbox[1]:
                    if bullet.x + bullet.radius > z237.hitbox[0] and bullet.x - bullet.radius< z237.hitbox[0] + z237.hitbox[2]:
                        z237.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z238.visible == True:
                if bullet.y - bullet.radius < z238.hitbox[1]+z238.hitbox[3] and bullet.y + bullet.radius > z238.hitbox[1]:
                    if bullet.x + bullet.radius > z238.hitbox[0] and bullet.x - bullet.radius< z238.hitbox[0] + z238.hitbox[2]:
                        z238.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z239.visible == True:
                if bullet.y - bullet.radius < z239.hitbox[1]+z239.hitbox[3] and bullet.y + bullet.radius > z239.hitbox[1]:
                    if bullet.x + bullet.radius > z239.hitbox[0] and bullet.x - bullet.radius< z239.hitbox[0] + z239.hitbox[2]:
                        z239.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z240.visible == True:
                if bullet.y - bullet.radius < z240.hitbox[1]+z240.hitbox[3] and bullet.y + bullet.radius > z240.hitbox[1]:
                    if bullet.x + bullet.radius > z240.hitbox[0] and bullet.x - bullet.radius< z240.hitbox[0] + z240.hitbox[2]:
                        z240.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))






            if z31.visible == True:
                if bullet.y - bullet.radius < z31.hitbox[1]+z31.hitbox[3] and bullet.y + bullet.radius > z31.hitbox[1]:
                    if bullet.x + bullet.radius > z31.hitbox[0] and bullet.x - bullet.radius< z31.hitbox[0] + z31.hitbox[2]:
                        z31.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z32.visible == True:
                if bullet.y - bullet.radius < z32.hitbox[1]+z32.hitbox[3] and bullet.y + bullet.radius > z32.hitbox[1]:
                    if bullet.x + bullet.radius > z32.hitbox[0] and bullet.x - bullet.radius< z32.hitbox[0] + z32.hitbox[2]:
                        z32.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z33.visible == True:
                if bullet.y - bullet.radius < z33.hitbox[1]+z33.hitbox[3] and bullet.y + bullet.radius > z33.hitbox[1]:
                    if bullet.x + bullet.radius > z33.hitbox[0] and bullet.x - bullet.radius< z33.hitbox[0] + z33.hitbox[2]:
                        z33.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z34.visible == True:
                if bullet.y - bullet.radius < z34.hitbox[1]+z34.hitbox[3] and bullet.y + bullet.radius > z34.hitbox[1]:
                    if bullet.x + bullet.radius > z34.hitbox[0] and bullet.x - bullet.radius< z34.hitbox[0] + z34.hitbox[2]:
                        z34.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z35.visible == True:
                if bullet.y - bullet.radius < z35.hitbox[1]+z35.hitbox[3] and bullet.y + bullet.radius > z35.hitbox[1]:
                    if bullet.x + bullet.radius > z35.hitbox[0] and bullet.x - bullet.radius< z35.hitbox[0] + z35.hitbox[2]:
                        z35.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z36.visible == True:
                if bullet.y - bullet.radius < z36.hitbox[1]+z36.hitbox[3] and bullet.y + bullet.radius > z36.hitbox[1]:
                    if bullet.x + bullet.radius > z36.hitbox[0] and bullet.x - bullet.radius< z36.hitbox[0] + z36.hitbox[2]:
                        z36.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z37.visible == True:
                if bullet.y - bullet.radius < z37.hitbox[1]+z37.hitbox[3] and bullet.y + bullet.radius > z37.hitbox[1]:
                    if bullet.x + bullet.radius > z37.hitbox[0] and bullet.x - bullet.radius< z37.hitbox[0] + z37.hitbox[2]:
                        z37.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z38.visible == True:
                if bullet.y - bullet.radius < z38.hitbox[1]+z38.hitbox[3] and bullet.y + bullet.radius > z38.hitbox[1]:
                    if bullet.x + bullet.radius > z38.hitbox[0] and bullet.x - bullet.radius< z38.hitbox[0] + z38.hitbox[2]:
                        z38.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z39.visible == True:
                if bullet.y - bullet.radius < z39.hitbox[1]+z39.hitbox[3] and bullet.y + bullet.radius > z39.hitbox[1]:
                    if bullet.x + bullet.radius > z39.hitbox[0] and bullet.x - bullet.radius< z39.hitbox[0] + z39.hitbox[2]:
                        z39.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z310.visible == True:
                if bullet.y - bullet.radius < z310.hitbox[1]+z310.hitbox[3] and bullet.y + bullet.radius > z310.hitbox[1]:
                    if bullet.x + bullet.radius > z310.hitbox[0] and bullet.x - bullet.radius< z310.hitbox[0] + z310.hitbox[2]:
                        z310.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z311.visible == True:
                if bullet.y - bullet.radius < z311.hitbox[1]+z311.hitbox[3] and bullet.y + bullet.radius > z311.hitbox[1]:
                    if bullet.x + bullet.radius > z311.hitbox[0] and bullet.x - bullet.radius< z311.hitbox[0] + z311.hitbox[2]:
                        z311.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z312.visible == True:
                if bullet.y - bullet.radius < z312.hitbox[1]+z312.hitbox[3] and bullet.y + bullet.radius > z312.hitbox[1]:
                    if bullet.x + bullet.radius > z312.hitbox[0] and bullet.x - bullet.radius< z312.hitbox[0] + z312.hitbox[2]:
                        z312.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z313.visible == True:
                if bullet.y - bullet.radius < z313.hitbox[1]+z313.hitbox[3] and bullet.y + bullet.radius > z313.hitbox[1]:
                    if bullet.x + bullet.radius > z313.hitbox[0] and bullet.x - bullet.radius< z313.hitbox[0] + z313.hitbox[2]:
                        z313.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z314.visible == True:
                if bullet.y - bullet.radius < z314.hitbox[1]+z314.hitbox[3] and bullet.y + bullet.radius > z314.hitbox[1]:
                    if bullet.x + bullet.radius > z314.hitbox[0] and bullet.x - bullet.radius< z314.hitbox[0] + z314.hitbox[2]:
                        z314.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            if z315.visible == True:
                if bullet.y - bullet.radius < z315.hitbox[1]+z315.hitbox[3] and bullet.y + bullet.radius > z315.hitbox[1]:
                    if bullet.x + bullet.radius > z315.hitbox[0] and bullet.x - bullet.radius< z315.hitbox[0] + z315.hitbox[2]:
                        z315.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))




                            
            if z41.visible == True:
                if bullet.y - bullet.radius < z41.hitbox[1]+z41.hitbox[3] and bullet.y + bullet.radius > z41.hitbox[1]:
                    if bullet.x + bullet.radius > z41.hitbox[0] and bullet.x - bullet.radius< z41.hitbox[0] + z41.hitbox[2]:
                        z41.hit()
                        if len(bullets)>0:
                            bullets.pop(bullets.index(bullet))
            
            

            
                    
            if man.left or man.right == True:
                if bullet.x < 900 and bullet.x > 0:
                    bullet.x += bullet.vel
                else:
                    if len(bullets)>0:
                        bullets.pop(bullets.index(bullet))
            else :
                if bullet.y<700 and bullet.y>0:
                    bullet.y+=bullet.vel
                else:
                    if len(bullets)>0:
                        bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]and slow ==0:
            man.shooting=True
            
            if man.left or man.right == True:
                if man.left:
                    facing = -1
                elif man.right :
                    facing = 1 
            else:
                if man.up:
                    facing = -1
                elif man.down:
                    facing = 1
            if r > 0:
                if len(bullets) < 1:
                    if man.right:
                        bullets.append(projectile(round(man.x + man.width //2+40), round(man.y + man.height//2-3), 4, (0,0,255), facing))
                    elif man.left:
                        bullets.append(projectile(round(man.x + man.width //2-40), round(man.y + man.height//2-5), 4, (0,0,255), facing))
                    elif man.up:
                        bullets.append(projectile(round(man.x + man.width //2+10), round(man.y + man.height//2-40), 4, (0,0,255), facing))
                    elif man.down:
                        bullets.append(projectile(round(man.x + man.width //2-10), round(man.y + man.height//2+40), 4, (0,0,255), facing))
                    r-=1
                    reload = False
            else:
                reload = True
            slow = 1
                
        if keys[pygame.K_r]:
            if reload == True:
                #reloadsound.play()
                r=r+100
                reload = False
                

        if keys[pygame.K_LEFT] and man.x > 40:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.up = False
            man.down = False
            man.standing = False
            man.shooting = False
            if keys[pygame.K_UP] and man.x >40:
                man.y-=man.vel
            elif keys[pygame.K_DOWN] and man.x >40:
                man.y+=man.vel
        elif keys[pygame.K_RIGHT] and man.x < 850:
            man.x += man.vel
            man.right = True
            man.left = False
            man.up = False
            man.down = False
            man.standing = False
            man.shooting = False
            if keys[pygame.K_UP]and man.x<850:
                man.y-=man.vel
            elif keys[pygame.K_DOWN]and man.x<850:
                man.y+=man.vel
        elif keys[pygame.K_UP] and man.y > 40 :
            man.y-= man.vel
            man.right = False
            man.left = False
            man.up = True
            man.down = False
            man.standing = False
            man.shooting = False
            if keys[pygame.K_LEFT]:
                man.x-=man.vel
            elif keys[pygame.K_RIGHT]:
                man.x+=man.vel
        elif keys[pygame.K_DOWN] and man.y < 650:
            man.y+=man.vel
            man.right = False
            man.left = False
            man.up = False
            man.down = True
            man.standing = False
            man.shooting = False
            if keys[pygame.K_LEFT]:
                man.x-=man.vel
            elif keys[pygame.K_RIGHT]:
                man.x+=man.vel
        else:
            man.standing = True
           
        j+=1
        redrawGameWindow()
ham = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Last room")
men = pygame.mixer.music.load('horror ambient.wav')
bg = pygame.image.load('menu.png')
bt1=pygame.image.load('menu2.png')
bt11=pygame.image.load('menu21.png')
bt2=pygame.image.load('menu3.png')
bt22=pygame.image.load('menu31.png')
bt3=pygame.image.load('s.png')
bt33=pygame.image.load('s2.png')
click=pygame.mixer.Sound('land.wav')
t=True
pygame.mixer.music.play(-1)
def menu():
    ham.blit(bg, (0,0))
    pygame.display.update()
def sound():
    mouse=pygame.mouse.get_pos()
    if 870<mouse[0]<975 and 30<mouse[1]<85:
        ham.blit(bt33,(0,0))
        pygame.display.update()
    else:
        ham.blit(bt3,(0,0))
        pygame.display.update()
def bt():
    mouse=pygame.mouse.get_pos()
    if 200<mouse[0]<350 and 450<mouse[1]<520:
        click.play()
        ham.blit(bt11,(0,0))
        pygame.display.update()
    else:
        ham.blit(bt1,(0,0))
        pygame.display.update()
def btq():
    mouse=pygame.mouse.get_pos()
    if 680<mouse[0]<820 and 485<mouse[1]<545:
        click.play()
        ham.blit(bt22,(0,0))
        pygame.display.update()
    else:
        ham.blit(bt2,(0,0))
        pygame.display.update()
run=True
while run:
    
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            if 870<mx<975 and 30<my<85:
                if t:
                    pygame.mixer.music.pause()
                    t=False
                else:
                    pygame.mixer.music.unpause()
                    t=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            if 200<mx<350 and 450<my<520:
                running()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            if 680<mx<820 and 485<my<545:
                pygame.quit()
            
            
    menu()
    sound()
    bt()
    btq()

pygame.quit()




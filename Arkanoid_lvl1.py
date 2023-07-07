import pygame
pygame.init()

def lel():
    WHITE = (255, 255, 255)
    RED = (225, 0, 50)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 225)
    W = 400
    H = 400
    i = 0
    x = 50
    hp = 2
    score = 0
    sc = pygame.display.set_mode((W, H))
    sc.fill(WHITE)
    pygame.display.update()
    ICHEYKI=('icheyka_3.png', 'icheyka_4.png', 'shar.png', 'Stena_1.png','Stena_2.png')
    ICHEYKI_SURF = []
    for i in range(len(ICHEYKI)):
        ICHEYKI_SURF.append(pygame.image.load(ICHEYKI[i]).convert_alpha())
            
    class Icheyki(pygame.sprite.Sprite):
        def __init__(self, x, y, surf, group):
            pygame.sprite.Sprite.__init__(self)
            self.image = surf
            self.rect = self.image.get_rect(center=(x, y))
            self.add(group)
        def destroy(self):
            self.kill()
    class Hero(pygame.sprite.Sprite):
        def __init__(self,x,surf, group):
            pygame.sprite.Sprite.__init__(self)
            self.image = surf
            self.rect = self.image.get_rect(center=(150, 325))
            self.add(group)
        def update(self, x):
            if self.rect.x <= 300 and x > 0:
                self.rect.x += x
            elif self.rect.x >= 0 and x < 0:
                self.rect.x += x
    class Shar(pygame.sprite.Sprite):
        def __init__(self, x, y, surf, group):
            pygame.sprite.Sprite.__init__(self)
            self.image = surf
            self.rect = self.image.get_rect(center=(x, y))
            self.add(group)
        def update(self, x, y):
            self.rect.x += x
            self.rect.y += y
    class Stena(pygame.sprite.Sprite):
        def __init__(self, x, y, surf, group):
            pygame.sprite.Sprite.__init__(self)
            self.image = surf
            self.rect = self.image.get_rect(center=(x, y))
            self.add(group)

    icheyki = pygame.sprite.Group()
    Hiro = pygame.sprite.Group()
    Sharik = pygame.sprite.Group()
    Stenki = pygame.sprite.Group()
    arr_ih = []
    while i <= 9:
        y = 30
        ich1 = Icheyki(x,y, ICHEYKI_SURF[0], icheyki)
        i += 1
        x += 60
    x = 70
    while i <= 13:
        y = 50
        Ich2 = Icheyki(x,y, ICHEYKI_SURF[0], icheyki)
        i += 1
        x += 70
    x = 50
    while i <= 19:
        y = 70
        ich3 = Icheyki(x,y, ICHEYKI_SURF[0], icheyki)
        i += 1
        x += 60
    x = 70
    while i <= 23:
        y = 90
        ich4 = Icheyki(x,y, ICHEYKI_SURF[0], icheyki)
        i += 1

        x += 70
    x = 50
    while i <= 26:
        y = 110
        ich5 = Icheyki(x,y, ICHEYKI_SURF[0], icheyki)
        i += 1
        x += 135

    hero = Hero(200, ICHEYKI_SURF[1], Hiro)
    Shar_1 = Shar(150, 200, ICHEYKI_SURF[2], Sharik)
    Stena1 = Stena(-5, 200, ICHEYKI_SURF[3], Stenki)
    Stena2 = Stena(405, 200, ICHEYKI_SURF[3], Stenki)
    Stena3 = Stena(200, 0, ICHEYKI_SURF[4], Stenki)
    s_x = 0
    s_y = 2
    f1 = pygame.font.SysFont('None', 18)
    f2 = pygame.font.SysFont('None', 18)
    text1 = f1.render(str(score), 0, (0, 180, 0))
    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
                
            
        if pygame.sprite.spritecollideany(Shar_1, Hiro):
            s_x = ((Shar_1.rect.x + 22) - (hero.rect.x + 50)) * 0.07
            s_y *= -1
        test = pygame.sprite.spritecollideany(Shar_1, icheyki)
        if test:
            s_y *= -1
            test.destroy()
            score += 100
            text1 = f1.render(str(score), 0, (0, 180, 0))
        if pygame.sprite.spritecollideany(Shar_1, Stenki):
            s_x *= -1
        if pygame.sprite.spritecollideany(Stena3, Sharik):
            s_y *= -1
            s_x *= -1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            hero.update(-4)
        if keys[pygame.K_RIGHT]:
            hero.update(4)
        if Shar_1.rect.y > 400:
            hp -= 1
            Shar_1.rect.x = 150
            Shar_1.rect.y = 200
            s_x = 0

        if hp == 2:
            text2 = f2.render("HP:2", 0, (0, 180, 0))
        elif hp == 1:
            text2 = f2.render("HP:1", 0, (0, 180, 0))
        if score == 2300:
            import Arkanoid_lvl2
            exit()
        
        Shar_1.update(s_x, s_y)
        sc.fill(WHITE)
        icheyki.draw(sc)
        Hiro.draw(sc)
        Sharik.draw(sc)
        Stenki.draw(sc)
        sc.blit(text1, (370, 10))
        sc.blit(text2, (300, 10))
        pygame.display.update()
        pygame.time.delay(20)
        if hp < 1:
            text2 = f2.render("HP:0", 0, (0, 180, 0))
            pygame.display.update()
            from Gui_DIED import g_d
            g_d()
        


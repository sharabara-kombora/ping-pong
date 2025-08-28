from pygame import *
font.init()
mixer.init()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), player_size)
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_p(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
class Myachik(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size):
        super().__init__(player_image, player_x, player_y, player_speed, player_size)
        self.speed2 = self.speed
    def go(self):
        self.rect.x += self.speed
        self.rect.y += self.speed2
 


mw = display.set_mode((700, 500))
display.set_caption('пинг-понг')
background = transform.scale(image.load('5559852.png'), (700, 500))



clock = time.Clock()
FPS = 60
font = font.SysFont('Arial', 70)

udar = mixer.Sound('kick.ogg')
udar.set_volume(0.15)

schet_l = 0
schet_p = 0

pr_platforma = Player('Photoroom-Photoroom.png', 650, 200, 5, (20, 150))
l_platforma = Player('Photoroom-Photoroom.png', 50, 200, 5, (20, 150))
myach = Myachik('25474-Photoroom.png', 300, 200, 5, (100, 100))

finish = False

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE and finish == True:
                finish = False
                schet_l = 0
                schet_p = 0
            if e.key == K_SPACE and finish == False:
                if myach.speed == 0:
                    myach.speed = 5
                    myach.speed2 = 5
    mw.blit(background, (0, 0))
    if finish == False:
        schetchik_l = font.render(str(schet_l), True, (255, 215, 0))
        schetchik_p = font.render(str(schet_p), True, (255, 215, 0))
        pr_platforma.reset()
        pr_platforma.update_p()
        l_platforma.reset()
        l_platforma.update_l()
        myach.reset()
        myach.go()
        if sprite.collide_rect(pr_platforma, myach):
            myach.speed = -myach.speed
            udar.play()
        if sprite.collide_rect(l_platforma, myach):
            myach.speed = -myach.speed
            udar.play()
        if myach.rect.y >= 400:
            myach.speed2 = -myach.speed2
        if myach.rect.y <= 0:
            myach.speed2 = -myach.speed2
        if myach.rect.x >= 600:
            schet_l += 1
            myach.rect.x = 300
            myach.rect.y = 200
            myach.speed = 0
            myach.speed2 = 0
        if myach.rect.x <= 0:
            schet_p += 1
            myach.rect.x = 300
            myach.rect.y = 200
            myach.speed = 0
            myach.speed2 = 0
        if schet_l >= 11 and schet_l > schet_p:
            if schet_l - 1 != schet_p:
                win = font.render('ИГРОК СЛЕВА ПОБЕДИЛ!', True, (255, 215, 0))
                finish = True
        if schet_p >= 11 and schet_p > schet_l:
            if schet_p - 1 != schet_l:
                win = font.render('ИГРОК СПРАВА ПОБЕДИЛ!', True, (255, 215, 0))
                finish = True  
        mw.blit(schetchik_l, (60, 10))
        mw.blit(schetchik_p, (640, 10))
    if finish == True:
        mw.blit(win, (10, 200))
    clock.tick(FPS)
    display.update()

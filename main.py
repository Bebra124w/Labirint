from pygame import*
'''Переменные картинок'''
img_back = 'kosmos.png.png'
img_hero = 'amogus.png'
img_bullet = 'patron.png'
img_enemy = 'mini.png'
img_goal = 'minios.png'
'''Music'''
mixer.init()
mixer.music.load('music.ogg')
mixer.music.play()
fire = mixer.Sound("a.ogg")
'''Шрифт'''
font.init()
font = font.SysFont('Times New Roman', 50)
win = font.render('YOU WIN!',True,(255,255,0))
lose = font.render('YOU LOSE:(!',True,(255,255,255))
count = 0

'''Классы'''
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, widht, height, speed):
        #Вызов конструктора класса Sprite
        sprite.Sprite.__init__(self)
        #Все спрайты хранят свойство image
        self.image = transform.scale(image.load(player_image), (widht,height))
        self.speed = speed
        #каждый спрайт хранит свойство rect хитбокс x y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    #метод описания героя в окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()#подключение клавиатуры
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 70:
            self.rect.y += self.speed
            # метод выстрела
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.right, self.rect.centery, 15, 20, 15)
        bullets.add(bullet)
        
class Enemy(GameSprite):
    side = "left"
    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width - 45:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Enemy2(GameSprite):
    side = "left"
    def update(self):
        if self.rect.x <= 200:
            self.side = "right"
        if self.rect.x >= win_width - 150:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    

class Wall(sprite.Sprite):
    def __init__(self, red, green, blue, wall_x, wall_y, widht, height):
        super().__init__()
        self.red = red
        self.green = green
        self.blue = blue
        self.w = widht
        self.h = height
        #в каждом спрайте есть image surface прямоугольная подложка 
        self.image = Surface((self.w, self.h))
        self.image.fill((red,green,blue))
        #каждый спрайт хранит свойство rect хитбокс x y
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#спрайт пули
class Bullet(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width+10:
            self.kill()
           

    
'''Окно Игры'''
win_width = 700
win_height = 500
display.set_caption('Maze')
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load(img_back), (win_width, win_height))
clock = time.Clock()
FPS = 60
'''Персонажи'''
hero = Player(img_hero, 5, win_height - 40,40,50,5)
enemy = Enemy(img_enemy, win_width - 80, 40,65,40,5)
enemy2 = Enemy2(img_enemy, 80, 380,100,40,5)
final = GameSprite(img_goal, win_width - 120, win_height -  80,65,65,0)
'''Стены'''
w1 = Wall(230, 205, 50, 100, 10, 600, 10)
w2 = Wall(230, 205, 50, 100, 480, 100, 10)
w3 = Wall(230, 205, 50, 100, 20, 10, 380)
w4 = Wall(230, 205, 50, 200, 80, 10, 410)
w5 = Wall(230, 205, 50, 200, 80, 100, 10)
w6 = Wall(230, 205, 50, 200, 80, 400, 10)
w7 = Wall(230, 205, 50, 300, 170, 500, 10)
w8 = Wall(230, 205, 50, 300, 170, 10, 100)
'''Группы Спрайтов'''
enemy3 = sprite.Group()
bullets = sprite.Group()
walls = sprite.Group()
''' Добавление спрайтов в группу '''
walls = sprite.Group()
bullets = sprite.Group()
enemygroup = sprite.Group()
walls.add(w1)
walls.add(w2)
walls.add(w3)
walls.add(w4)
walls.add(w5)
walls.add(w6)
walls.add(w7)
walls.add(w8)
enemygroup.add(enemy)
enemygroup.add(enemy2)





'''Игровой цикл игры'''
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()
                fire.play()
                
               
    if finish != True:
        window.blit(back, (0,0))
        hero.reset()
        enemygroup.update()
        enemygroup.draw(window)
        
        bullets.draw(window)
        bullets.update()
        text_count = font.render(str(count), True,(255,255,255))
        window.blit(text_count, (10,10))
        collides = sprite.groupcollide(bullets, enemygroup, True, True)
        sprite.groupcollide(bullets, walls, True, False)

        final.reset()
        hero.update()
        walls.draw(window)
        for c in collides:
            c.kill()
            count = count + 1
        #проигрыш
        if sprite.spritecollide(hero, enemy3, False):
            hero.kill()   
            finish = True
            window.blit(lose, (200,200))
        if sprite.spritecollide(hero, walls, False):
            hero.kill()
            finish = True
            window.blit(lose, (200,200))

        #выигрыш
        if sprite.collide_rect(hero,final):
            finish = True
            window.blit(win, (200,200))

    display.update()
    clock.tick(FPS)






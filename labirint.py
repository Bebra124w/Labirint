from pygame import*
'''Переменные картинок'''
img_back = 'kosmos.png.png'
img_hero = 'amogus.png.png'
img_bullet = 'patron.png'
img_enemy = 'minios.png'
img_goal = 'mini.png'
'''Music'''
#mixer.init()
#mixer.music.load('ASAp.ogg')
#mixer.music.play()
'''Шрифт'''
font.init()
font = font.SysFont('Times New Roman', 50)

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
        keys = key.get_pressed() #подключение клавиатуры
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def fire(self):
        pass
'''Окно Игры'''
win_width = 700
win_height = 500
display.set_caption('Maze')
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load(img_back), (win_width, win_height))
clock = time.Clock()
FPS = 60
'''Персонажи'''
hero = Player(img_hero, 5, win_height - 40,40,40,5)
enemy = GameSprite(img_enemy, win_width - 80, 280,65,65,10)
final = GameSprite(img_goal, win_width - 120, win_height -  80,65,65,0)
'''Игровой цикл игры'''
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(back, (0,0))
        hero.reset()
        enemy.reset()
        final.reset()
        hero.update()
    
    display.update()
    clock.tick(FPS)


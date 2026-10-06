#create a Maze game!
from pygame import *
"Required classes"


#parent class for sprites
class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        #every sprite must have the rect property - the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#heir class for the player sprite (controlled by arrows)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


#heir class for the enemy sprite (moves by itself)
class Enemy1(GameSprite):
    side = "left"
    def update(self):
        if self.rect.x <= 100:
            self.side = "right"
        if self.rect.x >= win_width - 55:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Enemy2(GameSprite):
    side = "down"
    def update(self):
        if self.rect.y <= 80:
            self.side = "up"
        if self.rect.y >= win_height - 65:
            self.side = "down"
        if self.side == "down":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

        
#Game scene
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))


#Game characters
packman = Player('hero.png', 5, win_height - 80, 6)
monster1 = Enemy1('cyborg.png', win_width - 500, 280, 8)
monster2 = Enemy2('cyborg.png', win_width - 100, 100, 10)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)


game = True 
clock = time.Clock()
FPS = 60
finish = False


#music
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:  
        window.blit(background,(0, 0))
        packman.update()
        monster1.update()
        monster2.update()
        final.update()
        packman.reset()
        monster1.reset()
        monster2.reset()
        final.reset()
    

    display.update()
    clock.tick(FPS)
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


#class for obstacle sprites
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        # picture of the wall - a rectangle of the desired size and color
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        # each sprite must store a rect property
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))



#Game scene
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))


#Game characters
player = Player('hero.png', 5, win_height - 80, 6)
monster1 = Enemy1('cyborg.png', win_width - 500, 280, 8)
monster2 = Enemy2('cyborg.png', win_width - 100, 100, 10)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)


w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 200, 200, 10, 350)


game = True 
clock = time.Clock()
FPS = 60
finish = False


font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))


#music
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()


money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    
    if finish != True:  
        window.blit(background,(0, 0))
        player.update()
        monster1.update()
        monster2.update()
        final.update()

        player.reset()
        monster1.reset()
        monster2.reset()
        final.reset()


        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
    

        #"Losing" situation/condition
    if sprite.collide_rect(player, monster1) or sprite.collide_rect(player, monster2) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()


        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200 ,200))
            money.play()


    display.update()
    clock.tick(FPS)

import pygame 

pygame.init()

# pygame.mixer.init()
# pygame.mixer.music.load("Anime_Osts/mirage.mp3")
# pygame.mixer.music.play()
width,height = 1366,768
char_width,char_height = 64,64
x,y = 400,600
background = pygame.transform.scale(pygame.image.load("assets/background.png"),(width,height))
walk_left = [pygame.image.load("Char_Sprite_Left/L1.png"),pygame.image.load("Char_Sprite_Left/L2.png"),pygame.image.load("Char_Sprite_Left/L3.png"),pygame.image.load("Char_Sprite_Left/L4.png"),pygame.image.load("Char_Sprite_Left/L5.png"),pygame.image.load("Char_Sprite_Left/L6.png"),pygame.image.load("Char_Sprite_Left/L7.png"),pygame.image.load("Char_Sprite_Left/L8.png"),pygame.image.load("Char_Sprite_Left/L9.png")]
walk_right = [pygame.image.load("Char_Sprite_Right/R1.png"),pygame.image.load("Char_Sprite_Right/R2.png"),pygame.image.load("Char_Sprite_Right/R3.png"),pygame.image.load("Char_Sprite_Right/R4.png"),pygame.image.load("Char_Sprite_Right/R5.png"),pygame.image.load("Char_Sprite_Right/R6.png"),pygame.image.load("Char_Sprite_Right/R7.png"),pygame.image.load("Char_Sprite_Right/R8.png"),pygame.image.load("Char_Sprite_Right/R9.png")]
standing = pygame.image.load("standing.png")
vel = 10
jumping = False
jumping_height = 20
jumping_gravity = 1
jumping_vel = jumping_height
walkcount = 0
fbs = 27
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((width,height))
class Player():
    def __init__(self,x,y,width,height,vel,jumping_height,jumping_gravity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.walkcount = 0
        self.standing = True
        self.left = False
        self.right = False
        self.jumping = False
        self.jumping_vel = jumping_height
        self.jumping_gravity = jumping_gravity

    def move_left(self):
        self.x -= self.vel
    def move_right(self):
        self.x += self.vel
    def jump(self):
        self.y -= self.jumping_vel * 2
        self.jumping_vel -= self.jumping_gravity 
        if self.jumping_vel < -jumping_height:
            self.jumping = False
            self.jumping_vel = jumping_height
    def drawing(self,win):
        if self.walkcount + 1 >= 27:
            self.walkcount = 0
        if not(self.standing):
            if self.left:
                win.blit(walk_left[self.walkcount//3],(self.x,self.y))
                self.walkcount += 1
            elif self.right:
                win.blit(walk_right[self.walkcount//3],(self.x,self.y))
                self.walkcount += 1
        else:
            if self.left:
                win.blit(walk_left[0],(self.x,self.y))
            else:
                win.blit(walk_right[0],(self.x,self.y))


def draw(player):
    screen.blit(background,(0,0))
    player.drawing(screen)
    pygame.display.update()

def key_movement(keys,player):
    global x,y,jumping,jumping_gravity,jumping_vel,jumping_height,left,right,walkcount
    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.move_left()
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_RIGHT] and player.x < width - player.width - player.vel:
        player.move_right()
        player.left = False
        player.right = True
        player.standing = False
    else:
        player.standing = True
        player.walkcount = 0
    if keys[pygame.K_SPACE]:
        player.jumping = True
        player.left = False
        player.right = False
        player.walkcount = 0
    if player.jumping:
        player.jump()

        
def main():
    run = True
    clock = pygame.time.Clock()
    player = Player(400,600,64,64,10,20,2)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
        keys_pressed = pygame.key.get_pressed()
        clock.tick(fbs)    
        key_movement(keys_pressed,player) 
        draw(player)  
        


main()
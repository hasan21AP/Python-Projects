import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH , HEIGHT = 700,500 #The width and height of the window

window = pygame.display.set_mode((WIDTH , HEIGHT)) #For display window set dimansions of the window 
pygame.display.set_caption("My game") #The title of the window
# pygame.display.set_icon()

BORDER = pygame.Rect(WIDTH//2,0,10,HEIGHT) #Border in the middle of screen to splite spaceships
HEALTH_FONT = pygame.font.SysFont("comicsans",40)
WINNER_FONT = pygame.font.SysFont("comicsans",100)
VEL = 5 #Velcity of spaceships
FPS = 60 #Frame per second 
WHITE = (255,255,255) #Background color of the window
BLACK = (0,0,0) #The color of the border
RED = (255,0,0)
YELLOW = (255,255,0)
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 50,40 #Spaceship dimansions 
BULLET_VEL = 7
MAX_BULLETS = 3
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("As","Grenade+1.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("As","Gun+Silencer.mp3"))


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("As","spaceship_yellow.png"))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("As","spaceship_red.png"))
#Spaceship images

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),-90)
#Rotate the spaceship in the right direction

SPACEBACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("As","space.png")),(WIDTH,HEIGHT))

def window_draw(yellow,red,yellow_bullets,red_bullets,yellow_health,red_health): #Function it's job to Draw the Surfaces in the window
    window.blit(SPACEBACKGROUND_IMAGE,(0,0))
    pygame.draw.rect(window,BLACK,BORDER) #Draw the rectangle that contain the border
    yellow_health_text = HEALTH_FONT.render(f"Health: {yellow_health}", 1, WHITE)
    window.blit(yellow_health_text,(10 ,10))
    red_health_text = HEALTH_FONT.render(f"Health: {red_health}", 1, WHITE)
    window.blit(red_health_text,(WIDTH - red_health_text.get_width() - 10,10))

    window.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y)) 
    window.blit(RED_SPACESHIP,(red.x,red.y))
    #Show the spaceships choose thier coordinates

    for bullet in yellow_bullets:
        pygame.draw.rect(window,YELLOW,bullet)

    for bullet in red_bullets:
        pygame.draw.rect(window,RED,bullet) 

    pygame.display.update() #Update the window


def yellow_movement(key_pressed,yellow): #Function for handle yellow spaceship movement
    if key_pressed[pygame.K_a] and yellow.x >= 10:
        yellow.x -= VEL
    if key_pressed[pygame.K_d] and yellow.x <= (BORDER.x - 50):
        yellow.x += VEL
    if key_pressed[pygame.K_w] and yellow.y > 10:
        yellow.y -= VEL
    if key_pressed[pygame.K_s] and yellow.y < (HEIGHT - 50):
        yellow.y += VEL
    
def red_movement(key_pressed,red): #Function for handle red spaceship movement
    if key_pressed[pygame.K_LEFT] and red.x >= (BORDER.x + 15):  
        red.x -= VEL
    if key_pressed[pygame.K_RIGHT] and red.x <= (WIDTH - 50):
        red.x += VEL
    if key_pressed[pygame.K_UP] and red.y > 10:
        red.y -= VEL
    if key_pressed[pygame.K_DOWN] and red.y < (HEIGHT - 50):
        red.y += VEL

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def check_winner(text):
    draw_text = WINNER_FONT.render(text,1,WHITE)
    window.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2,HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def mainloop(): #Function creates loop to make the window stay on
    yellow = pygame.Rect(50,200,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red = pygame.Rect(600,200,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []
    #objects for our spaceship and choose thier coordinates

    yellow_health = 10
    red_health = 10

    clock = pygame.time.Clock() #Object clock to help track time
    run = True
    while run: #The mainloop for our window
        clock.tick(FPS) #Get the time in milliseconds and this is to update our game in FPS => 60 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #To check if the user press on close window symbol
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
        winner_text = ""        
        if yellow_health <= 0:
            yellow_health = 0
            winner_text = "Red Wins!"
        if red_health  <= 0:
            red_health = 0
            winner_text = "Yellow Wins!"
        if winner_text != "":
            check_winner(winner_text)
            break
        
        key_pressed = pygame.key.get_pressed() #To check if the user press any key 
        
        yellow_movement(key_pressed,yellow)
        red_movement(key_pressed,red)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        #Call the functions to handle spaceships movement
        window_draw(yellow,red,yellow_bullets,red_bullets,yellow_health,red_health) 
    mainloop()


if __name__ == "__main__":
    mainloop()
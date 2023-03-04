import pygame
from random import randint
from os import path

pygame.init()
pygame.font.init()
pygame.mixer.init()

width,height= size = 800,800
fbs = 60
road_w = width//1.6
road_mark_w = width//60
car_player = pygame.image.load("car.png")
car_game = pygame.image.load("otherCar.png")
car_player_loc = car_player.get_rect()
car_game_loc = car_game.get_rect()
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
car_player_loc.center = right_lane,height*0.8
car_game_loc.center = left_lane,height*0.2
vel = 5
counter = 0
level = 0
game_over_text = pygame.font.SysFont("Arial",120)
level_text = pygame.font.SysFont(path.join("fonts","Lcd"),40,True,True)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car game")
pygame.mixer.music.load(path.join("Anime_Osts","Opus-Life-Is-Life.mp3"))
pygame.mixer.music.play()


def screen_draw(level):
    screen.fill((60,220,0))
    pygame.draw.rect(screen,(50,50,50),(width/2-road_w/2,0,road_w,height))
    pygame.draw.rect(screen,(255,240,60),(width/2,0,road_mark_w,height))
    pygame.draw.rect(screen,(255,255,255),(width/2-road_w/2 + road_mark_w*2,0,road_mark_w,height))
    pygame.draw.rect(screen,(255,255,255),(width/2+road_w/2 - road_mark_w*2,0,road_mark_w,height))
    pygame.draw.rect(screen,(230,230,0),(0,0,150,50))
    level_up_text = level_text.render(f"Level:{level}",True,(0,0,0))
    screen.blit(level_up_text,(20,10))
    screen.blit(car_player,car_player_loc)
    screen.blit(car_game,car_game_loc)
    pygame.display.update()


def mainloop():
    global car_player_loc,car_game_loc,car_place,left_lane,right_lane,game_over_text,counter,vel,level
    clock = pygame.time.Clock()
    run = True
    game_over = False
    # shuffle(osts)
    # ost = ost1
    while run:
        counter += 1
        if counter == 400:
            vel += 5
            level += 1
            counter = 0

        clock.tick(fbs)
        car_game_loc[1] += vel
        if car_game_loc[1] > height:
            car_game_loc[1] = height*-0.1
            if randint(0,1) == 0:
                car_game_loc.center = left_lane,height*-0.1
            else:
                car_game_loc.center = right_lane,height*-0.1
        if car_game_loc[0] == car_player_loc[0] and car_game_loc[1] > car_player_loc[1] -250:
            # ost.stop()
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if  event.key in [pygame.K_a,pygame.K_LEFT] and not(car_player_loc[0] <= width - road_w):
                    car_player_loc = car_player_loc.move([-int(road_w/2), 0])
                if  event.key in [pygame.K_d,pygame.K_RIGHT] and not(car_player_loc[0] >= width - road_w):
                    car_player_loc = car_player_loc.move([int(road_w/2), 0]) 
        screen_draw(level)
    game_over = True
    # ost = ost4
    pygame.mixer.music.load(path.join("Anime_Osts","Akon-Lonely.mp3"))
    pygame.mixer.music.play()
    while game_over :
        screen.fill((0,0,0))
        end_game = game_over_text.render("Game Over",True,"red")
        screen.blit(end_game,(100,300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
                pygame.quit()
            


if __name__ == "__main__":
    mainloop()
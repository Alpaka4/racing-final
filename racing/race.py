import pygame
import sys
import random
from  config_3 import *
from  grass import Grass
from  road import Road
from car import Car
from bar import Bar
from health import Health
def bar_spawn(bars,y):
    coord=[145,200,270,325,395,450,520,575]
    random.shuffle(coord)
    for i in range(3):
        b=Bar(screen,coord[i],y)
        bars.append(b)
def life(health,y):
    coor=[800,850,900]
    for i in range(3):
        h = Health(screen,coor[i],y)
        health.append(h)
def show_game_over():
    game_over =f2.render(("GAME OVER"), True,(WHITE))
    screen.blit(game_over, (50,300))
    pygame.display.update()
    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
grass=Grass("grass.jpg",screen,0,0)
grass_2=Grass("grass.jpg",screen,0,-1000)
road=Road("road_3.png",screen,150,0)
road_2=Road("road_3.png",screen,150,-1000)
car=Car("car.png",screen,(SCREEN_WIDTH)//2,(SCREEN_HEIGHT)//2)
bars1=[]
bars2=[]
health=[]
bar_spawn(bars1,0)
bar_spawn(bars2,-SCREEN_HEIGHT//2)
life(health,0)


f2 = pygame.font.SysFont('algerian', 168)
f3 = pygame.font.SysFont('algerian', 50)
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for bar in bars1:
        if car.rect.colliderect(bar):
            car.point+=-3
            health.remove(heart)
            bars1.remove(bar)
    for bar in bars2:
        if car.rect.colliderect(bar):
            car.point+=-3
            health.remove(heart)
            bars2.remove(bar)
    
    
    for bar in bars1:
        bar.update()
        if bar.rect.y>SCREEN_HEIGHT:
            car.point+=2
            road.speedy+=1
            road_2.speedy+=1
            grass.speedy+=1
            grass_2.speedy+=1
            bar.speedy+=1
            bars1.clear()
            bar_spawn(bars1,0)
    for bar in bars2:
        bar.update()
        if bar.rect.y>SCREEN_HEIGHT:
            car.point+=2
            road.speedy+=1
            road_2.speedy+=1
            grass.speedy+=1
            grass_2.speedy+=1
            bar.speedy+=1
            bars2.clear()
            bar_spawn(bars2,0)

        
            
    

    grass.update()
    grass_2.update()
    road.update()
    road_2.update()
    car.update()
    for heart in health:
        heart.update()
    
    screen.fill(BLACK)
    grass.draw()
    grass_2.draw()
    score=f3.render(str(car.point), True,(WHITE))
    screen.blit(score, (800,60))
        

    road.draw()
    road_2.draw()
    car.draw()
    for bar in bars1:
        bar.draw()
    for bar in bars2:
        bar.draw()
    for heart in health:
        heart.draw()
    pygame.display.update()
    
    if len(health)==0:
        show_game_over()
    clock.tick(FPS)

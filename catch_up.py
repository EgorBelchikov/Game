from pygame import *
from random import *


x1 = 100
y1 = 300
x2 = 300
y2 = 300

window = display.set_mode((700, 500))#создание окно игры
window.fill((170, 89, 44))

bg = transform.scale(image.load('background.png'), (700, 500 ))

sp1 = transform.scale(image.load('sprite1.png'), (100, 100 ))
hitbox1 = sp1.get_rect()
hitbox1.x = x1
hitbox1.y = y1

sp2 = transform.scale(image.load('sprite2.png'), (100, 100 ))
hitbox2 = sp2.get_rect()
hitbox2.x = x2
hitbox2.y = y2

width = 10
hight = 10

fps = time.Clock()
run = True
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and hitbox1.x>5:
        hitbox1.x -= 10
    if keys_pressed[K_RIGHT] and hitbox1.x<595:
        hitbox1.x += 10
    if keys_pressed[K_UP] and hitbox1.y>5:
        hitbox1.y -= 10
    if keys_pressed[K_DOWN] and hitbox1.y<395:
        hitbox1.y += 10

    if keys_pressed[K_a] and hitbox2.x>5:
        hitbox2.x -= 10
    if keys_pressed[K_d] and hitbox2.x<595:
        hitbox2.x += 10
    if keys_pressed[K_w] and hitbox2.y>5:
        hitbox2.y -= 10
    if keys_pressed[K_s] and hitbox2.y<395:
        hitbox2.y += 10

    if hitbox1.colliderect(hitbox2):
        width+=10
        hight+=10
        hitbox2.x = randint(10,600)
        hitbox2.y = randint(10,400)
        sp1 = transform.scale(sp1,(width,hight))
        #hitbox1 = sp1.get_rect()#(для себя)
        

    window.blit(bg, (0, 0))
    window.blit(sp1, hitbox1)
    window.blit(sp2, hitbox2)
    
    display.update()
    fps.tick(60)


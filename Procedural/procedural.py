import sys, pygame
import random
import string
pygame.init()

size = width, height = 800, 500
speed = 2
player_size = 100, 100 #226, 226
player_y = 0
player_x = 0

screen = pygame.display.set_mode(size)

player = pygame.image.load("enemy.png")
player = pygame.transform.scale(player, player_size)
player_rect = player.get_rect()
player_rect = player_rect.move( [ width/2-(player_size[0]/2) , height-player_size[1] ] )

keys = [False, False, False, False]
movement = [0, 0]

red = random.randrange(255)
green = random.randrange(255)
blue = random.randrange(255)

seed = "12345678901234567890"

letters = string.printable
seed = ''.join(random.choice(letters) for i in range(20))

# Esperamos un string de 20 de longitud
def generar_mapa(seed, x, y):
    num1 = ord(seed[0]) * ord(seed[1]) * ord(seed[2]) * (x+1)^5 * (y+1)^5
    num2 = ord(seed[3]) * ord(seed[4]) * ord(seed[5]) * (x+1)^5 * (y+1)^5
    num3 = ord(seed[6]) * ord(seed[7]) * ord(seed[8]) * (x+1)^5 * (y+1)^5

    ground_color = ( num1%255 , num2%255 , num3%255 )

    return ground_color

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                keys[0]=True
            if event.key==pygame.K_LEFT:
                keys[1]=True
            if event.key==pygame.K_DOWN:
                keys[2]=True
            if event.key==pygame.K_RIGHT:
                keys[3]=True

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            if event.key==pygame.K_LEFT:
                keys[1]=False
            if event.key==pygame.K_DOWN:
                keys[2]=False
            if event.key==pygame.K_RIGHT:
                keys[3]=False

    #Arriba
    if keys [0]:
        if(player_rect.y == 0):
            pass
        else:
            movement[1] -= speed

    #Izquierda
    if keys [1]:
        if(player_rect.x == 0):
            pass
        else:
            movement[0] -= speed

    #Abajo
    if keys [2]:
        if(player_rect.y == height-player_size[1]):
            pass
        else:
            movement[1] += speed

    #Derecha
    if keys [3]:
        if(player_rect.x == width-player_size[0]):
            pass
        else:
            movement[0] += speed

    player_rect = player_rect.move(movement)

    movement = [0, 0]
    screen.fill( generar_mapa(seed, player_x, player_y) )
    screen.blit(player, player_rect)
    pygame.display.flip()

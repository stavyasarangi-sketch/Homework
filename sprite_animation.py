import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

img_still = pygame.image.load('Images/still.png').convert() 
img_left = pygame.image.load('Images/left_foot.png').convert()
img_right = pygame.image.load('Images/right_foot.png').convert()

img_still.set_colorkey((255, 255, 255))
img_left.set_colorkey((255, 255, 255))
img_right.set_colorkey((255, 255, 255))

current_image = img_still
frame_number = 1
animation_timer = 0

x = 400
y = 300
facing_left = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    is_moving = False

    if keys[pygame.K_LEFT]:
        x = x - 4
        facing_left = True
        is_moving = True
        
    if keys[pygame.K_RIGHT]:
        x = x + 4
        facing_left = False
        is_moving = True
        
    if keys[pygame.K_UP]:
        y = y - 4
        is_moving = True
        
    if keys[pygame.K_DOWN]:
        y = y + 4
        is_moving = True

    if is_moving == True:
        animation_timer = animation_timer + 1
        
        if animation_timer >= 10:
            animation_timer = 0
            if frame_number == 1:
                frame_number = 2
            else:
                frame_number = 1
                
        if frame_number == 1:
            current_image = img_left
        else:
            current_image = img_right
    else:
        animation_timer = 0
        current_image = img_still

    image_to_draw = current_image

    if facing_left == True:
        image_to_draw = pygame.transform.flip(image_to_draw, True, False)

    screen.fill((50, 50, 50))
    screen.blit(image_to_draw, (x, y))
    pygame.display.flip()
    clock.tick(60)

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30)

bg = pygame.image.load('Images/pixel_space.jpg')
bg = pygame.transform.scale(bg, (800, 600))

player = pygame.image.load('Images/spaceship.jpeg')
player = pygame.transform.scale(player, (60, 60))
player.set_colorkey((255, 255, 255))
p_rect = player.get_rect()
p_rect.x = 370
p_rect.y = 520

asteroid = pygame.image.load('Images/asteroid.jpg')
asteroid = pygame.transform.scale(asteroid, (50, 50))
asteroid.set_colorkey((255, 255, 255))

asteroids = []
frames_elapsed = 0
score = 0
asteroid_speed = 5
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if p_rect.left > 0:
            p_rect.x -= 7
            
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if p_rect.right < 800:
            p_rect.x += 7

    if random.randint(1, 30) == 1:
        new_ast = asteroid.get_rect()
        new_ast.x = random.randint(0, 750)
        new_ast.y = -50
        asteroids.append(new_ast)

    frames_elapsed += 1
    if frames_elapsed == 60:
        score += 1
        frames_elapsed = 0

    asteroid_speed = 5 + (score // 10) * 0.5

    asteroids_to_keep = []
    for ast in asteroids:
        ast.y += asteroid_speed
        
        if p_rect.colliderect(ast):
            running = False
            
        if ast.top <= 600:
            asteroids_to_keep.append(ast)
            
    asteroids = asteroids_to_keep

    screen.blit(bg, (0, 0))
    screen.blit(player, p_rect)
    for ast in asteroids:
        screen.blit(asteroid, ast)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

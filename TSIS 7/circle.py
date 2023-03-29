import pygame
pygame.init()
W=800
H=600
x=400
y=300
screen = pygame.display.set_mode((W, H))
pygame.display.update()
clock = pygame.time.Clock()
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True 
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] or pressed[pygame.K_w] and y>=25: y -= 20
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s] and y<=H-25: y += 20
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a] and x>=25: x -= 20
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d ]and x<=W-25: x += 20
        
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, "red", (x, y), 40)
        pygame.display.flip()  
        clock.tick(60)
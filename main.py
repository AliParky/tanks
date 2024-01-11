import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

def draw_walls(screen):
    color = (0, 0, 0)
    thickness = 5

    # Draw lines around the screen edges
    pygame.draw.line(screen, color, (0, 0), (1280, 0), thickness)
    pygame.draw.line(screen, color, (0, 0), (0, 720), thickness)
    pygame.draw.line(screen, color, (0, 720), (1280, 720), thickness)
    pygame.draw.line(screen, color, (1280, 0), (1280, 720), thickness)

class Tank:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

tank = Tank(50, 50, 50)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    tank.update()

    screen.fill("white")

    # Render the graphics here.
    tank.draw(screen)
    draw_walls(screen)
    
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
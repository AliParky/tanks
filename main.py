import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

wall_matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

walls = [
    pygame.Rect(0, 0, 1280, 5),
    pygame.Rect(0, 0, 5, 720),
    pygame.Rect(1275, 0, 5, 720),
    pygame.Rect(640, 360, 5, 360)
]

def draw_walls(screen):
    color = (0, 0, 0)
    for wall in walls:
        pygame.draw.rect(screen, color, wall)

class Tank:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def update(self):
        original_x = self.rect.x
        original_y = self.rect.y

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        for wall in walls:
            if self.rect.colliderect(wall):
                self.rect.x = original_x
                self.rect.y = original_y

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
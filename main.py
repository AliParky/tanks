import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

wall_matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def create_walls_from_matrix(matrix, width, height):
    walls = []
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell == 1:
                wall = pygame.Rect(x * width, y * height, width, height)
                walls.append(wall)
    return walls

wall_width = 80
wall_height = 80
walls = create_walls_from_matrix(wall_matrix, wall_width, wall_height)

def draw_walls(screen):
    color = (0, 0, 0)
    for wall in walls:
        pygame.draw.rect(screen, color, wall)

class Tank:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = 5
        self.barrel_length = size // 2
        self.direction = "UP"

    def get_barrel_rect(self):
        match self.direction:
            case "UP":
                return pygame.Rect(self.rect.centerx - 5, self.rect.y - self.barrel_length, 10, self.barrel_length)
            case "DOWN":
                return pygame.Rect(self.rect.centerx - 5, self.rect.y + self.rect.height, 10, self.barrel_length)
            case "LEFT":
                return pygame.Rect(self.rect.x - self.barrel_length, self.rect.centery - 5, self.barrel_length, 10)
            case "RIGHT":
                return pygame.Rect(self.rect.x + self.rect.width, self.rect.centery - 5, self.barrel_length, 10)
        
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.get_barrel_rect())

    def update(self):
        original_x = self.rect.x
        original_y = self.rect.y

        keys = pygame.key.get_pressed()
        movement_keys_pressed = sum([keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN]])
        if movement_keys_pressed == 1:
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
                self.direction = "LEFT"
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
                self.direction = "RIGHT"
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
                self.direction = "UP"
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed
                self.direction = "DOWN"

        for wall in walls:
            if self.rect.colliderect(wall) or self.get_barrel_rect().colliderect(wall):
                self.rect.x = original_x
                self.rect.y = original_y

class Bullet:
    def __init__(self, x, y, direction, speed=10, size=5):
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed
        self.direction = direction

tank = Tank(100, 100, 50)

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
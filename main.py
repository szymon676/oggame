import pygame

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Load the image for your entity
entity_image = pygame.image.load("siurek.png")

class Entity:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.Vector2(0, 0)
        self.gravity = pygame.Vector2(0, 1)
        self.move_speed = 7
        self.on_ground = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.velocity += self.gravity
        self.rect.move_ip(self.velocity)

        if self.rect.bottom >= screen.get_height():
            self.rect.bottom = screen.get_height()
            self.velocity.y = 0
            self.on_ground = True
        else:
            self.on_ground = False

        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity.x = 0
        elif self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
            self.velocity.x = 0

player = Entity(entity_image, screen.get_width() / 2, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    player.update(dt)
    player.draw(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player.on_ground:
        player.velocity.y = -15
        player.on_ground = False

    player.velocity.x = player.move_speed * (keys[pygame.K_d] - keys[pygame.K_a])

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

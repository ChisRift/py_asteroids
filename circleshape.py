import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, color="white", points=self.triangle(), width=2)

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, other):
        distance_sum = self.radius + other.radius
        return self.position.distance_to(other.position) <= distance_sum

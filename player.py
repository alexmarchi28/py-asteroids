import pygame
from circleshape import *
from constants import *
from shot import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def accelerate(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * PLAYER_ACCELERATION * dt
        if self.velocity.length() > PLAYER_MAX_SPEED:
            self.velocity.scale_to_length(PLAYER_MAX_SPEED)

    def brake(self, dt):
        speed = self.velocity.length()
        if speed == 0:
            return

        new_speed = speed - PLAYER_BRAKE_DECELERATION * dt
        if new_speed <= 0:
            self.velocity.update(0, 0)
        else:
            self.velocity.scale_to_length(new_speed)

    def move(self, dt):
        self.position += self.velocity * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.velocity = shot_velocity
        self.cooldown = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.accelerate(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.brake(dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown <= 0:
                self.shoot()

        self.move(dt)
        self.cooldown -= dt

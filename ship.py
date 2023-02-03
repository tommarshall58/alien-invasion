import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialise the ship and set its starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # load the ship image and get its rect
        # rect is an image's rectangular coordinates
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # initialise the ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        # change to float for more precise control
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        #Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the status of movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect value with new center value
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current position on the screen"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
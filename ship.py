import  pygame
class Ship():

        def __init__(self, ai_settings, screen):
            """Initializes the ship and st its starting position"""
            self.screen =  screen
            #Load the ship image and get its rect>
            self.ai_settings = ai_settings
            self.image = pygame.image.load('images/ship.bmp')
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()

            #start each new ship at the bottom center of th screen
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom
            self.center = float(self.rect.centerx)
            #movement flag
            self.moving_right = False
            self.moving_left = False
        def update(self):
            """update the positionbased on the movemnet flag"""

                #limits the movement of the robot to the edge of the screen
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
            if self.moving_left and self.rect.left>0 :
                self.center -= self.ai_settings.ship_speed_factor
            self.rect.centerx = self.center
        def blitme(self):
            """draw th ship at its curret locatio"""
            self.screen.blit(self.image, self.rect)


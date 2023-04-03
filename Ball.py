import pygame, sys, math

class Ball():
    def __int__(self, image, speed = [0,0], startpos=[0,0]):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx ,self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        
        self.rect =self.rect.move(startpos)
        
        self.didbounceX = False
        self.didbounceY = False
        
    def move(self):
        self.didbounceX = False
        self.didbounceY = False
        self.speed = [self.speedx ,self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def wallcollide (self,size):
        width = size [0]
        height = size [0]
        if not self.didbounceY:
            if self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didbounceY = True
            if self.rect.top < 0:
                self.speedy = -self.speedy
                selfdidbounceY = True
        if not self.didbounceX:
            if self.rect.right > width:
                self.speedx = -self.speedx
                self.didbounceX = True
            if 
                


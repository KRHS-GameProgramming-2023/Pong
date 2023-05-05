import pygame, sys, math

class Ball():
    def __init__(self, speed = [0,0], startpos=[0,0]):
        self.image = pygame.image.load("Ball/ball.png")
        self.rect = self.image.get_rect(center = startpos)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx ,self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        
        
        self.didbounceX = False
        self.didbounceY = False
        
    def move(self):
        self.didbounceX = False
        self.didbounceY = False
        self.speed = [self.speedx ,self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def wallcollide (self,size):
        
        width = size [0]
        height = size [1]
        print(self.rect.bottom)
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
            if self.rect.left < 0:
                self.speedx = -self.speedx
                self.didbounceX = True
            
    def  ballcolide (self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.lift < other.rect.right:
                    if self.rect.top < other.rect.bottom:
                        if self.rect.bottom > other.rect.top:
                            if self.getdist (other) < self.rad + other.rad:
                                if not self.didbounceX:
                                    self.speedx = -self.speedx
                                    self.didbounceX = True
                                if not self.didbouncey:
                                    self.speedy = -self.speedy
                                    self.didbounceY = True
                                return True
        return False
    
    def getdist (self, other):
        x1=self.rect.centerx
        x2=other.rect.centerx
        y1=self.rect.centery
        y2=other.rect.centery
        return math.sqrt ((x2-x1)**2+(y2-y1)**2)


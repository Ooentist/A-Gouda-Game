import pygame
class Object:
    def __init__(self,x,y,tilewid,tilehei,col):
        self. tilewid =tilewid
        self.tilehei  =tilehei
        self.col  =col
        self.y  =y
        self.x  =x
    def draw(self):
        pass
    def update(self):
        pass
class Player(Object):
    def __init__(self,x,y,tilewid,tilehei,col=(255,255,255)):
        super().__init__(x,y,tilewid,tilehei,col)
    def draw(self,surface):
        pygame.draw.rect(surface,self.col,(self.x*self.tilewid,self.y*self.tilehei,self.tilewid,self.tilehei))

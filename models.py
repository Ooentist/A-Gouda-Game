import pygame
class Object:
    def __init__(self,x,y,tilewid,tilehei,col):
        self. tilewid =tilewid
        self.tilehei  =tilehei
        self.col  =col
        self.y  =y
        self.x  =x
    def draw(self,surface):
        pygame.draw.rect(surface,self.col,(self.x*self.tilewid,self.y*self.tilehei,self.tilewid,self.tilehei))
    def update(self):
        pass
class Player(Object):
    def __init__(self,x,y,tilewid,tilehei,col=(255,255,255)):
        super().__init__(x,y,tilewid,tilehei,col)
    def draw(self,surface):
        pygame.draw.rect(surface,self.col,(self.x*self.tilewid,self.y*self.tilehei,self.tilewid,self.tilehei))
    def update(self):
        pass
    def handeinput(self,event,map,num_cols,num_rows):
        moved=False
        newx=self.x
        newy=self.y
        if event.type==pygame.KEYDOWN:
            if event.key in (pygame.K_UP,pygame.K_w):
                newy-=1
            elif event.key in (pygame.K_DOWN,pygame.K_s):
                newy+=1
            elif event.key in (pygame.K_LEFT,pygame.K_a):
                newx-=1
            elif event.key in (pygame.K_RIGHT,pygame.K_d):
                newx+=1
        if newx >=0 and newx<num_cols and newy>=0 and newy<num_rows:
            if  map[newx][newy]==0:
                map[newx][newy]= map[self.x][self.y]
                map[self.x][self.y]=0
                self.x=newx
                self.y=newy
                moved=True
        return moved
    
class Wall(Object):
    def __init__(self,x,y,tilewid,tilehei,col=(0,0,0)):
        super().__init__(x,y,tilewid,tilehei,col)
    def update(self):
        pass
    def draw(self,surface):
        pygame.draw.rect(surface,self.col,(self.x*self.tilewid,self.y*self.tilehei,self.tilewid,self.tilehei))
import pygame,random
from spritesheet import *

Ppath='./assets/3 Dude_Monster'
move_frames=20
class Object:
    def __init__(self,x,y,tilewid,tilehei,col):
        self.xmovestacks=0
        self.ymovestacks=0
        self. tilewid =tilewid
        self.tilehei  =tilehei
        self.col  =col
        self.drawx=x
        self.drawy=y
        self.y  =y
        self.x  =x
    def draw(self,surface):
        pygame.draw.rect(surface,self.col,(self.x*self.tilewid,self.y*self.tilehei,self.tilewid,self.tilehei))
    def update(self):
        if self.xmovestacks!=0:
            if self.xmovestacks>0:
                self.drawx-=1/move_frames
                self.xmovestacks-=1
            else:
                self.drawx+=1/move_frames
                self.xmovestacks+=1
        if self.ymovestacks!=0:
            if self.ymovestacks>0:
                self.drawy-=1/move_frames
                self.ymovestacks-=1
            else:
                self.drawy+=1/move_frames
                self.ymovestacks+=1
class Player(Object):
    def __init__(self,x,y,tilewid,tilehei,col=(255,255,255)):
        super().__init__(x,y,tilewid,tilehei,col)
        scale=(tilewid,tilehei)
        self.animations={'idle':Animation(loadsheet(Ppath+'/Dude_Monster_Idle_4.png',32,32,scale),speed=10),'walk':Animation(loadsheet(Ppath+'/Dude_Monster_Walk_6.png',32,32,scale),speed=8)}
        self.state='idle'
        self.direction='right'    
    def draw(self,surface):
        frame=self.animations[self.state].getframe()
        if self.direction=='left':
            frame=pygame.transform.flip(frame,True,False)
        surface.blit(frame,(self.drawx*self.tilewid,self.drawy*self.tilehei))
    def update(self):
        super().update()
        if abs(self.x-self.drawx)>0.01 or abs(self.y-self.drawy)>0.01:
            if self.state!='walk':
                self.state='walk'
                self.animations[self.state].reset()
        else:
            if self.state!='idle':
                self.state='idle'
                self.animations[self.state].reset()
        self.animations[self.state].update()
    def handeinput(self,event,map,num_cols,num_rows):
        moved=False
        newx=self.x
        newy=self.y
        newoffx=0
        newoffy=0
        if event.type==pygame.KEYDOWN:
            if event.key in (pygame.K_UP,pygame.K_w):
                newy-=1
                newoffy+=1
            elif event.key in (pygame.K_DOWN,pygame.K_s):
                newy+=1
                newoffy-=1
            elif event.key in (pygame.K_LEFT,pygame.K_a):
                newx-=1
                newoffx+=1
                self.direction='left'
            elif event.key in (pygame.K_RIGHT,pygame.K_d):
                newx+=1
                newoffx-=1
                self.direction='right'
            
        if newx >=0 and newx<num_cols and newy>=0 and newy<num_rows:
            if  map[newx][newy]==0:
                map[newx][newy]= map[self.x][self.y]
                map[self.x][self.y]=0
                self.x=newx
                self.y=newy
                self.xmovestacks+=newoffx*move_frames
                self.ymovestacks+=newoffy*move_frames
                moved=True

        return moved
    
class Wall(Object):
    def __init__(self,x,y,tilewid,tilehei,col=(0,0,0)):
        super().__init__(x,y,tilewid,tilehei,col)
    def draw(self,surface):
        pygame.draw.rect(surface,self.col,(self.x*self.tilewid,self.y*self.tilehei,self.tilewid,self.tilehei))
class Enemy(Object):
    def __init__(self,x,y,tilewid,tilehei,col=(255,0,0)):
        super().__init__(x,y,tilewid,tilehei,col)
    def move(self,game_map):
        self.moveran(game_map)
    def draw(self,surface):
        pygame.draw.rect(surface,self.col,(self.drawx*self.tilewid,self.drawy*self.tilehei,self.tilewid,self.tilehei))
    def moveran(self,game_map):
        directions=[(0,-1),(0,1),(-1,0),(1,0)]
        random.shuffle(directions)
        for dx,dy in directions:
            if 0<=self.x+dx<len(game_map) and 0<=self.y+dy<len(game_map[0]):
                if game_map[self.x+dx][self.y+dy]==0:
                    game_map[self.x+dx][self.y+dy]=game_map[self.x][self.y]
                    game_map[self.x][self.y]=0
                    self.x+=dx
                    self.y+=dy
                    self.xmovestacks+=dx*move_frames*-1
                    self.ymovestacks+=dy*move_frames*-1
                    break
                    
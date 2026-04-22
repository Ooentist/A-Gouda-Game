import pygame,random
from models import *
FPS=60
INITX=2
INITY=7
class Game():
    def __init__(self,wid,hei):
        pygame.init()
        self.wid=wid
        self.hei=hei
        self.display=pygame.display.set_mode((wid,hei))
        pygame.display.set_caption('A Gouda Game')
        self.clock=pygame.time.Clock()
        self.running=True
        self.gridcol=20
        self.gridrow=20
        self.tilewid=self.wid/self.gridcol
        self.tilehei=self.hei/self.gridrow
        self.initgamejects()
    def initgamejects(self):
        self.map=[[0 for _ in range(self.gridcol)] for _ in range(self.gridcol)]
        self.player=Player(INITX,INITY,self.tilewid,self.tilehei)
        self.map[INITX][INITY]=self.player
        self.enemies=[]
        self.generatelevel(60,5)
    def generatelevel(self,walls,enemies):
        for col in range(self.gridcol):
            self.map[col][0]=Wall(col,0,self.tilewid,self.tilehei)
            self.map[col][-1]=Wall(col,self.gridrow-1,self.tilewid,self.tilehei)
        for row in range(self.gridrow):
            self.map[0][row]=Wall(0,row,self.tilewid,self.tilehei)
            self.map[-1][row]=Wall(self.gridrow-1,row,self.tilewid,self.tilehei) 
        for _ in range(walls):
            x,y=0,0
            while self.map [x][y]!=0:
                x=random.randint(1, self.gridcol-2)
                y=random.randint(1, self.gridrow-2)
            self.map[x][y]=Wall(x,y,self.tilewid,self.tilehei)
        for _ in range(enemies):
            maxx=self.gridcol-2
            maxy=self.gridrow-2
            x,y=self.findtile(1,3,maxx,maxy)
            self.map[x][y]=Enemy(x,y,self.tilewid,self.tilehei)
            self.enemies.append(self.map[x][y])
    def findtile(self,minx,miny,maxx,maxy):
        x,y=0,0
        while self.map [x][y]!=0:
            x=random.randint(minx, maxx)
            y=random.randint(miny, maxy)
        return x,y
    def game_looop(self):
        while self.running:
            self._handle_inputs()
            self._update()
            self._draw()
    def _draw(self):
        self.display.fill((40,40,40))
        for col in range(self.gridcol):
            for row in range(self.gridrow):
                rect=(col*self.tilewid,row*self.tilehei,self.tilewid,self.tilehei)
                if isinstance(self.map[col][row],Wall):
                    self.map[col][row].draw(self.display)
                if isinstance(self.map[col][row],Enemy):
                    self.map[col][row].draw(self.display)
                pygame.draw.rect(self.display,'black',rect,1)
        self.player.draw(self.display)
        pygame.display.update()
    def _handle_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running =False
            if self.player:
                moved=self.player.handeinput(event,self.map,self.gridcol,self.gridrow)
                if moved:
                    for enemy in self.enemies:
                        enemy.move(self.map)


    def _update(self):
        for enemy in self.enemies:
            enemy.update()
        self.player.update()  
    


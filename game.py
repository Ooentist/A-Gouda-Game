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
        self.pen=False
        self.pend=False
        self.maxlives=3
        self.lives=self.maxlives
        self.game_over=False
        self.font=pygame.font.SysFont(None,36)
        self.loadtile()
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
            holex,holey=self.findtile(1,1,self.gridcol-2,self.gridrow-2)
            self.hole=Hole(holex,holey,self.tilewid,self.tilehei)
        self.bake()
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
            clock=pygame.time.Clock()
            clock.tick(60)
    def _draw(self):
        self.display.blit(self.tileleayer,(0,0))

        self.player.draw(self.display)
        self.hole.draw(self.display)
        for enemy in self.enemies:
            enemy.draw(self.display)
        
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
                        if enemy.x==self.player.x and enemy.y==self.player.y:
                            self.pend=True
                    if self.player.x==self.hole.x and self.player.y==self.hole.y and not self.pend:
                        self.pen=True


    def _update(self):
        if self.game_over:
            return
        self.player.update()
        if self.pend and self. player.state=='idle':
            self.dend=False
            self.player.die()
        if self.pen and self.player.state=='idle':
            self.pen=False
            self.player.fellinhole()
        if self.player.fell:
            self.player.fell=False
            self.nextlevel()
        if not self.player.falling:
            for enemy in self.enemies:
                enemy.update()

    def loadtile(self):
        w,h=int(self.tilewid),int(self.tilehei)
        self.flrtile=pygame.image.load(flrpath).convert()
        self.flrtile=pygame.transform.scale(self.flrtile,(w,h))
        w,h=int(self.tilewid),int(self.tilehei)
        self.waltile=pygame.image.load(wallpath).convert()
        self.waltile=pygame.transform.scale(self.waltile,(w,h))
    def bake(self):
        self.tileleayer=pygame.Surface((self.wid,self.hei))
        for col in range(self.gridcol):
            for row in range(self.gridrow):
                if isinstance(self.map[col][row],Wall):
                    tile=self.waltile
                else:
                    tile=self.flrtile
                self.tileleayer.blit(tile,(col*self.tilewid,row*self.tilehei))
    def nextlevel(self):
            self.pen=False
            self.map=[[0 for _ in range(self.gridrow)]for _ in range(self.gridcol)]
            self.enemies=[]
            self.map[self.player.x][self.player.y]=self.player
            self.generatelevel(60,5)
            print(self.map)
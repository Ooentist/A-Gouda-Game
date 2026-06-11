import pygame,random
from models import *
from utils import *
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
        self.state='game'
        self.maxlives=3
        self.lives=self.maxlives
        self.spawnx=INITX
        self.spawny=INITY
        self.level=1
        self.font=pygame.font.SysFont(None,36)
        self.loadtile()
        self.initgamejects()
        
    def initgamejects(self):
        self.map=[[0 for _ in range(self.gridcol)] for _ in range(self.gridcol)]
        self.player=Player(self.spawnx,self.spawny,self.tilewid,self.tilehei)
        self.map[self.spawnx][self.spawny]=self.player
        self.enemies=[]
        self.generatelevel(60,5+self.level)
    def generatelevel(self,walls,enemies):
        work=False
        while work ==False:
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
            if bfs(self.map,(self.player.x,self.player.y),(self.hole.x,self.hole.y),Wall)==False:
                work=False
            else:
                work=True
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

        
        self.hole.draw(self.display)
        self.player.draw(self.display)
        for enemy in self.enemies:
            enemy.draw(self.display)
        self.drawhud()
        if self.state=='game over':
            self.drawgameover()
        self.drawdark()
        
        pygame.display.update()
    def _handle_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running =False
            if self.state=='game':
                moved=self.player.handeinput(event,self.map,self.gridcol,self.gridrow)
                if moved:
                    for enemy in self.enemies:
                        enemy.move(self.map,self.player.x,self.player.y)
                        if enemy.x==self.player.x and enemy.y==self.player.y:
                            self.state='death'
                            return
                    if self.player.x==self.hole.x and self.player.y==self.hole.y:
                        self.state='fall'


    def _update(self):
        if self.state=='game over':
            return
        self.player.update()

        if self.player.deaddone:
            self.player.deaddone=False
            self.loselife()
            return
        if self.state=='death' and self.player.state=='idle':
            self.player.die()
        if self.player.fell:
            self.player.fell=False
            self.nextlevel()
        if self.state=='fall' and self.player.state=='idle':
            self.player.fellinhole()
        
            

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
            self.resetmap()
            self.enemies=[]
            self.map[self.player.x][self.player.y]=self.player
            self.generatelevel(60,5)
            self.state='game'
            self.level+=1
    def resetmap(self):
        self.map=[[0 for _ in range(self.gridrow)]for _ in range(self.gridcol)]
    def loselife(self):
        self.lives-=1
        if self.lives==0:
            self.state='game over'
        else:
            self.state='game'
            self.respawnplayer()
    def respawnplayer(self):
        self.map[self.player.x][self.player.y]
        self.player.x=self.spawnx
        self.player.y=self.spawny
        self.player.drawx=self.spawnx
        self.player.drawy=self.spawny
        self.player.state='idle'
        self.player.deaddone
        self.player.falling
        self.player.fell
        self.map[self.player.x][self.player.y]=self.player
        for enemy in self.enemies:
            if enemy.x==self.player.x and enemy.y==self.player.y:
                x,y=self.findtile(1,1,self.gridcol-2,self.gridrow-2)
                enemy.x,enemy.y=x,y
                enemy.drawx,enemy.drawy=x,y
                self.map[enemy.x][enemy.y]=enemy
                
    def drawhud(self):
        lives=self.font.render(f'Lives:{self.lives}',True,'white')
        self.display.blit(lives,(10,10))
        level=self.font.render(f'Level:{self.level}',True,'white')
        self.display.blit(level,(10,50))
    def drawgameover(self):
        bg=pygame.Surface((self.wid,self.hei),pygame.SRCALPHA)
        bg.fill((100,0,0,160))
        self.display.blit(bg,(0,0))
        gameovertext=self.font.render('Game Over',True,'white')
        self.display.blit(gameovertext,(self.wid//2-gameovertext.get_width()//2,self.hei//2-gameovertext.get_height()//2))
    def drawdark(self):
        dark=pygame.Surface((self.tilewid,self.tilehei),pygame.SRCALPHA)
        for col in range(self.gridcol):
            for row in range(self.gridrow):
                dark.fill((0,0,0,200))
                for i in range(((row-self.player.x)+ (col-self.player.y))//2):
                    dark.fill((0,0,0,200))
                    self.display.blit(dark,(col*self.tilewid*(col+1),row*self.tilehei*(row+1)))
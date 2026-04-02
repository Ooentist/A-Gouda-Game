import pygame
FPS=60
class Game():
    def __init__(self,wid,hei):
        pygame.init()
        self.wid=wid
        self.hei=hei
        self.display=pygame.display.set_mode((wid,hei))
        pygame.display.set_caption('A Gouda Game')
        self.clock=pygame.time.Clock()
        self.running=True
    def game_looop(self):
        while self.running:
            self._handle_inputs()
            self._update()
            self._draw()
    def _draw(self):
        self.display.fill((40,40,40))
        pygame.display.update()
    def _handle_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running =False
    def _update(self):
        pass

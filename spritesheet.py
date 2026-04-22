import pygame
def loadsheet(path,fwid,fhei,scaleto=None):
    sheet = pygame.image.load(path).convert_alpha()
    sheet_w,sheet_h =sheet.get_size()
    for y in range (0,sheet_h,fhei):
        for x in range(0,sheet_w,fwid):
            frame=sheet.subsurface(pygame.Rect(x,y,fwid,fhei))
            frames=[]
            if scaleto:
                frame=pygame.transform.scale(frame,(int(scaleto[0]),int(scaleto[1])))
            frames.append(frame)
    return frames
class Animation:
    def __init__(self,frames,speed):
        self.frames=frames
        self.speed=speed
        self.curframe=0
        self.timer=0
    def update(self):
        self.timer+=1
        if self.timer>self.speed:
            self.timer=0
            self.curframe=(self.curframe+1)%len(self.frames)

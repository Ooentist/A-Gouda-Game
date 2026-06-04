
def bfs(map,start,end,wallclass):
    queue=[start]
    visited=[[None for _ in range(len(map[0]))] for  _ in range(len(map))]
    visited[start[0]][start[1]]= 'start'
    ende=False
    while len(queue)>0:
        
        x,y=queue.pop(0)
        if visited[x+1][y]==None and not isinstance(map[x+1][y],wallclass):
            visited[x+1][y]=(1,0)
            if x+1==end[0] and y==end[1]:
                ende=True
                
            queue.append((x+1,y))
        if visited[x-1][y]==None and not isinstance(map[x-1][y],wallclass):
            visited[x-1][y]=(-1,0)
            if x-1==end[0] and y==end[1]:
                print('hi')
                ende=True
            queue.append((x-1,y))
        if visited[x][y+1]==None and not isinstance(map[x][y+1],wallclass):
            visited[x][y+1]=(0,1)
            if x==end[0] and y+1==end[1]:
                print('hi')
                ende=True
            queue.append((x,y+1))
        if visited[x][y-1]==None and not isinstance(map[x][y-1],wallclass):
            visited[x][y-1]=(0,-1)
            if x==end[0] and y-1==end[1]:
                print('hi')
                ende=True
            queue.append((x,y-1))
        if ende==True:
            curx,cury=end[0],end[1]
            curdx,curdy=(0,0)
            while visited[curx][cury]!='start':
                curdx,curdy=visited[curx][cury]
                curx-= curdx
                cury-= curdy
            return curdx,curdy
    return False
        #print(queue)
    #print(visited)
        
        

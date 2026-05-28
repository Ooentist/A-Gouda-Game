from models import Wall
def bfs(map,start,end,numrows,numcols):
    queue=[start]
    visited=[[None for _ in range(len(map[0]))] for  _ in range(len(map))]
    visited[start[0]][start[1]]= (start[0],start[1])
    while len(queue)>0:
        x,y=queue.pop(0)
        if visited[x+1][y]==None and not isinstance(map[x+1][y],Wall):
            visited[x+1][y]=(1,0)
            if visited[x+1][y]==end:
                print('hi')
                return
            queue.append((x+1,y))
        if visited[x-1][y]==None and not isinstance(map[x-1][y],Wall):
            visited[x-1][y]=(-1,0)
            if visited[x-1][y]==end:
                print('hi')
                return
            queue.append((x-1,y))
        if visited[x][y+1]==None and not isinstance(map[x][y+1],Wall):
            visited[x][y+1]=(0,1)
            if visited[x][y+1]==end:
                print('hi')
                return
            queue.append((x,y+1))
        if visited[x][y-1]==None and not isinstance(map[x][y-1],Wall):
            visited[x][y-1]=(0,-1)
            if visited[x][y-1]==end:
                print('hi')
                return
            queue.append((x,y-1))
        print(queue)
    print(visited)
        
        

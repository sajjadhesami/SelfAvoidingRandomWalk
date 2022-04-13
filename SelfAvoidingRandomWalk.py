import sys,random,stddraw,color


def drawMap(n):
    stddraw.setXscale(0,n)
    stddraw.setYscale(0,n)

    for i in range(0,n):
            stddraw.line(i,0,i,n)
            stddraw.line(0,i,n,i)
if __name__=="__main__":
    n=int(sys.argv[1])
    lattice=[[False]*n]*n
    drawMap(n)
    stddraw.setPenColor(color.RED)

    x=n/2
    y=n/2
    lattice[x][y]=True
    stddraw.filledCircle(x,y,0.5)

    while(x-1>0 and x+1<n and y-1>0 and y+1<n and (lattice[x-1][y]!=False or lattice[x+1][y]!=False or lattice[x][y-1]!=False or lattice[x][y+1])):


        stddraw.show(100)


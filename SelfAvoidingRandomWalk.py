import sys, random, stddraw, color
import tkinter

def drawMap(n):
    '''
    This function receives the size of the map and draws a grid on the canvas
    :param n: size of the map
    :return: NoneType (internally draws the canvas)
    '''
    stddraw.clear(color.WHITE)
    stddraw.setPenColor(color.BLACK)
    stddraw.setXscale(0, n)
    stddraw.setYscale(0, n)

    for i in range(0, n):
        stddraw.line(i, 0, i, n)
        stddraw.line(0, i, n, i)


def drawCircle(x, y, lattice,path):
    '''
    Moves the red circle from its previous place to the new place
    :param x: new X of the circle
    :param y: new Y of the circle
    :param lattice: lattice
    :param path: path variable
    :return: NoneType
    '''
    N=len(lattice)
    drawMap(N)


    stddraw.setPenColor(color.BLACK)
    stddraw.setPenRadius(0.05)

    for i in range(0,len(path)-1):
        stddraw.line(path[i][0],N-path[i][1],path[i+1][0],N-path[i+1][1])


    stddraw.setPenRadius()
    stddraw.setPenColor(color.RED)
    stddraw.filledCircle(x, N-y, 0.25)

def main():
    if (len(sys.argv) != 4):
        print("please run the script with three arguments: SlefAvoidingRandomWalk.py 10 100 1")
        return
    N = int(sys.argv[1])
    T = int(sys.argv[2])
    SHOW = bool(int(sys.argv[3]))

    escape_counter = 0
    deadend_counter = 0

    for t in range(0, T):
        lattice = [[False] * N for i in range(N)]
        x = N // 2
        y = N // 2
        lattice[x][y] = True

        if(SHOW==True):
            path=[(x,y)]
            drawCircle(x,y,lattice,path)
            stddraw.show(200)

        while True:

            print("move from (%-10d,%-10d)" %(x,y),end=" ")
            while (True):
                r = random.randrange(0, 4)
                if r == 0:
                    if (lattice[x + 1][y]):
                        continue
                    x += 1
                    break
                elif r == 1:
                    if (lattice[x - 1][y]):
                        continue
                    x -= 1
                    break
                elif r == 2:
                    if (lattice[x][y + 1]):
                        continue
                    y += 1
                    break
                else:
                    if (lattice[x][y - 1]):
                        continue
                    y -= 1
                    break
            print("(%-10d,%-10d)" %(x,y))
            lattice[x][y] = True
            if(SHOW==True):
                path.append((x,y))
                drawCircle(x,y,lattice,path)
                stddraw.show(200)
            if (x - 1 < 0 or x + 1 >= N or y - 1 < 0 or y + 1 >= N):
                escape_counter += 1
                break
            if (lattice[x - 1][y] == True and lattice[x + 1][y] == True and lattice[x][y - 1] == True and lattice[x][
                y + 1] == True):
                deadend_counter += 1
                break

        print("Experiment #%-10d has just finished: #escape: %-10d #deadend: %-10d" % (
        t+1, escape_counter, deadend_counter))



if __name__ == "__main__":
    main()

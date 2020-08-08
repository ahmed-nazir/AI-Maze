from PIL import Image, ImageDraw
import sys

im = Image.new('RGB', (1000, 1000), (255, 255, 255))
draw = ImageDraw.Draw(im)
maze = [[0,0,0,0,0,0,8,0,0,0],[0,1,1,1,1,1,1,0,1,0],[0,1,0,0,0,0,0,0,1,0],[0,1,0,1,1,1,1,1,1,0],[0,1,0,1,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,1,0,0,0],[0,1,0,1,1,1,1,1,1,0],[0,1,0,0,1,0,1,0,1,0],[0,0,0,0,9,0,0,0,0,0]]
for i in range(10):
    for j in range(10):
        if maze[i][j] == 0:
            draw.rectangle((0+(j*100),0+(i*100),100+(j*100),100+(i*100)), fill=(0,0,0), outline=(0,0,0))
        elif maze[i][j] == 1:
            draw.rectangle((0+(j*100),0+(i*100),100+(j*100),100+(i*100)), fill=(255,255,255), outline=(0,0,0))
        elif maze[i][j] == 8:
            draw.rectangle((0+(j*100),0+(i*100),100+(j*100),100+(i*100)), fill=(34,255,0), outline=(34,255,0))
            startY = i
            startX = j
            sY = i
            sX = j
        elif maze[i][j] == 9:
            draw.rectangle((0+(j*100),0+(i*100),100+(j*100),100+(i*100)), fill=(255,0,0), outline=(255,0,0))
            endi = i
            endj = j
im.save('Documents/Before.jpg', quality=100)
traversed = [(startY,startX)]
node = []
completenode = []
path = [(startY,startX)]
def moveLeft():
    if startX>0:
        if (maze[startY][startX-1] != 0) and ((startY,startX-1) not in traversed):
            return True
        else:
            return False
def moveRight():
    if startX<10:
        if (maze[startY][startX+1] != 0) and ((startY,startX+1) not in traversed):
            return True
        else:
            return False
def moveUp():
    if startY>0:
        if (maze[startY-1][startX] != 0) and ((startY-1,startX) not in traversed):
            return True
        else:
            return False
def moveDown():
    if startY<10:
        if (maze[startY+1][startX] != 0) and ((startY+1,startX) not in traversed):
            return True
        else:
            return False

for q in range(50):
    if startY == endi and startX == endj:
        print("Finished")
        draw.rectangle((0+(startX*100),0+(startY*100),100+(startX*100),100+(startY*100)), fill=(255,0,0), outline=(255,0,0))
        break

    if (not(moveDown() or moveLeft() or moveRight() or moveUp())):
        a = path.index(node[-1])
        b = path.index((startY,startX))
        del path[a+1:b+1]
        startX = node[-1][1]
        startY = node[-1][0]
        node.pop()
        
    if (moveDown() and (moveLeft() or moveRight() or moveUp())) or (moveUp() and (moveLeft() or moveRight())) or(moveLeft() and moveRight()) :
        node.append((startY,startX))
        completenode.append((startY,startX))

    if moveDown():
        startY = startY+1
        traversed.append((startY,startX))
        path.append((startY,startX))
    
    elif moveLeft():
        startX = startX-1
        traversed.append((startY,startX))
        path.append((startY,startX))
    
    elif moveUp():
        startY = startY-1
        traversed.append((startY,startX))
        path.append((startY,startX))
    
    elif moveRight():
        startX = startX+1
        traversed.append((startY,startX))
        path.append((startY,startX))

def PATH():
    for i in path:
        draw.rectangle((0+(i[1]*100),0+(i[0]*100),100+(i[1]*100),100+(i[0]*100)), fill=(66,75,200), outline=(0,0,0))
    draw.rectangle((0+(endj*100),0+(endi*100),100+(endj*100),100+(endi*100)), fill=(255,0,0), outline=(255,0,0))
    draw.rectangle((0+(sX*100),0+(sY*100),100+(sX*100),100+(sY*100)), fill=(34,255,0), outline=(34,255,0))

def TRAVERSED():
    for i in traversed:
        draw.rectangle((0+(i[1]*100),0+(i[0]*100),100+(i[1]*100),100+(i[0]*100)), fill=(247,250,185), outline=(0,0,0))
    draw.rectangle((0+(endj*100),0+(endi*100),100+(endj*100),100+(endi*100)), fill=(255,0,0), outline=(255,0,0))
    draw.rectangle((0+(sX*100),0+(sY*100),100+(sX*100),100+(sY*100)), fill=(34,255,0), outline=(34,255,0))

TRAVERSED()
PATH()

im.save('Documents/Finished.jpg', quality=100)

from PIL import Image, ImageDraw
import sys

im = Image.new('RGB', (1000, 1000), (255, 255, 255))
draw = ImageDraw.Draw(im)
size = 50
unsolved = True
maze = [[0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0],
        [0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,9],
        [0,1,0,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,1,0],
        [0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0],
        [0,1,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,1,1,0],
        [0,1,0,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0],
        [0,1,0,0,1,0,1,0,1,0,0,0,0,0,1,1,1,0,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0],
        [0,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,0,1,0],
        [0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0],
        [0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1,1,0],
        [0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0],
        [0,1,0,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

for i in range(20):
    for j in range(20):
        if maze[i][j] == 0:
            draw.rectangle((0+(j*size),0+(i*size),size+(j*size),size+(i*size)), fill=(0,0,0), outline=(0,0,0))
        elif maze[i][j] == 1:
            draw.rectangle((0+(j*size),0+(i*size),size+(j*size),size+(i*size)), fill=(255,255,255), outline=(0,0,0))
        elif maze[i][j] == 8:
            draw.rectangle((0+(j*size),0+(i*size),size+(j*size),size+(i*size)), fill=(34,255,0), outline=(0,0,0))
            startY = i
            startX = j
            sY = i
            sX = j
        elif maze[i][j] == 9:
            draw.rectangle((0+(j*size),0+(i*size),size+(j*size),size+(i*size)), fill=(255,0,0), outline=(0,0,0))
            endi = i
            endj = j
im.save('Before.jpg', quality=100)

traversed = [(startY,startX)]
node = []
path = [(startY,startX)]
def moveLeft():
    if startX>0:
        if (maze[startY][startX-1] != 0) and ((startY,startX-1) not in traversed):
            return True
        else:
            return False
def moveRight():
    if startX<20:
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
    if startY<20:
        if (maze[startY+1][startX] != 0) and ((startY+1,startX) not in traversed):
            return True
        else:
            return False

while unsolved:
    if startY == endi and startX == endj:
        print("Finished")
        draw.rectangle((0+(startX*size),0+(startY*size),size+(startX*size),size+(startY*size)), fill=(255,0,0), outline=(0,0,0))
        unsolved = False
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
        draw.rectangle((0+(i[1]*size),0+(i[0]*size),size+(i[1]*size),size+(i[0]*size)), fill=(66,75,200), outline=(0,0,0))
    draw.rectangle((0+(endj*size),0+(endi*size),size+(endj*size),size+(endi*size)), fill=(255,0,0), outline=(0,0,0))
    draw.rectangle((0+(sX*size),0+(sY*size),size+(sX*size),size+(sY*size)), fill=(34,255,0), outline=(0,0,0))

def TRAVERSED():
    for i in traversed:
        draw.rectangle((0+(i[1]*size),0+(i[0]*size),size+(i[1]*size),size+(i[0]*size)), fill=(247,250,185), outline=(0,0,0))
    draw.rectangle((0+(endj*size),0+(endi*size),size+(endj*size),size+(endi*size)), fill=(255,0,0), outline=(0,0,0))
    draw.rectangle((0+(sX*size),0+(sY*size),size+(sX*size),size+(sY*size)), fill=(34,255,0), outline=(0,0,0))

#TRAVERSED()
PATH()

im.save('Finished.jpg', quality=100)

import pygame as pg
import time
import random

Width = 391
Height = 391
count = 0
CS = 23
TC = 17
PX = 2
PY = 2
SL = 3
Snake = []
X_Dir = 0
Y_Dir = 0
Score = 0
Score2 = 1
RGB = (255, 0, 0)
Yellow = (0, 0, 255)
White = (255, 255, 255)
Black = (0, 0, 0)

pg.init()
pg.display.set_caption("파이게임")
pg.key.set_repeat(1, 5)
Screen = pg.display.set_mode((Width, Height))

pos = 0

def Draw_Board():
    Screen.fill(Black)
    for n in range(17):
        pg.draw.line(Screen, Yellow, [0, 391 - 23 * n], [391, 391 - 23 * n], 1)
        pg.draw.line(Screen, Yellow, [391 - 23 * n, 0], [391 - 23 * n, 391], 1)
def check_duplicates(lst):
    head = lst[0]
    body = lst[1:]
    print(f"head:{head}, body:{body}") 
    for b in body:
        # head와 body (x,y) 비교 
        if b == head:
            print("warn")
def Draw_Snake():    
    for idx, s in enumerate(Snake):
        if idx == 0:
            pg.draw.rect(Screen,(255,255,255),(s[0]*CS, s[1]*CS,CS,CS),)
        else:
            pg.draw.rect(Screen,(0,255,0),(s[0]*CS, s[1]*CS,CS,CS),)
def Move_Snake():
    global PX, PY, Score, SL, Snake
    PX += X_Dir
    PY += Y_Dir
    Snake.insert(0, (PX, PY))
    while( len(Snake)>SL):
        Snake.pop()
def Draw_apple(A):
    global Ax, Ay, Score2
    if A==0:
        Ax = 391 - random.randint(1, 15) * 23 + 12
        Ay = 391 - random.randint(1, 15) * 23 + 12
        Score2 = Score2+1
    if A==1:
        Ax = 334
        Ay = 334
        pg.draw.circle(Screen, RGB, [Ax, Ay], 11.5)
    if A==2:
        pg.draw.circle(Screen, RGB, [Ax, Ay], 11.5)
Running = True
Move_Snake()
while Running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                Running = False
            elif event.key == pg.K_UP and not Y_Dir == 1:
                X_Dir = 0
                Y_Dir = -1
            elif event.key == pg.K_DOWN and not Y_Dir == -1:
                X_Dir = 0
                Y_Dir = 1
            elif event.key == pg.K_LEFT and not X_Dir == 1:
                X_Dir = -1
                Y_Dir = 0
            elif event.key == pg.K_RIGHT and not X_Dir == -1:
                X_Dir = 1
                Y_Dir = 0
    count = count+1
    if count == 15:
        Draw_Board()
        Draw_Snake()
        Move_Snake()
        count = 0
    if Score == 0:
        Draw_apple(1)
        if Score == 0 and Ax == PX*23+12 and Ay == PY*23+12:    
            Score = Score+1
            print(Score)
    if Score == Score2:
        Draw_apple(0)
        print("working")
    if Score == Score2-1:
        Draw_apple(2)
        if Ax == PX*23+12 and Ay == PY*23+12:
            Draw_apple(0)
            Score=Score+1
            SL += 1
            print(Ax,Ay)
            print(Score)
            Snake.insert(0,(PX,PY))
            print(Snake)

    check_duplicates(Snake)
    pg.display.update()
    time.sleep(0.01)

pg.quit()
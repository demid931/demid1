import tkinter
import tkinter as tk
import random
from tkinter import PhotoImage
def prepare_and_start():
    global player
def move_by_keys(event):
    info_coords = canvas.coords(player)
    x = info_coords[0]
    y = info_coords[1]
    label.config(text=str(x)+ ' '+ str(y))
    if event.keysym == 'Up':
        canvas.move(player,0,-20)
    elif event.keysym == 'Down':
        canvas.move(player,0,20)
    elif event.keysym == 'Left':
        canvas.move(player,-20,0)
    elif event.keysym == 'Right':
        canvas.move(player,20, 0)


def move_wrap(obj, move_x, move_y):
    xy = canvas.coords(obj)
    canvas.move(obj, move_x, move_y)
    print(xy)
    if xy[0] <= 0:
        canvas.move(obj, WIDTH, 0)
    if xy[0] >= WIDTH:
        canvas.move(obj, -WIDTH, 0)
    if xy[1] <= 0:
        canvas.move(obj, 0, HEIGHT)
    if xy[1] >= HEIGHT:
        canvas.move(obj, 0, -HEIGHT)
step=10
win = tk.Tk()
canvas = tk.Canvas(win, bg='#fff', width=700, height=700)
label = tk.Label(win, text='Глеб')
player_pos = (200,200)
player_pic = tk.PhotoImage(file=r"Демид бомбит украину.png")

player = canvas.create_image((player_pos[0], player_pos[1]), image=player_pic, anchor='nw')
label.config(text="Найди выход!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
win.bind("<KeyPress>", move_by_keys)
canvas.pack()
win.mainloop()
master = tkinter.Tk()

step = 32
N_X = 10
N_Y = 10
WIDTH = step * N_X
HEIGHT = step * N_Y
a = False
player_pic = tkinter.PhotoImage(file="Демид бомбит украину.png")

canvas = tkinter.Canvas(master, bg= '#FCAB08',
                        width= WIDTH, height=HEIGHT)

player_pos = (random.randint(0, N_X - 1) * step,
              random.randint(0, N_Y - 1) * step)
print(player_pos)
label = tkinter.Label(master, text="не попадись!")
restart = tkinter.Button(master, text="начать заново",
                         command=prepare_and_start)
restart.pack()
label.pack()

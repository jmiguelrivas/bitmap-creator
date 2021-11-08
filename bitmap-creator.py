#!/usr/bin/python3
import tkinter as tk

current_color = 0
grid_size = 16
buttons = [[0 for x in range(grid_size)] for y in range(grid_size)]
colors = [
  "#000000",
  "#01007f",
  "#008008",
  "#008083",
  "#7e0003",
  "#7d037c",
  "#7f8100",
  "#c0c0c2",
  "#808080",
  "#0001fc",
  "#01fe05",
  "#00fffd",
  "#fb0200",
  "#fb01ff",
  "#fffe01",
  "#fefff1",
]

win = tk.Tk()
win.title("Bitmap Creator - " + str(current_color))

def change_color_btn(x,y):
  win.title("Bitmap Creator - " + str(x) + str(y))
  # buttons[x][y].config(text=current_color)

def change_color(color):
  current_color = color
  win.title("Bitmap Creator - " + str(color))

for x in range(grid_size):
  for y in range(grid_size):
    buttons[x][y] = tk.Button(text=str(current_color), width=2, height=2, bg=colors[current_color], command=change_color_btn(x,y))
    buttons[x][y].grid(column=x, row=y)

color_btn = [0 for x in range(grid_size)]
for index in range(grid_size):
  color_btn[index] = tk.Button(text=index, width=2, height=2, bg=colors[index], command=change_color(index))
  color_btn[index].grid(column=index, row=grid_size)


win.mainloop()
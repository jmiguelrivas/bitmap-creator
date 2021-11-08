#!/usr/bin/python3
import tkinter as tk

current_color = 15
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
win.resizable(False, False)

def change_color_btn(x,y):
  buttons[x][y].config(
    text=str(current_color),
    bg=colors[current_color]
  )

def change_color(color):
  global current_color
  win.title("Bitmap Creator - " + str(color))
  current_color = int(color)

for x in range(grid_size):
  for y in range(grid_size):
    buttons[x][y] = tk.Button(
      text=str(0),
      width=2,
      height=2,
      bg=colors[0],
      command=lambda x=x, y=y: change_color_btn(x,y)
    )
    buttons[x][y].grid(column=x, row=y)

color_btn = [0 for x in range(grid_size)]
for index in range(grid_size):
  color_btn[index] = tk.Button(
    text=index,
    width=2,
    height=2,
    bg=colors[index],
    command=lambda index=index: change_color(index)
  )
  color_btn[index].grid(column=index, row=grid_size)

win.mainloop()
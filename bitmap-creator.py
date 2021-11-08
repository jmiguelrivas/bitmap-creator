#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

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
colors_name = [
  "Black",
  "Blue",
  "Green",
  "Cyan",
  "Red",
  "Magenta",
  "Brown",
  "Light Grey",
  "Dark Grey",
  "Light Blue",
  "Light Green",
  "Light Cyan",
  "Light Red",
  "Light Magenta",
  "Yellow",
  "White",
]

def set_window_title(color):
  win.title("Bitmap Creator - " + colors_name[color] + "(" + str(color) + ")")

def close_window():
  win.destroy()

def clear_values():
  global current_color
  current_color = 15
  set_window_title(current_color)
  for x in range(grid_size):
    for y in range(grid_size):
      buttons[x][y].config(
        text=str(0),
        bg=colors[0]
      )

def save_cpp_file():
  messagebox.showinfo("Bitmap Created", "file created at: " + dir_path + "/bitmap.cpp")

def save_pascal_file():
  messagebox.showinfo("Bitmap Created", "file created at: " + dir_path + "/bitmap.pas")

def change_color_btn(x,y):
  buttons[x][y].config(
    text=str(current_color),
    bg=colors[current_color]
  )

def change_color(color):
  global current_color
  set_window_title(color)
  current_color = int(color)

# defining window
win = tk.Tk()
set_window_title(current_color)
win.resizable(False, False)

# creating menu bar
menu1 = tk.Menu()
win.config(menu=menu1)

# creating options for the menu bar
file_menu = tk.Menu(menu1, tearoff=0)
save_menu = tk.Menu(menu1, tearoff=0)
edit_menu = tk.Menu(menu1, tearoff=0)
colors_menu = tk.Menu(menu1, tearoff=0)
help_menu = tk.Menu(menu1, tearoff=0)

# adding options to the menu bar
menu1.add_cascade(label="File", menu=file_menu)
menu1.add_cascade(label="Options", menu=edit_menu)
menu1.add_cascade(label="Help", menu=help_menu)

file_menu.add_command(label="New File", command=clear_values)
file_menu.add_cascade(label="Save As", menu=save_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=close_window)

edit_menu.add_cascade(label="Set Color", menu=colors_menu)

help_menu.add_command(label="About", command=close_window)

save_menu.add_command(label="C++", command=save_cpp_file)
save_menu.add_command(label="Pascal", command=save_pascal_file)

for index in range(len(colors)):
  colors_menu.add_command(label=colors_name[index], command=lambda index=index: change_color(index))

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
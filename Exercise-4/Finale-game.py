from turtle import *
from random import choice
from freegames import floor, vector
from subprocess import call
import os
import webbrowser 
from tkinter import *
import tkinter as tk

root=tk.Tk()

def openwindow():
    button3 = tk.Button(root, fg="magenta", relief=RAISED, text="Take me to pacman", command=pacman)
    button3.pack( side=LEFT)

    button4 = tk.Button(root, fg="green", relief=RAISED, text="Show me your work - assignment 3 was on HTML and CSS", command=assignment)
    button4.pack( side=RIGHT)

    button5 = tk.Button(root, fg="blue", relief=RAISED, text="Take a Screenshot", command=screenshot)
    button5.pack()

    button2.pack_forget()
    button1.pack_forget()


def assignment():
    
    webbrowser.open_new_tab('https://arkakjsce.github.io/MyPortfolioDraft/')


def pacman():

  state = {'score': 0}
  path = Turtle(visible=False)
  writer = Turtle(visible=False)
  aim = vector(5, 0)
  pacman = vector(-40, -80)
  ghosts = [
      [vector(-180, 160), vector(5, 0)],
      [vector(-180, -160), vector(0, 5)],
      [vector(100, 160), vector(0, -5)],
      [vector(100, -160), vector(-5, 0)],
  ]
  tiles = [
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
      0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
      0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
      0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
      0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
      0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
      0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
      0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
      0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
      0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
      0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
      0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
      0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
      0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
      0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
      0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
      0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  ]


  def square(x, y):
      "Draw square using path at (x, y)."
      path.up()
      path.goto(x, y)
      path.down()
      path.begin_fill()

      for count in range(4):
          path.forward(20)
          path.left(90)

      path.end_fill()


  def offset(point):
      "Return offset of point in tiles."
      x = (floor(point.x, 20) + 200) / 20
      y = (180 - floor(point.y, 20)) / 20
      index = int(x + y * 20)
      return index


  def valid(point):
      "Return True if point is valid in tiles."
      index = offset(point)

      if tiles[index] == 0:
          return False

      index = offset(point + 19)

      if tiles[index] == 0:
          return False

      return point.x % 20 == 0 or point.y % 20 == 0


  def world():
      "Draw world using path."
      bgcolor('black')
      path.color('blue')

      for index in range(len(tiles)):
          tile = tiles[index]

          if tile > 0:
              x = (index % 20) * 20 - 200
              y = 180 - (index // 20) * 20
              square(x, y)

              if tile == 1:
                  path.up()
                  path.goto(x + 10, y + 10)
                  path.dot(2, 'white')


  def move():
      "Move pacman and all ghosts."
      writer.undo()
      writer.write(state['score'])

      clear()

      if valid(pacman + aim):
          pacman.move(aim)

      index = offset(pacman)

      if tiles[index] == 1:
          tiles[index] = 2
          state['score'] += 1
          x = (index % 20) * 20 - 200
          y = 180 - (index // 20) * 20
          square(x, y)

      up()
      goto(pacman.x + 10, pacman.y + 10)
      dot(20, 'yellow')

      for point, course in ghosts:
          if valid(point + course):
              point.move(course)
          else:
              options = [
                  vector(5, 0),
                  vector(-5, 0),
                  vector(0, 5),
                  vector(0, -5),
              ]
              plan = choice(options)
              course.x = plan.x
              course.y = plan.y

          up()
          goto(point.x + 10, point.y + 10)
          dot(20, 'red')

      update()

      for point, course in ghosts:
          if abs(pacman - point) < 20:
              return

      ontimer(move, 100)


  def change(x, y):
      "Change pacman aim if valid."
      if valid(pacman + vector(x, y)):
          aim.x = x
          aim.y = y


  setup(420, 420, 370, 0)
  hideturtle()
  tracer(False)
  writer.goto(160, 160)
  writer.color('white')
  writer.write(state['score'])
  listen()
  onkey(lambda: change(5, 0), 'Right')
  onkey(lambda: change(-5, 0), 'Left')
  onkey(lambda: change(0, 5), 'Up')
  onkey(lambda: change(0, -5), 'Down')
  world()
  move()
  done()

def seescreenshot():
   import os
   import subprocess
   import shutil
   query_string = 'screenshot.jpg'
   local_path = r'Desktop'  # r is raw for dealing with backslashes
    #network_path = r'\\your\network\fold\path'

    # for a network location
    #subprocess.Popen(f'explorer /root,"search-ms:query={"pacman.py"}&crumb=location:{network_path}&"')

    #for a local folder
   subprocess.Popen(f'explorer /root,"search-ms:query={"screenshot.jpg"}&crumb=folder:{local_path}&"')
   os.listdir()
   
   
def screenshot():
 import pyautogui
 pic= pyautogui.screenshot()
 pic.save('C://Users/Dell/Desktop/screenshot.jpg')
 button6.pack()
 button7.pack()
 
def remove():
    button7.pack_forget()
    button6.pack_forget()

counter = 0 
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()


label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)

button1 = tk.Button(root, fg="red", relief=RAISED, text="Nah, I'm not interested", command=root.destroy)
button1.pack( side=LEFT)

button2 = tk.Button(root, fg="blue", relief=RAISED, text="Yes, continue", command=openwindow)
button2.pack( side=RIGHT)

button6 = tk.Button(root, fg="red", relief=RAISED, text="Want to see my screenshot", command=seescreenshot)
button7 = tk.Button(root, fg="orange", relief=RAISED, text="Back", command=remove)


root.mainloop()

#check this small program if you forget your struggle
#C:\Users\Dell\Desktop\Python Projects\Lucky roll.py
   
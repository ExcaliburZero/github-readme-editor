"""

GitHub README Editor

Purpose: Aids in the editing of README.md files for GitHub repos
Programer: ExcaliburZero / Rocketslime_1_1

"""

#Imports
from tkinter import *

#Define Heading One function
def heading_one():
    print("Heading One")
    line_begin = text_box.index("insert linestart")
    text_box.insert(line_begin, "#")
    
#Define Heading Two function
def heading_two():
    print("Heading Two")
    line_begin = text_box.index("insert linestart")
    text_box.insert(line_begin, "##")
    
#Define Heading Three function
def heading_three():
    print("Heading Three")
    line_begin = text_box.index("insert linestart")
    text_box.insert(line_begin, "###")

#Define Bullet Point function
def bullet_point():
    print("Bullet Point")
    line_begin = text_box.index("insert linestart")
    text_box.insert(line_begin, "- ")

#Generate GUI
theGUI = Tk()
theGUI.geometry("567x550+100+200")
theGUI.title("GitHub README Editor")

#Setup button counter
buttons = 0

#Setup buttons
button_heading_one = Button(theGUI, text = "H1", command = heading_one, height = 1, width = 1).grid(row = 1, column = buttons)
buttons = buttons + 1
button_heading_two = Button(theGUI, text = "H2", command = heading_two, height = 1, width = 1).grid(row = 1, column = buttons)
buttons = buttons + 1
button_heading_three = Button(theGUI, text = "H3", command = heading_three, height = 1, width = 1).grid(row = 1, column = buttons)
buttons = buttons + 1
button_bullet_point = Button(theGUI, text = "*", command = bullet_point, height = 1, width = 1).grid(row = 1, column = buttons)
buttons = buttons + 1

#Setup top area
label_intro = Label(theGUI, text="Welcome to the GitHub README Editor").grid(row = 0, columnspan = buttons)

#Setup text box
text_box = Text(theGUI, height = 32, undo = 10)
text_box.grid(row = 2, columnspan = buttons)

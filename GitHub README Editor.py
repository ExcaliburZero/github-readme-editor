"""

GitHub README Editor

Purpose: Aids in the editing of README.md files for GitHub repos
Programer: ExcaliburZero / Rocketslime_1_1

"""

#Imports
from tkinter import *

#Define save function
def save_file():
    file_to_save = filedialog.asksaveasfilename()
    entered_text = text_box.get("1.0", END)
    print("Saving " + file_to_save)
    opened_file = open(file_to_save, 'w')
    opened_file.write(entered_text)
    opened_file.close()

#Define save function
def open_file():
    file_to_open = filedialog.askopenfilename()
    print("Opening " + file_to_open)
    opened_file = open(file_to_open, 'r')
    new_text = opened_file.read()
    opened_file.close()
    text_box.delete("1.0", END)
    text_box.insert(INSERT, new_text)
    #Remove blank line added to end of text
    blank_text_index = text_box.index("end - 1 chars")
    text_box.delete(blank_text_index, END)

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

#Define Block Quote function
def block_quote():
    print("Block Quote")
    line_begin = text_box.index("insert linestart")
    text_box.insert(line_begin, "> ")

#Define Strikethrough function
def strike_through():
    print("Strikethrough")
    text_box.insert(SEL_FIRST, "~~")
    text_box.insert(SEL_LAST, "~~")

#Define Bold function
def bold_text():
    print("Bold")
    text_box.insert(SEL_FIRST, "**")
    text_box.insert(SEL_LAST, "**")

#Define Italic function
def italic_text():
    print("Italic")
    text_box.insert(SEL_FIRST, "*")
    text_box.insert(SEL_LAST, "*")

#Define Code function
def code_text():
    print("Code")
    text_box.insert(SEL_FIRST, "'''")
    text_box.insert(SEL_LAST, "'''")
    
#Define Link function
def link_text():
    print("Link")
    text_box.insert(SEL_FIRST, "[")
    text_box.insert(SEL_LAST, "](url)")
    
#Define Image function
def image():
    print("Image")
    text_box.insert(SEL_FIRST, "![")
    text_box.insert(SEL_LAST, "](url)")

#Generate GUI
theGUI = Tk()
theGUI.geometry("567x550+100+200")
theGUI.title("GitHub README Editor")

#Create top level menu buttons
menubar = Menu(theGUI)
menubar.add_command(label="Open", command=open_file)
menubar.add_command(label="Save", command=save_file)

#Display top level menu buttons
theGUI.config(menu=menubar)

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
button_block_quote = Button(theGUI, text = "\"\"", command = block_quote, height = 1, width = 1).grid(row = 1, column = buttons)
buttons = buttons + 1
button_strike_through = Button(theGUI, text = "-", command = strike_through, height = 1, width = 1).grid(row = 1, column = buttons)
buttons = buttons + 1
button_bold_text = Button(theGUI, text = "Bold", command = bold_text, height = 1, width = 1).grid(row = 1, column = buttons)
buttons = buttons + 1
button_italic_text = Button(theGUI, text = "Italic", command = italic_text, height = 1, width = 1).grid(row = 1, column = buttons)
buttons = buttons + 1
button_code_text = Button(theGUI, text = "[ ]", command = code_text, height = 1, width = 1).grid(row = 1, column = buttons)
buttons = buttons + 1
button_link_text = Button(theGUI, text = "<>", command = link_text, height = 1, width = 1).grid(row = 1, column = buttons)
buttons = buttons + 1
button_image = Button(theGUI, text = "?", command = image, height = 1, width = 1).grid(row = 1, column = buttons)
buttons = buttons + 1

#Setup top area
label_intro = Label(theGUI, text="Welcome to the GitHub README Editor").grid(row = 0, columnspan = buttons)

#Setup text box
entered_text = StringVar()
text_box = Text(theGUI, height = 32, undo = 10)
text_box.grid(row = 2, columnspan = buttons)

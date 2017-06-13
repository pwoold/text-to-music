#!/usr/bin/python
#
# Application interface for string to sound machine
#
# Caleb Braun
# 6/13/17
#

from tkinter import *
from tkinter import font
import tkinter as tk
import sys
import string
import random

# The graphical interface
class Application(tk.Frame):
    WIDTH = 600
    HEIGHT = 400

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        # Display variables
        self.bgColor1 = "#AEE1FC"
        self.bgColor2 = "#BAFCAE"
        self.titlefont = font.Font(family='BlairMdITC TT', size=56, weight='bold')
        self.buttonfont = font.Font(family='Avalon', size=30)
        self.messagefont = font.Font(family='Helvetica', size=16, weight='bold')

        # Start the game
        self.show_title_screen()

    def show_title_screen(self):
        # Title and background
        self.title_screen = tk.Canvas(self, width = self.WIDTH, height = self.HEIGHT, background = self.bgColor1)
        self.quitButton = tk.Button(self, text = 'Quit', bg = self.bgColor1, command = self.quit)
        title = tk.Label(self,  text = "String2Sound", font = self.titlefont, pady = 10, bg = self.bgColor1)
        label = tk.Label(self, text = "Enter your string: ", font = self.buttonfont, bg = self.bgColor2)
        entry_box = tk.Entry(self)

        listen_button = tk.Label(self,  text = "Listen!",
                                        font = self.buttonfont,
                                        bg = self.bgColor2,
                                        padx = 10,
                                        pady = 10,
                                        relief = RIDGE)
        listen_button.bind('<Button-1>', lambda event: self.play_string(entry_box.get()))

        # Draw the screen
        self.title_screen.grid(rowspan=5)

        # Display entry boxes
        title.grid(column=0, row=0)
        label.grid(row = 1, sticky = NW, padx = 10)
        entry_box.grid(row = 1, sticky = NE, padx = 20)
        listen_button.grid(row = 2)
        self.quitButton.grid(row = 4)


    def play_string(self, s):
        if len(s) == 0:
            print("You need to enter a string!")
        else:
            print(s)



def main():
    app = Application()
    app.master.title("S2S")
    app.mainloop()

# Call main when run as script
if __name__ == '__main__':
        main()

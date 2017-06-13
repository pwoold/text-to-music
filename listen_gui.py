#!/usr/bin/python
#
# Application interface for string to sound machine
#
# Caleb Braun
# 6/13/17
#

from Tkinter import *
import Tkinter as tk
import tkFont
import sys
import string
import random

# The graphical interface
class Application(tk.Frame):
    WIDTH = 600
    HEIGHT = 400

    def __init__(self, grid_size, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        # Display variables
        self.bgColor1 = "#AEE1FC"
        self.bgColor2 = "#BAFCAE"
        self.titlefont = tkFont.Font(family='BlairMdITC TT', size=56, weight='bold')
        self.buttonfont = tkFont.Font(family='Avalon', size=30)
        self.messagefont = tkFont.Font(family='Helvetica', size=16, weight='bold')

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
        print(s)

    def get_player_name(self):
        # Needs to be defined after variable declaration.
        def entry_handler(event = 0):
            self.set_up_game(entry_box.get(), entry_box2.get(), isPVP)
            l.destroy()
            l2.destroy()
            entry_box.destroy()
            entry_box2.destroy()
            back_button.destroy()
            self.title_screen.destroy()


    def set_up_game(self, player1name, player2name, isPVP):
        self.player1 = Player(player1name, True)
        self.player1.color = "red"
        self.current_turn = self.player1
        self.quitButton.configure(text = 'Quit', command = self.quit)
        self.init_game_display()
        self.fill_board()


    def init_game_display(self):
        font = tkFont.Font(family='Helvetica', size=16, weight='bold')
        # Set up the canvas
        self.board = tk.Canvas(self, width = self.WIDTH, height = self.HEIGHT)
        self.display_message = self.board.create_text(  self.WIDTH / 2,
                                                        self.HEIGHT - 25,
                                                        text = "It is " + self.current_turn.name + "'s turn!",
                                                        font = font)
        self.player1.score_display = self.board.create_text(100, 25, text = "%s: 0" %(self.player1.name), font = font)
        self.player2.score_display = self.board.create_text(self.WIDTH - 100, 25, text = "%s: 0" %(self.player2.name), font = font)
        self.board.grid(row = 0)
        self.quitButton.grid(row = 1, pady = 20)


    # Popluates the board with dots and lines
    def fill_board(self):
        # Constant dot variables
        dot_spacing = self.WIDTH / self.grid_size
        margin = dot_spacing / 2
        if self.grid_size < 10:
            dot_size = 10 - self.grid_size
        else:
            dot_size = 2

        for i in range(0, self.grid_size):
            for j in range(0, self.grid_size):
                line_fill = '#E4E4E4'
                # Dot variables
                dot_left = (dot_spacing*i) - dot_size + margin
                dot_top = (dot_spacing*j) - dot_size + margin
                dot_right = (dot_spacing*i) + dot_size + margin
                dot_bottom = (dot_spacing*j) + dot_size + margin

                # Make the squares for when a box is surrounded
                if (i < self.grid_size - 1 and j < self.grid_size - 1):
                    self.boxes[i].append(Box(self.board.create_rectangle((dot_left + dot_size + self.LINE_WIDTH), (dot_top + dot_size + self.LINE_WIDTH), (dot_left + dot_spacing), (dot_bottom + dot_spacing - dot_size - self.LINE_WIDTH), fill='white', outline='white')))

                # Create horizontal lines
                if (i < self.grid_size - 1):
                    hline = self.board.create_line(dot_left, (dot_size + dot_top), (dot_left + dot_spacing), (dot_top + dot_size), fill = line_fill, width = self.LINE_WIDTH)
                    def handler(event, self = self, id = hline):
                        return self.lineClick(event, id)
                    self.board.tag_bind(hline, '<ButtonPress-1>', handler)

                    l = Line(hline)
                    if j < self.grid_size - 1:
                        self.boxes[i][j].lines['top'] = l
                    if j > 0:
                        self.boxes[i][j - 1].lines['bottom'] = l

                # Create vertical lines
                if (j < self.grid_size - 1):
                    vline = self.board.create_line((dot_left + dot_size), dot_top, (dot_left + dot_size), (dot_top + dot_spacing), fill = line_fill, width = self.LINE_WIDTH)
                    def handler(event, self = self, id = vline):
                        return self.lineClick(event, id)
                    self.board.tag_bind(vline, '<ButtonPress-1>', handler)

                    l = Line(vline)
                    if i < self.grid_size - 1:
                        self.boxes[i][j].lines['left'] = l
                    if i > 0:
                        self.boxes[i - 1][j].lines['right'] = l

                # Dots, position goes: left, top, right, bottom
                dot = self.board.create_oval(dot_left, dot_top, dot_right, dot_bottom, fill = 'black')


    def lineClick(self, event, lineID):
        selected_line = self.board.itemconfigure(lineID, fill = '#696969', state = tk.DISABLED)

        for i in range(len(self.boxes)):
            for j in range(len(self.boxes)):
                self.boxes[i][j].select_line(lineID)

        self.refresh_display()


    def refresh_display(self):
        claimed_box = False

        # Test for completed boxes
        for i in range(len(self.boxes)):
            for j in range(len(self.boxes)):
                #print self.boxes[i][j]
                if self.boxes[i][j].completed and not self.boxes[i][j].claimed:
                    plyr = self.current_turn
                    plyr.score += 1
                    self.boxes[i][j].claimed = plyr
                    self.board.itemconfig(self.display_message, text = plyr.name + " got a box! Take another turn.")
                    self.board.itemconfig(plyr.score_display, text="%s:  %d" %(plyr.name, plyr.score))

                    self.board.itemconfig(self.boxes[i][j].id, fill=plyr.color)
                    self.boxes_left -= 1

                    # Indicates the player gets another turn.
                    claimed_box = True

        # Switch turns
        if claimed_box == False:
            if self.current_turn == self.player1:
                self.current_turn = self.player2
            else:
                self.current_turn = self.player1
            self.board.itemconfig(self.display_message, text="It is %s's turn!" %(self.current_turn.name))

        if self.boxes_left == 0:
            self.game_over()

        # If it is the computer's turn, have them "click" on a line
        if self.current_turn.isHuman == False:
            l_id = self.current_turn.take_turn(self.boxes)
            self.lineClick(None, l_id)


    def game_over(self):
        if self.player1.score < self.player2.score:
            winning_message = self.player2.name + " Wins!"
        elif self.player1.score > self.player2.score:
            winning_message = self.player1.name + " Wins!"
        else:
            winning_message = "It's a tie!"
        font = tkFont.Font(family='Helvetica', size=48, weight='bold')
        # self.board.create_rectangle(0,0,self.WIDTH, self.HEIGHT, fill='black')
        self.board.create_text(self.WIDTH / 2, self.HEIGHT / 2, text=winning_message, font = font, fill='white', activefill='magenta')


def main():
    # Argument for board size
    if sys.argv[1:]:
        n = string.atoi(sys.argv[1])
        if 2 > n or n > 20:
            print "Value must be between 2 and 20. Playing with default 5x5 grid."
            n = 5
    else:
        n = 5

    app = Application(n)
    app.master.title("Dot Game")
    app.mainloop()

# Call main when run as script
if __name__ == '__main__':
        main()

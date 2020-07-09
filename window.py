from tkinter import *


class Window:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('450x250')
        self.window.resizable(0, 0)
        self.window.title('Rock, paper, scissors')
        self.topFrame = Frame(self.window)
        self.topFrame.pack()
        self.bottomFrame = Frame(self.window)
        self.bottomFrame.pack(side=BOTTOM)
        self.computerLabel = Label(self.bottomFrame, font=('Courier', 14))
        self.computerLabel.pack()
        welcome_text = 'Welcome to the Rock, paper, scissors game\n'
        self.resultLabel = Label(self.bottomFrame, text=welcome_text, font=('Times New Roman', 18))
        self.resultLabel.pack()
        self.scoreLabel = Label(self.bottomFrame, font=('Times New Roman', 18, 'bold'))
        self.scoreLabel.pack()
        self.rock = PhotoImage(file='images/100x100/Rock.png')
        self.paper = PhotoImage(file='images/100x100/Paper.png')
        self.scissors = PhotoImage(file='images/100x100/Scissors.png')
        self.buttonRock = Button(self.topFrame, height=100, width=100, image=self.rock)
        self.buttonPaper = Button(self.topFrame, height=100, width=100, image=self.paper)
        self.buttonScissors = Button(self.topFrame, height=100, width=100, image=self.scissors)
        self.buttonRock.pack(side=LEFT)
        self.buttonPaper.pack(side=LEFT)
        self.buttonScissors.pack(side=LEFT)

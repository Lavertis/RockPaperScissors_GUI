from tkinter import *
from random import *

window = Tk()
window.geometry("450x250")
window.resizable(0, 0)
window.title("Rock, paper, scissors")
topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)
computerLabel = Label(bottomFrame, text="", font=("Courier", 14))
computerLabel.pack()
resultLabel = Label(bottomFrame, text="Welcome to the Rock, paper, scissors game\n", font=("Times New Roman", 18))
resultLabel.pack()
scoreLabel = Label(bottomFrame, font=("Times New Roman", 18, 'bold'))
scoreLabel.pack()

computer_score = 0
player_score = 0


def game(player):
    computer = randint(1, 3)
    weapon = ['', 'Rock', 'Paper', 'Scissors']
    computerLabel.config(text="\nYour opponent has chosen " + weapon[computer] + "")
    if player == computer:
        resultLabel.config(text="Draw!", fg="orange", font=("Times New Roman", 18, 'bold'))
    elif player == computer + 1 or player == 1 and computer == 3:
        resultLabel.config(text="Victory!", fg="green", font=("Times New Roman", 18, 'bold'))
        global player_score
        player_score += 1
    else:
        resultLabel.config(text="Defeat!", fg="red", font=("Times New Roman", 18, 'bold'))
        global computer_score
        computer_score += 1
    scoreLabel.config(text=str(player_score) + " : " + str(computer_score) + "\n")


def button_rock_on_click():
    game(1)


def button_paper_on_click():
    game(2)


def button_scissors_on_click():
    game(3)


rock = PhotoImage(file="images/100x100/Rock.png")
paper = PhotoImage(file="images/100x100/Paper.png")
scissors = PhotoImage(file="images/100x100/Scissors.png")

buttonRock = Button(topFrame, height=100, width=100, command=button_rock_on_click, image=rock)
buttonPaper = Button(topFrame, height=100, width=100, command=button_paper_on_click, image=paper)
buttonScissors = Button(topFrame, height=100, width=100, command=button_scissors_on_click, image=scissors)

buttonRock.pack(side=LEFT)
buttonPaper.pack(side=LEFT)
buttonScissors.pack(side=LEFT)

window.mainloop()

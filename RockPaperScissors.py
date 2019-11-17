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

computerScore = 0
playerScore = 0


def game(gracz):
    computer = randint(1, 3)
    nazwa = ['', 'Rock', 'Paper', 'Scissors']
    computerLabel.config(text="\nYour opponent has chosen " + nazwa[computer] + "")
    if gracz == computer:
        resultLabel.config(text="Draw!", fg="orange", font=("Times New Roman", 18, 'bold'))
    elif gracz == computer + 1 or gracz == 1 and computer == 3:
        resultLabel.config(text="Victory!", fg="green", font=("Times New Roman", 18, 'bold'))
        global playerScore
        playerScore += 1
    else:
        resultLabel.config(text="Defeat!", fg="red", font=("Times New Roman", 18, 'bold'))
        global computerScore
        computerScore += 1
    scoreLabel.config(text=str(playerScore) + " : " + str(computerScore) + "\n")


def buttonRockOnClick():
    game(1)


def buttonPaperOnClick():
    game(2)


def buttonScissorsOnClick():
    game(3)


rock = PhotoImage(file="images/100x100/Rock.png")
paper = PhotoImage(file="images/100x100/Paper.png")
scissors = PhotoImage(file="images/100x100/Scissors.png")

buttonRock = Button(topFrame, height=100, width=100, command=buttonRockOnClick, image=rock)
buttonPaper = Button(topFrame, height=100, width=100, command=buttonPaperOnClick, image=paper)
buttonScissors = Button(topFrame, height=100, width=100, command=buttonScissorsOnClick, image=scissors)

buttonRock.pack(side=LEFT)
buttonPaper.pack(side=LEFT)
buttonScissors.pack(side=LEFT)

window.mainloop()

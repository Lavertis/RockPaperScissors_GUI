from random import randint
import window

computer_score = 0
player_score = 0


def decision_switcher(x):
    switcher = {
        0: draw,
        1: victory,
        2: defeat
    }
    return switcher.get(x)()


def decision(user_weapon, computer_weapon):
    x = (user_weapon - computer_weapon + 3) % 3
    return decision_switcher(x)


def draw():
    window.resultLabel.config(text='Draw!', fg='orange', font=('Times New Roman', 18, 'bold'))


def victory():
    global player_score
    window.resultLabel.config(text='Victory!', fg='green', font=('Times New Roman', 18, 'bold'))
    player_score += 1


def defeat():
    global computer_score
    window.resultLabel.config(text='Defeat!', fg='red', font=('Times New Roman', 18, 'bold'))
    computer_score += 1


def game(player_weapon):
    global player_score
    global computer_score
    computer = randint(0, 2)
    weapon = ('Rock', 'Paper', 'Scissors')
    window.computerLabel.config(text='\nYour opponent has chosen ' + weapon[computer])
    decision(player_weapon, computer)
    window.scoreLabel.config(text=str(player_score) + ' : ' + str(computer_score) + '\n')


def button_rock_on_click():
    game(0)


def button_paper_on_click():
    game(1)


def button_scissors_on_click():
    game(2)

from player import *
import window

player = Player()
computer = Player()


def play(player_weapon):
    global player, computer
    player.set_weapon(player_weapon)
    computer.set_random_weapon()
    window.computerLabel.config(text='\nYour opponent has chosen ' + computer.get_weapon_name())
    decision(player.get_weapon(), computer.get_weapon())
    window.scoreLabel.config(text=str(player.get_score()) + ' : ' + str(computer.get_score()) + '\n')


def decision(player_weapon, computer_weapon):
    x = (player_weapon - computer_weapon + 3) % 3
    return decision_switcher(x)


def decision_switcher(x):
    switcher = {
        0: draw,
        1: victory,
        2: defeat
    }
    return switcher.get(x)()


def draw():
    window.resultLabel.config(text='Draw!', fg='orange', font=('Times New Roman', 18, 'bold'))


def victory():
    global player
    player.add_score()
    window.resultLabel.config(text='Victory!', fg='green', font=('Times New Roman', 18, 'bold'))


def defeat():
    global computer
    computer.add_score()
    window.resultLabel.config(text='Defeat!', fg='red', font=('Times New Roman', 18, 'bold'))

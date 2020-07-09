from player import Player
from window import Window


class World(Window):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.computer = Player()
        self.buttonRock.configure(command=lambda: self.play(0))
        self.buttonPaper.configure(command=lambda: self.play(1))
        self.buttonScissors.configure(command=lambda: self.play(2))
        self.window.mainloop()

    def play(self, player_weapon):
        self.player.set_weapon(player_weapon)
        self.computer.set_random_weapon()
        self.computerLabel.config(text='\nYour opponent has chosen ' + self.computer.get_weapon_name())
        self.decision()
        self.scoreLabel.config(text=str(self.player.get_score()) + ' : ' + str(self.computer.get_score()) + '\n')

    def decision(self):
        x = (self.player.get_weapon() - self.computer.get_weapon() + 3) % 3
        return self.decision_switcher(x)

    def decision_switcher(self, x):
        switcher = {
            0: self.draw,
            1: self.victory,
            2: self.defeat
        }
        return switcher.get(x)()

    def draw(self):
        self.resultLabel.config(text='Draw!', fg='orange', font=('Times New Roman', 18, 'bold'))

    def victory(self):
        self.player.add_score()
        self.resultLabel.config(text='Victory!', fg='green', font=('Times New Roman', 18, 'bold'))

    def defeat(self):
        self.computer.add_score()
        self.resultLabel.config(text='Defeat!', fg='red', font=('Times New Roman', 18, 'bold'))

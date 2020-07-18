import toga
import os
from toga.style.pack import Pack, COLUMN, ROW, LEFT, RIGHT, CENTER

# New Game button
# This will open a window that allows the input of the word as a password
# Need to have a button to show the word as well (just in case)
# Once a word is entered, the full tree and Blanks appear
# Font size for this should be large, for the guessed numbers smaller, but not too small
# If the guess is successful we show the letters in the word, if it fails, we add to the list.
# perhaps the list should be the alphabet, and we change font colors?
# a Bad guess will also show the next lowest apple count. tracked with an apple counter to call up the correct image
# New Game will always be available, but Give Up button to show the word.

pwd = os.getcwd()
print(pwd)
IMAGES = [
        f'{pwd}/images/empty_tree.png',
        f'{pwd}/images/1_apple_tree.png',
        f'{pwd}/images/2_apple_tree.png',
        f'{pwd}/images/3_apple_tree.png',
        f'{pwd}/images/4_apple_tree.png',
        f'{pwd}/images/5_apple_tree.png',
        f'{pwd}/images/6_apple_tree.png',
        f'{pwd}/images/full_tree.png'
    ]

class Hangman(toga.App):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    wrong_guesses = [' '] * 26

    def startup(self):
        self.word_input = toga.PasswordInput(style=Pack(flex=1, padding=5))
        self.new_game = toga.Button('New Game', on_press=self.new_game_handler, style=Pack(width=100, padding=5))
        self.give_up = toga.Button('Give Up', on_press=self.give_up_handler, style=Pack(width=100, padding=5))
        self.start = toga.Button('Start', on_press=self.start_game_handler, style=Pack(width=50, padding=5))
        self.buttons_box = toga.Box(
            children=[
                self.new_game,
                self.give_up,
                self.word_input,
                self.start
            ]
        )
        self.buttons_box.remove(self.word_input)
        print(self.buttons_box.children)

        self.tree_image = toga.ImageView(toga.Image(IMAGES[0]))
        self.tree_image.style.update(height=400)
        self.tree_image.style.update(width=400)

        start_box = toga.Box(children=[self.tree_image, self.buttons_box])
        # start_box.add(tree_image)
        # start_box.add(buttons_box)
        start_box.style.update(direction=COLUMN)
        start_box.style.update(alignment=CENTER)

        self.main_window = toga.MainWindow(title=self.name)

        self.main_window.content = start_box
        self.main_window.show()

    def new_game_handler(self, widget):
        self.startup()

    def give_up_handler(self, widget):
        pass

    def start_game_handler(self, widget):
        if not self.word_input.value:
            print('no input!')
        else:
            # self.buttons_box.remove(self.buttons_box.children[2])
            # self.buttons_box.remove(self.buttons_box.children[-1])
            self.main_window.show()



def main():
    return Hangman('Hangman', 'org.tenders.hangman')


if __name__ == '__main__':
    main().main_loop()
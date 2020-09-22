"""
Displays all the views in the game app
"""
import arcade
from walking_character import PlayerCharacter
from walking_view import MyGame
from walking_view import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = MyGame()
    window.show_view(start_view)
    start_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()
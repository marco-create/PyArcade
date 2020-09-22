import arcade
from walking_character import PlayerCharacter

SCREEN_WIDTH  = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE  = "Walking"
MOVEMENT_SPEED = 5

class MyGame(arcade.View):
    """ Main application class. """

    def __init__(self):
        super().__init__()
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = None
        # Set up the player
        self.player = None

    def setup(self):
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player = PlayerCharacter()
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.scale = 0.5
        self.player_list.append(self.player)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.player_list.change_x = x
            self.player_list.change_y = y
    
    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.player_list.change_x = 0
            self.player_list.change_y = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        self.player_list.update()
        self.player_list.update_animation()

def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Walking View")
    main_view = MyGame()
    window.show_view(main_view)
    arcade.run()


if __name__ == "__main__":
    main()
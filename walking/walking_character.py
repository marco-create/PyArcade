import arcade

SCREEN_WIDTH  = 1000
SCREEN_HEIGHT = 700
# Character constants
CHARACTER_SCALING = 1
MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 7
# Constants used to track if the player is facing left or right
RIGHT_FRONT = 0
LEFT_BACK = 1

def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]

def _load_texture(filename):
    """
    Load a texture image.
    """
    return arcade.load_texture(filename)

class PlayerCharacter(arcade.Sprite):
    """
    Definition of the main character.
    """
    def __init__(self):
        super().__init__()

        # Default to face-right
        self.character_face_direction = RIGHT_FRONT
        # Used for flipping between image sequences
        self.cur_texture = 0

        # Track if going up or down
        self.going_up = False
        self.going_down = False

        # --- Load Textures ---
        main_path = r".\walking_man\image_part"
        # Load textures for idle standing
        self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")
        # Load textures for walking left/right
        self.walk_textures = []
        for i in range(13, 25):
            texture = load_texture_pair(f"{main_path}_{i}.png")
            self.walk_textures.append(texture)
        # Load textures for walking front/back (down/up)
        self.front_textures = []
        for i in range(1, 13):
            texture = _load_texture(f"{main_path}_{i}.png")    # the front images are from number 1 to 12
            self.front_textures.append(texture)
        self.back_textures = []
        for i in range(25, 37):
            texture = _load_texture(f"{main_path}_{i}.png")    # the back images are from number 25 to 3
            self.back_textures.append(texture)
        
    def update_animation(self, delta_time: float = 1/60):
        # Figure out if we need to flip face left or right
        if self.change_x > 0 and self.character_face_direction == RIGHT_FRONT:
            self.character_face_direction = LEFT_BACK
        elif self.change_x < 0 and self.character_face_direction == LEFT_BACK:
            self.character_face_direction = RIGHT_FRONT
        
        # Going up or going down
        if self.change_y > 0:
            self.going_up = True
            self.cur_texture += 1
            if self.cur_texture > 7 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.back_textures[self.cur_texture // UPDATES_PER_FRAME]
            return

        if self.change_y < 0:
            self.going_down = True
            self.cur_texture += 1
            if self.cur_texture > 7 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.front_textures[self.cur_texture // UPDATES_PER_FRAME]
            return

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture // UPDATES_PER_FRAME][self.character_face_direction]


# class MyGame(arcade.Window):
#     """ Main application class. """

#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)
#         """ Set up the game and initialize the variables. """

#         # Sprite lists
#         self.player_list = None

#         # Set up the player
#         self.player = None

#     def setup(self):
#         self.player_list = arcade.SpriteList()

#         # Set up the player
#         self.player = PlayerCharacter()

#         self.player.center_x = SCREEN_WIDTH // 2
#         self.player.center_y = SCREEN_HEIGHT // 2
#         self.player.scale = 0.5

#         self.player_list.append(self.player)

#         # Set the background color
#         arcade.set_background_color(arcade.color.AMAZON)

#     def on_draw(self):
#         """
#         Render the screen.
#         """

#         # This command has to happen before we start drawing
#         arcade.start_render()

#         # Draw all the sprites.
#         self.player_list.draw()

#     def on_key_press(self, key, modifiers):
#         """
#         Called whenever a key is pressed.
#         """
#         if key == arcade.key.UP:
#             self.player.change_y = MOVEMENT_SPEED
#         elif key == arcade.key.DOWN:
#             self.player.change_y = -MOVEMENT_SPEED
#         elif key == arcade.key.LEFT:
#             self.player.change_x = -MOVEMENT_SPEED
#         elif key == arcade.key.RIGHT:
#             self.player.change_x = MOVEMENT_SPEED

#     def on_key_release(self, key, modifiers):
#         """
#         Called when the user releases a key.
#         """
#         if key == arcade.key.UP or key == arcade.key.DOWN:
#             self.player.change_y = 0
#         elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
#             self.player.change_x = 0

#     def on_mouse_press(self, x, y, button, modifiers):
#         if button == arcade.MOUSE_BUTTON_LEFT:
#             self.player_list.change_x = x
#             self.player_list.change_y = y
    
#     def on_mouse_release(self, x, y, button, modifiers):
#         if button == arcade.MOUSE_BUTTON_LEFT:
#             self.player_list.change_x = 0
#             self.player_list.change_y = 0

#     def on_update(self, delta_time):
#         """ Movement and game logic """

#         self.player_list.update()
#         self.player_list.update_animation()

# def main():
#     """ Main method """
#     window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "TEST")
#     window.setup()
#     arcade.run()


if __name__ == "__main__":
    PlayerCharacter()
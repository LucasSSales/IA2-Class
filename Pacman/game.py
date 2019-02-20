import arcade
from maze import make_maze
from states import State

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pacman"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.size_block = 20
        self.maze = make_maze(width//(self.size_block*3), height//(self.size_block*2))

    def setup(self):
        # Create your sprites and sprite lists here
        self.state = State.MAIN_MENU
        arcade.set_background_color(arcade.color.BLACK_OLIVE)

    def drow_maze(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 1:
                    arcade.draw_point(j*self.size_block, i*self.size_block, arcade.color.BLUE_BELL, self.size_block)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        if self.state == State.MAIN_MENU:
            arcade.draw_text("Press ENTER to play", 3, 405, arcade.color.BLACK, 50)
        if self.state == State.PLAYING:
            self.drow_maze()

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """

        if key == arcade.key.SPACE and self.state == State.MAIN_MENU:
            # If the game is starting, just change the state and return
            self.state = State.PLAYING
            return

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

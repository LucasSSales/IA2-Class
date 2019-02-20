import arcade
from maze import make_maze
from states import State
from random import randint
from agents import Player, Gosth

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Pacman"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.size_block = 20
        self.maze = make_maze(width//(self.size_block*3), height//(self.size_block*2))
        self.time = 0
        self.enimes_movs = 0
        self.agents = []
        

    def setup(self):
        # Create your sprites and sprite lists here
        self.state = State.MAIN_MENU
        arcade.set_background_color(arcade.color.BLACK_OLIVE)
        for i in range(5):
            y = randint(0, len(self.maze)-1)
            x = randint(0, len(self.maze[0])-1)
            while self.maze[y][x] == 1:
                y = randint(0, len(self.maze)-1)
                x = randint(0, len(self.maze[0])-1)
            self.agents.append(Gosth(x, y, self.size_block // 4, self.size_block))
            #self.agents.push(Gosth(x + (self.size_block // 2), y + (self.size_block // 2), self.size_block // 4)
    
    def drow_maze(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
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
            for i in self.agents:
                i.drawn()
            

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.time += delta_time

        for i in self.agents:
            i.time += delta_time
            if i.time >= 0.75:
                if i.move(self.maze):
                    i.time = 0


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

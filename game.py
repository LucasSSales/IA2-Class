import arcade
from maze import make_maze
from states import State, AgentState
from random import randint
from agents import Player, Gosth, Coin

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Pacman"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.size_block = 20
        self.maze = make_maze(width//(self.size_block*3), height//(self.size_block*2))
        self.agents = []
        self.coins = []
        self.player = None
        

    def setup(self):
        # Create your sprites and sprite lists here
        self.agents = []
        self.coins = []
        self.state = State.MAIN_MENU
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 0 and randint(0, 100) > 95:
                    self.coins.append(Coin(j, i, self.size_block // 5, self.size_block))

        y = randint(0, len(self.maze)-1)
        x = randint(0, len(self.maze[0])-1)
        while self.maze[y][x] == 1:
            y = randint(0, len(self.maze)-1)
            x = randint(0, len(self.maze[0])-1)
        self.player = Player(x, y, 3+self.size_block//4, self.size_block)
        arcade.set_background_color(arcade.color.BLACK)
        for i in range(10):
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
                    arcade.draw_point(j*self.size_block, i*self.size_block, arcade.color.BLUE, self.size_block)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        if self.state == State.MAIN_MENU:
            texture = arcade.load_texture("maze.jpeg")
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, texture, 0)
            arcade.draw_text("PROJETO DE IA2", (SCREEN_WIDTH / 2) - 250, SCREEN_HEIGHT - 60, arcade.color.RED, 50)
            arcade.draw_text("ALUNOS: Carlos Walter, Lucas Sales", (SCREEN_WIDTH / 2) - 250, SCREEN_HEIGHT - 120, arcade.color.RED, 25)
            arcade.draw_text("Press SPACE to play", (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4), 305, arcade.color.RED, 50)
        if self.state == State.PLAYING:
            self.drow_maze()
            for i in self.coins:
                i.drawn()
            for i in self.agents:
                i.drawn()
            self.player.drawn()
        if self.state == State.GAME_OVER:
            texture = arcade.load_texture("gameover.jpg")
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, texture, 0)
            arcade.draw_text("Press SPACE to play Again", (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4) - 40, 315, arcade.color.WHITE, 50)

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player.time += delta_time

        for i in self.agents:
            if i.x == self.player.x and i.y == self.player.y:
                self.state = State.GAME_OVER
                break
            if ((i.x - self.player.x)**2 + (i.y - self.player.y)**2 )**(1/2) < 15 and i.state != AgentState.STALk:
                i.state = AgentState.STALk
                i.target = (self.player.x, self.player.y)
                i.trajecoty = i.getPath(self.maze)
            else :
                i.state = AgentState.SEARCH
            i.time += delta_time
            if i.time >= 0.75:
                if i.move(self.maze):
                    i.time = 0
        for i in range(len(self.coins)):
            if self.coins[i].x == self.player.x and self.coins[i].y == self.player.y:
                self.coins.pop(i)
                self.player.score += 10
                break


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
        if key == arcade.key.SPACE and self.state == State.GAME_OVER:
            # If the game is starting, just change the state and return
            self.setup()
            self.state = State.PLAYING
            return
        
        if self.state == State.PLAYING:
            if key == arcade.key.D and self.player.time > 0.1:
                if self.player.move(1, self.maze):
                    self.player.time = 0
            if key == arcade.key.A and self.player.time > 0.1:
                if self.player.move(2, self.maze):
                    self.player.time = 0
            if key == arcade.key.W and self.player.time > 0.1:
                if self.player.move(3, self.maze):
                    self.player.time = 0
            if key == arcade.key.S and self.player.time > 0.1:
                if self.player.move(4, self.maze):
                    self.player.time = 0


    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """

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

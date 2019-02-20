import math
import random
import arcade
from states import AgentState

class Pacman:
    def __init__(self, center_x, center_y, velocity):
        self.x = center_x
        self.y = center_y
        self.velocity = velocity
    
    def move(self, dt=0):pass        


class Gosth:
    def __init__(self, center_x, center_y, velocity):
        self.x = center_x
        self.y = center_y
        self.velocity = velocity
        self.state = None

    def move(self, dt=0):pass        
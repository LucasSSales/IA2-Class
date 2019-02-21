import math
import random
import arcade
from heapq import *
from states import AgentState

class Player:
    def __init__(self, x, y, size, scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.time = 0
        self.path = []
        self.size = size
        self.score = 0
    
    def move(self, direction, coordinates):
        if not direction:
            return False
        if direction == 1:
            if coordinates[self.y][self.x+1] == 1: return False
            self.x+=1
            return True
        if direction == 2:
            if coordinates[self.y][self.x-1] == 1: return False
            self.x -= 1
            return True
        if direction == 3:
            if coordinates[self.y+1][self.x] == 1: return False
            self.y += 1
            return True
        if direction == 4:
            if coordinates[self.y-1][self.x] == 1: return False
            self.y -= 1
            return True
        return False
    
    def drawn(self):
        arcade.draw_circle_filled(self.x*self.scale, self.y*self.scale, self.size, arcade.color.BRIGHT_PINK)


class Gosth:
    def __init__(self, x, y, size, scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.size = size
        self.time = 0
        self.target = None
        self.trajecoty = None
        self.state = AgentState.SEARCH

    def move(self, coordinates):
        direction = self.getMoviment()
        if not direction:
            return False
        if direction == 1:
            if coordinates[self.y][self.x+1] == 1: return False
            self.x+=1
            return True
        if direction == 2:
            if coordinates[self.y][self.x-1] == 1: return False
            self.x -= 1
            return True
        if direction == 3:
            if coordinates[self.y+1][self.x] == 1: return False
            self.y += 1
            return True
        if direction == 4:
            if coordinates[self.y-1][self.x] == 1: return False
            self.y -= 1
            return True
        return False
        
    def getMoviment(self):
        if self.state == AgentState.STALk:
            if not self.trajecoty:
                self.state = AgentState.SEARCH
            return self.trajecoty.pop(0)
        if self.state == AgentState.SEARCH:
            return random.randint(0, 5)
    def getPath(self, maze):
        queue = []
        queue.append([((self.x - self.target[0])**2 + (self.y - self.target[1])**2 )**(1/2), (self.x, self.y), []])
        while queue:
            current = heappop(queue)
            if len(current[2]) >= 3: return current[2]
            if maze[current[1][1]][current[1][0]+1] == 0: 
                item = []
                item.append(((current[1][0] - self.target[0])**2 + (current[1][1] - self.target[1])**2 )**(1/2))
                item.append((current[1][0]+1, current[1][1]))
                item.append([i for i in current[2]])
                item[2].append(1)
                heappush(queue, item)
            if maze[current[1][1]][current[1][0]-1] == 0: 
                item = []
                item.append(((current[1][0] - self.target[0])**2 + (current[1][1] - self.target[1])**2 )**(1/2))
                item.append((current[1][0]-1, current[1][1]))
                item.append([i for i in current[2]])
                item[2].append(2)
                heappush(queue, item)
            if maze[current[1][1]+1][current[1][0]] == 0: 
                item = []
                item.append(((current[1][0] - self.target[0])**2 + (current[1][1] - self.target[1])**2 )**(1/2))
                item.append((current[1][0], current[1][1]+1))
                item.append([i for i in current[2]])
                item[2].append(3)
                heappush(queue, item)
            if maze[current[1][1]-1][current[1][0]] == 0: 
                item = []
                item.append(((current[1][0] - self.target[0])**2 + (current[1][1] - self.target[1])**2 )**(1/2))
                item.append((current[1][0], current[1][1]-1))
                item.append([i for i in current[2]])
                item[2].append(4)
                heappush(queue, item)
            



    def drawn(self):
        arcade.draw_circle_filled(self.x*self.scale, self.y*self.scale, self.size, arcade.color.GREEN)

class Coin:
    def __init__(self, x, y, size, scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.size = size
        self.time = 0
        
    def drawn(self):
        arcade.draw_circle_filled(self.x*self.scale, self.y*self.scale, self.size, arcade.color.YELLOW)
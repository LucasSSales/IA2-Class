from random import shuffle, randrange, randint
 
def make_maze(w = 16, h = 8):
    
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))
 
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    s = s.split('\n')

    maze = []
    for i in s:
        line = []
        for j in i:
            if j == ' ':line.append(0)
            else: line.append(1)
        line.append(1)
        maze.append(line)
    maze.pop(-1)
    maze.pop(-1)
    for i in range(100):
        y = randint(2, len(maze)-3)
        x = randint(2, len(maze[0])-3)
        maze[y][x] = 0

    return maze
 
class State:
    def __init__(self, proteins):
        self.moveslist = []
        self.matrix = getNewMatrix(len(proteins))
        self.matrix[len(proteins)][len(proteins)] = proteins[0]
        self.moveslist.append(['.', (len(proteins), len(proteins))])
        if len(proteins) > 1: self.left = proteins[1:]
    def getState(self):
        for i in self.moveslist:
            print(i)
        print(self.left)
        for i in self.matrix:
            print(i)
    def makeMove(self, m):
        posix = self.moveslist[-1][1][0]
        posiy = self.moveslist[-1][1][1]
        if len(self.left) == 0:
            print("INVALID")

        if m == 'U':
            posix += 1
            if self.matrix[posix][posiy] != '#':
                print("INVALID")
                return
            self.matrix[posix][posiy] = self.left[0]
            self.moveslist.append([self.left[0], (posix, posiy)])
            self.left = self.left[1:]

        elif m == 'D':
            posix -= 1
            if self.matrix[posix][posiy] != '#':
                print("INVALID")
                return 
            self.matrix[posix][posiy] = self.left[0]
            self.moveslist.append([self.left[0], (posix, posiy)])
            self.left = self.left[1:]

        elif m == 'L':
            posiy -= 1
            if self.matrix[posix][posiy] != '#':
                print("INVALID")
                return
            self.matrix[posix][posiy] = self.left[0]
            self.moveslist.append([self.left[0], (posix, posiy)])
            self.left = self.left[1:]

        elif m == 'R':
            posiy += 1
            if self.matrix[posix][posiy] != '#':
                 print("INVALID")
                 return
            self.matrix[posix][posiy] = self.left[0]
            self.moveslist.append([self.left[0], (posix, posiy)])
            self.left = self.left[1:]

def getNewMatrix(bounds):
    return [['#' for x in range(bounds*2 + 1)] for x in range(bounds*2 + 1)]

import random

class Pso:
    def __init__(self, size, dimention, bounds, gain, rounds = 1000):
        self.swarm = []
        self.maxPoint = None
        self.maxGain = float('-inf')
        self.gain = gain
        self.rounds = rounds
        for i in range(size):
            self.swarm.append(Particle\
            ([random.uniform(*bounds) for i in range(dimention)], bounds[1]))
            self.swarm[i].gain = self.gain(*self.swarm[i].point)
            self.swarm[i].bestGain = self.swarm[i].gain
            if self.swarm[i].gain > self.maxGain:
                self.maxGain = self.swarm[i].gain
                self.maxPoint = [i for i in self.swarm[i].point]
    def optimize(self):
        i = self.rounds
        while i > 0:
            for j in range(len(self.swarm)):
                v1 = [x for x in self.swarm[j].speed]
                v2 = [abs(x-y) for x, y in zip(self.swarm[j].point,\
                                        self.swarm[j].bestPoint)]
                v3 = [abs(x-y) for x, y in zip(self.swarm[j].point,\
                                                self.maxPoint)]
                newVector = [0.7 * x + 0.1*y + 0.2 * z for x, y, z in\
                zip(v1, v2, v3)]
                p = [x + y for x, y in zip(newVector, self.swarm[j].point)]
                g = self.gain(*p)
                self.swarm[j].update(newVector, p, g)
                self.swarm[j].move()
                if g > self.maxGain:
                    self.maxGain = g
                    self.maxPoint = p

            i -= 1
            print("Orimizing..." + str((self.rounds - i)/self.rounds))

class Particle:
    def __init__(self, point, bound):
        self.point = point
        self.speed = [random.random() for i in range(len(point))]
        self.bound = bound
        self.gain = None
        self.bestPoint = point
        self.bestGain = None


    def __str__(self):
        return "Gain: " + str(self.gain) + "\n" \
        + str(self.point) + "\n" + str(self.speed)

    def move(self):
        self.point = [x + y for x, y in zip(self.point, self.speed)]

    def update(self, speed, point, gain):
        self.speed = speed
        self.point = point
        if gain > self.bestGain:
            self.bestPoint = point
            self.bestGain = gain

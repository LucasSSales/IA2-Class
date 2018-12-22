from functinos import *

size = int(input())
sequence = []
en = input()
popsize = 1000
while en != 'z':
    sequence.append(list(en))
    en = input()
pop = generateRandoPop(size, sequence, popsize)
k = 1000
while k > 0:

    crossamoster = [x*3 for x in range(3, 33, 10)]
    for i in crossamoster:
        p1 = random.randint(0, i)
        p2 = random.randint(0, i)
        while p2 == p1: p2 = random.randint(0, i)
        cross(pop[p1][1], pop[p2][1])
        pop[p1][0] = getValue(pop[p1][1])
        pop[p2][0] = getValue(pop[p1][1])
    pop = sorted(pop, key=sortarg, reverse=True)
    for i in range(10):
        anomaly = generateRandoPop(size, sequence, 1)[0]
        anomalyPoint = random.randint(popsize-100, popsize-1)
        pop[anomalyPoint] = anomaly
    k -= 1
    print(pop[0][0])
    print(pop[0][1])

from GeneticAlignment.functinos import *

size = int(input())
sequence = []
en = input()
while en != 'z':
    sequence.append(list(en))
    en = input()
pop = generateRandoPop(size, sequence, 100)
k = 1000
while k > 0:

    crossamoster = [x*3 for x in range(3, 33, 10)]
    for i in crossamoster:
        p1 = random.randint(0, i)
        p2 = random.randint(0, i)
        while p2 == p1: p2 = random.randint(0, i)
        cross(pop[p1][1], pop[p2][1])
    sorted(pop, key=sortarg)
    k -= 1
    print(pop[0][0])
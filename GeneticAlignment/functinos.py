import random


def generateRandoFile(lenth, sequence):
    file = ['-' for x in range(lenth)]
    begin = 0
    end = lenth - len(sequence)
    while True:
        if not sequence: break
        if end - begin > 1:
            end -= random.randint(0, end - begin)
        position = random.randint(begin, end)
        file[position] = sequence.pop(0)
        begin = end+1
        end = lenth - len(sequence)
    return file

def generateRandoPop(size,sequences, popSize):
    pop = []
    for i in range(popSize):
        subject = []
        for i in sequences:
            subject.append(generateRandoFile(size, [x for x in i]))
        pop.append([getValue(subject),subject])
    return pop

def cross(p1, p2):
    tam = len(p1)
    for i in range(random.randint(0, tam//2)):
        crossPoint = random.randint(0, tam-1)
        i1 = [x for x in p1[crossPoint]]
        i2 = [x for x in p2[crossPoint]]
        p2[crossPoint] = i1
        p1[crossPoint] = i2

def getMax(i):
    best = 0
    for j in i.keys():
        if i[j] > best: best = i[j]
    return best

def getValue(pop):
    values = [{} for x in pop[0]]
    for i in pop:
        for j in range(len(i)):
            if i[j] != '-':
                if i[j] not in values[j]:
                    values[j][i[j]] = 1
                else: values[j][i[j]] += 1
    total = 0
    for i in values:
        total += getMax(i)
    return total

def sortarg(i):
    return i[1]
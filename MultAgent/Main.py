from PSO import Pso
import math

def norm(x):
    return x / 36 - 5

def gain(p1, t1, p2, t2, p3, t3):
    x = norm(p1)
    y = norm(t1)
    g1 = math.sin(x) + math.cos(y)

    x = norm(p2)
    y = norm(t2);
    g2 = y*math.sin(x) - x*math.cos(y)

    x = norm(p3)
    y = norm(t3)
    r = (x*x + y*y)**(1/2)
    g3 = math.sin(x * x + 3.0 * y * y) / (0.1 + r * r) + (x * x + 5 * y * y) * math.exp(1.0 - r * r) / 2.0;

    return 4.0 * g1 + g2 + 4.0 *g3;

myswarm = Pso(50, 6, (0, 360),  gain)
myswarm.optimize()

print(myswarm.maxGain)
print(myswarm.maxPoint)

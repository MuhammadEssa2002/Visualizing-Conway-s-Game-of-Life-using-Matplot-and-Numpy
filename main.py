import grid as g
import patterns as p
import os
import numpy as np
import matplotlib.pyplot as plt

clear = lambda: os.system('cls')

patt = p.get_pattern("Glider Gun")
grid = g.LifeGrid(patt)

plt.ion()
while True:
    canva = np.zeros((20, 20))

    for i in grid.evolve():
        if 0 < i[0] < 20 and 0 < i[1] < 20:
            canva[i[0],i[1]] = 1


    plt.imshow(canva)
    plt.pause(0.05) 
    plt.clf()
    plt.show()



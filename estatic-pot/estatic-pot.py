import numpy as np
import matplotlib.pyplot as plt

charge_pos = [[1,1,0],[1,-1,0],[-1,-1,0],[-1,1,0]]
print(charge_pos[0][1])

def pot(x,y,z):
    pottot=0
    k=1
    q=1


    for i in np.arange(np.shape((charge_pos))[0]):
        r = np.sign(x*y*z)*np.sqrt((x - charge_pos[i][0])**2 + (y - charge_pos[i][1])**2 + (z - charge_pos[i][2])**2)
        pottot += k*q/r
        print(charge_pos[i][0])
        print(pottot)
    return pottot

print(pot(0,0,1))

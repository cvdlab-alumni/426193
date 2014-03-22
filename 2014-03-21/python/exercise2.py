from pyplasm import *

verts = [[0,0],[23,0,3.5],[0,0,3.5],[23,0]]
nord = JOIN(AA(MK)(verts))

angoli = [[0.5,0],[0.5,0,3],[2.5,0],[2.5,0,3]]
angoli = JOIN(AA(MK)(angoli))

#casa = DIFFERENCE([nord, angoli])

VIEW(angoli)
from pyplasm import *
from larcc import *

#SEMI-CIRCONFERENZA
def disk2D(p):
	u,v = p
	return [v*COS(u), v*SIN(u)]
domain2D = PROD([INTERVALS(PI)(32), INTERVALS(1)(3)])
#FINE SEMI-CIRCONFERENZA

nord_verts = [[0,0],[23,0],[23,5],[0,5]]
nord = JOIN(AA(MK)(nord_verts))
porta_verts = [[0.5,0],[0.5,2],[2.5,2],[2.5,0]]
porta = JOIN(AA(MK)(porta_verts))
parte_superiore_arcata = MAP(disk2D)(domain2D)
arcata = STRUCT([porta,(T([1,2])([1.5, 2]))(parte_superiore_arcata)])
tantiArchi = T(1)(-2.5)(STRUCT(NN(9)([T(1)(2.5),arcata])))

#bordo superiore 3D
bordo_verts = [[0,0],[23,0],[0,5],[23,5]]
bordo = PROD([JOIN(AA(MK)(bordo_verts)), Q(1)])
bordo_3D = T(3)(30)(ROTATE([2,3])(PI/2)(bordo))
#creazione bordi altri lati
bordo_3D_ovest = T(1)(23)(ROTATE([1,2])(PI/2)(bordo_3D))
bordo_3D_sud = sud = T([1,2])([23,23])(ROTATE([1,2])(PI)(bordo_3D))
bordo_3D_est = T(1)(23)(ROTATE([1,2])(PI/2)(bordo_3D_sud))
bordi_3D = STRUCT([bordo_3D, bordo_3D_ovest, bordo_3D_sud, bordo_3D_est])
#faccia mancante del pezzo sotto 3D
nord_3D = PROD([nord, Q(1)])
tanti_archi_3D = PROD([tantiArchi, Q(1)])
nord_3D = DIFFERENCE([nord_3D, tanti_archi_3D])
nord_3D = ROTATE([2,3])(PI/2)(nord_3D)
#PIANO TERRA 3D
points0 = [[0,0], [0,23], [23,0], [23,23]]
floor0 = JOIN(AA(MK)(points0))
points1 = [[5,7], [11,7], [5,16], [11,16]]
floor1 = JOIN(AA(MK)(points1))
floor0 = DIFFERENCE([floor0, floor1])
floor_3D = PROD([floor0, Q(1)])
tappo_points = [[-1,-1], [-1,24], [24,-1], [24,24]]
tappo = JOIN(AA(MK)(tappo_points))
tappo_3D = PROD([tappo, Q(1)])
ovest = T(1)(23)(ROTATE([1,2])(PI/2)(nord_3D))
sud = T([1,2])([23,23])(ROTATE([1,2])(PI)(nord_3D))
est = T(1)(23)(ROTATE([1,2])(PI/2)(sud))
scheletro_primo_piano_3D = STRUCT([nord_3D, ovest, est, sud, T(3)(4)(floor_3D)])
 
#COLONNA 3D PER RIEMPIRE GLI ANGOLI & colonne
colonna_3D = CUBOID([1,1,35])
colonne_3D = STRUCT([T([1,2])([-1,-1])(colonna_3D), T([1,2])([23,-1])(colonna_3D), T([1,2])([-1,23])(colonna_3D), T([1,2])([23,23])(colonna_3D)])
#modello 3d mancante del piano terra e de
modello_3D = STRUCT(NN(5)([T(3)(5),scheletro_primo_piano_3D]))
#modello completo
modello_3D = STRUCT([colonne_3D,modello_3D,scheletro_primo_piano_3D, bordi_3D, T(3)(34)(floor_3D), COLOR([0.84,0.84,0.84])(T(3)(-1)(tappo_3D))])

VIEW(modello_3D)
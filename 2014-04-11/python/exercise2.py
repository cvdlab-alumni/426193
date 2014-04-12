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
tappo0 = T([1,2,3])([-5,-5,-1])(CUBOID([33,33,0.5]))
tappo1 = T([1,2,3])([-6,-5,-1.5])(CUBOID([35,33,0.5]))
tappo2 = T([1,2,3])([-7,-5,-2])(CUBOID([37,33,0.5]))
tappo3 = T([1,2,3])([-8,-5,-2.5])(CUBOID([39,33,0.5]))
tappo4 = T([1,2,3])([-9,-5,-3])(CUBOID([41,33,0.5]))
tappo5 = T([1,2,3])([-10,-5,-3.5])(CUBOID([43,33,0.5]))
tappo6 = T([1,2,3])([-11,-5,-4])(CUBOID([45,33,0.5]))
tappo7 = T([1,2,3])([-12,-5,-4.5])(CUBOID([47,33,0.5]))
tappo8 = T([1,2,3])([-13,-5,-5])(CUBOID([49,33,0.5]))
tappo9 = T([1,2,3])([-14,-5,-5.5])(CUBOID([51,33,0.5]))
ovest = T(1)(23)(ROTATE([1,2])(PI/2)(nord_3D))
sud = T([1,2])([23,23])(ROTATE([1,2])(PI)(nord_3D))
est = T(1)(23)(ROTATE([1,2])(PI/2)(sud))
scheletro_primo_piano_3D = STRUCT([nord_3D, ovest, est, sud, T(3)(4)(floor_3D)])
tappi = COLOR([0.85,0.74,0.67])(STRUCT([tappo0,tappo1,tappo2,tappo3,tappo4,tappo5,tappo6,tappo7,tappo8,tappo9])) #
#COLONNA 3D PER RIEMPIRE GLI ANGOLI & colonne
colonna_3D = CUBOID([1,1,35])
colonne_3D = STRUCT([T([1,2])([-1,-1])(colonna_3D), T([1,2])([23,-1])(colonna_3D), T([1,2])([-1,23])(colonna_3D), T([1,2])([23,23])(colonna_3D)])
#modello 3d mancante del piano terra e de
modello_3D = STRUCT(NN(5)([T(3)(5),scheletro_primo_piano_3D]))
#modello completo
modello_3D = STRUCT([colonne_3D,modello_3D,scheletro_primo_piano_3D, bordi_3D, COLOR([0.84,0.84,0.84])(T(3)(34)(floor_3D)),tappi])

###########################EDIFICIO PICCOLO########################################

nord_verts_b = [[0,0],[18,0],[18,5],[0,5]]
nord_b = JOIN(AA(MK)(nord_verts_b))
porta_verts_b = [[0.5,0],[0.5,2],[2.5,2],[2.5,0]]
porta_b = JOIN(AA(MK)(porta_verts_b))
parte_superiore_arcata_b = MAP(disk2D)(domain2D)
arcata_b = STRUCT([porta_b,(T([1,2])([1.5, 2]))(parte_superiore_arcata_b)])
tantiArchi_b = T(1)(-2.5)(STRUCT(NN(7)([T(1)(2.5),arcata_b])))
tanti_archi_3D_b_colorati = COLOR([0.68,0.82,0.96])(ROTATE([2,3])(PI/2)(PROD([tantiArchi_b, Q(1)]))) #colore alternativo [0,0.51,0.51]
#bordo superiore 3D
bordo_verts_b = [[0,0],[18,0],[0,5],[18,5]]
bordo_b = PROD([JOIN(AA(MK)(bordo_verts_b)), Q(1)])
bordo_3D_b = T(3)(30)(ROTATE([2,3])(PI/2)(bordo_b))
#creazione bordi altri lati
bordo_3D_ovest_b = T(1)(18)(ROTATE([1,2])(PI/2)(bordo_3D_b))
bordo_3D_sud_b = sud = T([1,2])([18,18])(ROTATE([1,2])(PI)(bordo_3D_b))
bordo_3D_est_b = T(1)(18)(ROTATE([1,2])(PI/2)(bordo_3D_sud_b))
bordi_3D_b = STRUCT([bordo_3D_b, bordo_3D_ovest_b, bordo_3D_sud_b, bordo_3D_est_b])
#faccia mancante del pezzo sotto 3D
nord_3D_b = PROD([nord_b, Q(1)])
tanti_archi_3D_b = PROD([tantiArchi_b, Q(1)])
nord_3D_b = DIFFERENCE([nord_3D_b, tanti_archi_3D_b])
nord_3D_b = COLOR([0.84,0.84,0.84])(ROTATE([2,3])(PI/2)(nord_3D_b))
nord_3D_b = STRUCT([tanti_archi_3D_b_colorati, nord_3D_b]) #utile per colorare parte interna
#PIANO TERRA 3D
points0_b = [[0,0], [0,18], [18,0], [18,18]]
floor0_b = JOIN(AA(MK)(points0_b))
points1_b = [[5,7], [11,7], [5,16], [11,16]]
floor1_b = JOIN(AA(MK)(points1_b))
floor0_b = DIFFERENCE([floor0_b, T([1,2])([-2,-2])(floor1_b)])
floor_3D_b = PROD([floor0_b, Q(1)])
ovest_b = T(1)(18)(ROTATE([1,2])(PI/2)(nord_3D_b))
sud_b = T([1,2])([18,18])(ROTATE([1,2])(PI)(nord_3D_b))
est_b = T(1)(18)(ROTATE([1,2])(PI/2)(sud_b))
scheletro_primo_piano_3D_b = STRUCT([nord_3D_b, ovest_b, est_b, sud_b, T(3)(4)(floor_3D_b)])
 
#COLONNA 3D PER RIEMPIRE GLI ANGOLI & colonne
colonna_3D_b = CUBOID([1,1,35])
colonne_3D_b = STRUCT([T([1,2])([-1,-1])(colonna_3D_b), T([1,2])([18,-1])(colonna_3D_b), T([1,2])([-1,18])(colonna_3D_b), T([1,2])([18,18])(colonna_3D_b)])
#modello 3d mancante del piano terra e de
modello_3D_b = STRUCT(NN(5)([T(3)(5),scheletro_primo_piano_3D_b]))
#modello completo
modello_3D_b = STRUCT([COLOR([0.84,0.84,0.84])(colonne_3D_b),modello_3D_b,scheletro_primo_piano_3D_b, COLOR([0.84,0.84,0.84])(bordi_3D_b), COLOR([0.84,0.84,0.84])(T(3)(34)(floor_3D_b))])

########### ASSEMBLAGGIO PARTI#############
modello_3D = STRUCT([T([1,2])([2.5, 2.5])(modello_3D_b), COLOR([0.84,0.84,0.84])(modello_3D)])

VIEW(modello_3D)
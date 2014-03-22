from pyplasm import *

#INIZIO CREAZIONE PIANI
points0 = [[0,0], [0,23], [23,0], [23,23]]
floor0 = JOIN(AA(MK)(points0))
 
floor1 = JOIN(AA(MK)(points0)) #TRASLATO NELLA STRUCT

points2 = [[0,0,7], [0,23,7], [23,0,7], [23,23,7]]
floor2 = JOIN(AA(MK)(points2))

points3 = [[0,0,10.5], [0,23,10.5], [23,0,10.5], [23,23,10.5]]
floor3 = JOIN(AA(MK)(points3))

points4 = [[0,0,14], [0,23,14], [23,0,14], [23,23,14]]
floor4 = JOIN(AA(MK)(points4))

floor5 = JOIN(AA(MK)(points0)) #TRASLATO NELLA STRUCT
#FINE CREAZIONE PIANI

floors = STRUCT([COLOR([1.0, 0.89, 0.76])(floor0), COLOR([1.0,0.14,0.15])(T(3)(3.5)(floor1)), 
		COLOR([1.0,0.84,0.0])(floor2), COLOR([0.55,0.84,0.0])(floor3), COLOR([1.0,0.84,0.46])(floor4), 
		COLOR([1.0,0.34,0.25])(T(3)(19)(floor5))])

VIEW(floors)
from pyplasm import *

#SEMI-CIRCONFERENZA
def disk2D(p):
	u,v = p
	return [v*COS(u), v*SIN(u)]
domain2D = PROD([INTERVALS(PI)(32), INTERVALS(1)(3)])
#FINE SEMI-CIRCONFERENZA

#INIZIO PARTE ESTERNA
nord_verts = [[0,0],[23,0],[23,5],[0,5]]
nord = JOIN(AA(MK)(nord_verts))
porta_verts = [[0.5,0],[0.5,2],[2.5,2],[2.5,0]]
porta = JOIN(AA(MK)(porta_verts))
parte_superiore_arcata = MAP(disk2D)(domain2D)
arcata = STRUCT([porta,(T([1,2])([1.5, 2]))(parte_superiore_arcata)])
tanti_archi = T(1)(-2.5)(STRUCT(NN(9)([T(1)(2.5),arcata])))
centro_verts = [[4,4],[19,4],[19,19],[4,19]]
centro = PROD([JOIN(AA(MK)(centro_verts)),Q(35)])
nord = ROTATE([2,3])(PI/2)(DIFFERENCE([nord, tanti_archi]))
nord0 = T(3)(5)(nord)
nord1 = T(3)(10)(nord)
nord2 = T(3)(15)(nord)
nord3 = T(3)(20)(nord)
nord4 = T(3)(25)(nord)
#bordo_verts = [[0,0],[23,0],[23,0],[0,0]]
#bordo = PROD([JOIN(AA(MK)(bordo_verts)), Q(5)])
#bordo = T([1,3])([23,30])(ROTATE([1,2])(PI)(bordo))
#facciata_singola_nord = STRUCT([nord,nord0,nord1,nord2,nord3,nord4,bordo])
#ovest = T(1)(23)(ROTATE([1,2])(PI/2)(facciata_singola_nord))
sud = T([1,2])([23,23])(ROTATE([1,2])(PI)(facciata_singola_nord))
est = T(1)(23)(ROTATE([1,2])(PI/2)(sud))
#struttura_esterna = STRUCT([facciata_singola_nord,est,sud,ovest,centro])
#FINE PARTE ESTERNA

#INIZIO PARTE INTERNA
points0 = [[0,0], [0,23], [23,0], [23,23]]
floor0 = JOIN(AA(MK)(points0)) #TRASLATO NELLA STRUCT
floor1 = JOIN(AA(MK)(points0)) #TRASLATO NELLA STRUCT
floor2 = JOIN(AA(MK)(points0)) #TRASLATO NELLA STRUCT
floor3 = JOIN(AA(MK)(points0)) #TRASLATO NELLA STRUCT
floor4 = JOIN(AA(MK)(points0)) #TRASLATO NELLA STRUCT
floor5 = JOIN(AA(MK)(points0)) #TRASLATO NELLA STRUCT
floor6 = JOIN(AA(MK)(points0)) #TRASLATO NELLA STRUCT
floor7 = JOIN(AA(MK)(points0)) #TRASLATO NELLA STRUCT
#FINE PARTE INTERNA

#two_and_half_model = STRUCT([COLOR([0.06, 0.30, 0.54])(floor0), COLOR([0.09,0.45,0.80])(T(3)(4)(floor1)), 
		#COLOR([0.10,0.52,0.93])(T(3)(9)(floor2)), COLOR([0.11,0.56,1.0])(T(3)(14)(floor3)), COLOR([0.11,0.58,1.0])(T(3)(19)(floor4)), 
		#COLOR([0,0.60,0.80])(T(3)(24)(floor5)),COLOR([0, 0.70, 0.80])(T(3)(29)(floor6)),
		#COLOR([0,0.69,0.93])(T(3)(34)(floor7))])

#building = STRUCT([two_and_half_model, COLOR([0.79,0.69,0.56])(struttura_esterna)])

### INIZIO 3D ###
floor7_3D = PROD([floor7, Q(1)])
floor6_3D = PROD([floor6, Q(1)])
floor5_3D = PROD([floor5, Q(1)])
floor4_3D = PROD([floor4, Q(1)])
floor3_3D = PROD([floor3, Q(1)])
floor2_3D = PROD([floor2, Q(1)])
floor1_3D = PROD([floor1, Q(1)])
floor0_3D = PROD([floor0, Q(1)])

two_and_half_model_3D = STRUCT([(T(3)(34)(floor7_3D)),(T(3)(29)(floor6_3D)),(T(3)(24)(floor5_3D)),(T(3)(19)(floor4_3D)),(T(3)(14)(floor3_3D)),(T(3)(9)(floor2_3D)),(T(3)(4)(floor1_3D)),floor0_3D])

#building = STRUCT([struttura_esterna, two_and_half_model_3D])

bordo_verts = [[0,0],[23,0],[0,5],[23,5]]
bordo = PROD([JOIN(AA(MK)(bordo_verts)), Q(1)])
bordo_3D = T([1,3])([23,30])(ROTATE([2,3])(PI/2)(bordo))
tanti_archi_3D = PROD([tanti_archi, Q(1)])
est_3D = PROD([est, Q(1)])
nord_3D = PROD([nord, Q(1)])
nord_3D = ROTATE([2,3])(PI/2)(DIFFERENCE([nord_3D, tanti_archi_3D]))
nord0_3D = T(3)(5)(nord_3D)
nord1_3D = T(3)(10)(nord_3D)
nord2_3D = T(3)(15)(nord_3D)
nord3_3D = T(3)(20)(nord_3D)
nord4_3D = T(3)(25)(nord_3D)
facciata_singola_nord_3D = STRUCT([nord_3D, nord0_3D,nord1_3D, nord2_3D,nord3_3D,nord4_3D])
ovest_3D = T(1)(23)(ROTATE([1,2])(PI/2)(facciata_singola_nord_3D))
sud_3D = T([1,2])([23,23])(ROTATE([1,2])(PI)(facciata_singola_nord_3D))
est_3D = T(1)(23)(ROTATE([1,2])(PI/2)(sud_3D))
struttura_esterna_3D = STRUCT([facciata_singola_nord_3D,est_3D,sud_3D,ovest_3D, centro,bordo_3D])



VIEW(nord_3D)
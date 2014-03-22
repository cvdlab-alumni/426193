from pyplasm import *

dom1D = INTERVALS(1)(1)
dom3D = INSR(PROD)([INTERVALS(2*PI)(22), dom1D, dom1D])

def spiral1(p):
	alpha,r,h = p
	return [r*COS(alpha), r*SIN(alpha), alpha/(2*PI)]

def spiral2(p):
	alpha,r,h = p
	return [r*COS(alpha), r*SIN(alpha), alpha/(2*PI) + 0.1]


obj1 = MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D)
obj2 = T(3)(1)(MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D))
obj3 = T(3)(2)(MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D))
obj4 = T(3)(3)(MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D))
obj5 = T(3)(4)(MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D))
obj6 = T(3)(5)(MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D))
obj7 = T(3)(6)(MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D))
obj8 = T(3)(7)(MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D))
obj9 = T(3)(8)(MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D))
obj10 = T(3)(9)(MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D))
obj11 = T(3)(10)(MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D))
obj12 = T(3)(11)(MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D))
obj13 = T(3)(12)(MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D))
obj14 = T(3)(13)(MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D))

scale = T([1,2])([11.5,11.5])(STRUCT([obj1,obj2,obj3,obj4,obj5,obj6,obj7,obj8,obj9,obj10,obj11,obj12,obj13,obj14]))

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

#parete = DIFFERENCE([nord, tantiArchi])
nord = ROTATE([2,3])(PI/2)(DIFFERENCE([nord, tantiArchi]))
nord0 = T(3)(5)(nord)
nord1 = T(3)(10)(nord)
nord2 = T(3)(15)(nord)
nord3 = T(3)(20)(nord)
nord4 = T(3)(25)(nord)
bordo_verts = [[0,0],[23,0],[23,0],[0,0]]
bordo = PROD([JOIN(AA(MK)(bordo_verts)), Q(5)])
bordo = T([1,3])([23,30])(ROTATE([1,2])(PI)(bordo))
facciata_singola = STRUCT([nord,nord0,nord1,nord2,nord3,nord4,bordo])
ovest = T(1)(23)(ROTATE([1,2])(PI/2)(facciata_singola))
sud = T([1,2])([23,23])(ROTATE([1,2])(PI)(facciata_singola))
est = T(1)(23)(ROTATE([1,2])(PI/2)(sud))
struttura_esterna = STRUCT([facciata_singola,est,sud,ovest])

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

two_and_half_model = STRUCT([COLOR([0.06, 0.30, 0.54])(floor0), COLOR([0.09,0.45,0.80])(T(3)(5)(floor1)), 
		COLOR([0.10,0.52,0.93])(T(3)(10)(floor2)), COLOR([0.11,0.56,1.0])(T(3)(15)(floor3)), COLOR([0.11,0.58,1.0])(T(3)(20)(floor4)), 
		COLOR([0,0.60,0.80])(T(3)(25)(floor5)),COLOR([0, 0.70, 0.80])(T(3)(30)(floor6)),
		COLOR([0,0.69,0.93])(T(3)(35)(floor7))])

mock_up_3D = STRUCT([two_and_half_model, COLOR([0.79,0.69,0.56])(struttura_esterna), scale])


VIEW(mock_up_3D)
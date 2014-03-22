from pyplasm import *

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

VIEW(two_and_half_model)
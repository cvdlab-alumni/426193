from pyplasm import *
from larcc import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])
number = 0
GRID = COMP([INSR(PROD),AA(QUOTE)])

casa = assemblyDiagramInit([11,7,1])([[1,7,1,3,1,2,1,4,1,8,1],[1,5,1,2,1,8,1],[4]])
V,CV = casa
casa_hpc = SKEL_1(STRUCT(MKPOLS(casa)))
casa_hpc = cellNumbering (casa,casa_hpc)(range(len(casa[1])),CYAN,2)

toRemove = [8,9,10,12,31,22,24,25,26,29,31,36,38,40,45,47,50,52,54,61,64,65,66,68]
casa = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
toMerge = 15
porta_cucina = assemblyDiagramInit([1,3,2])([[1],[3,2,3],[3,1]])
casa = diagram2cell(porta_cucina,casa,toMerge)
toMerge = 13
porta_camera = assemblyDiagramInit([1,2,2])([[1],[1.5,6.5],[3,1]])
casa = diagram2cell(porta_camera,casa,toMerge)
toMerge = 24
porta_cameretta = assemblyDiagramInit([2,1,2])([[0.5,1.5],[1],[3,1]])
casa = diagram2cell(porta_cameretta,casa,toMerge)
toMerge = 19
porta_cameretta = assemblyDiagramInit([1,1,2])([[1],[1],[3,1]])
casa = diagram2cell(porta_cameretta,casa,toMerge)
toMerge = 31
porta_bagno = assemblyDiagramInit([3,1,2])([[1.5,1.5,1],[1],[3,1]])
casa = diagram2cell(porta_bagno,casa,toMerge)
toMerge = 36
porta_camera2 = assemblyDiagramInit([1,2,2])([[1],[1.5,6.5],[3,1]])
casa = diagram2cell(porta_camera2,casa,toMerge)
toMerge = 20
porta_sala = assemblyDiagramInit([1,3,2])([[1],[2,3,3],[3,1]])
casa = diagram2cell(porta_sala,casa,toMerge)
toMerge = 17
porta_muro = assemblyDiagramInit([3,1,2])([[0.5,2,0.5],[1],[3,1]])
casa = diagram2cell(porta_muro,casa,toMerge)
toMerge = 5
finestra_cucina = assemblyDiagramInit([1,3,3])([[1],[2,4,2],[1.5,1.5,1]])
casa = diagram2cell(finestra_cucina,casa,toMerge)
toMerge = 6
finestra_camera = assemblyDiagramInit([3,1,3])([[1.5,1,1.5],[1],[1.5,1,1.5]])
casa = diagram2cell(finestra_camera,casa,toMerge)
toMerge = 13
finestra_cameretta = assemblyDiagramInit([3,1,3])([[2,2,2],[1],[1.5,1,1.5]])
casa = diagram2cell(finestra_cameretta,casa,toMerge)
toMerge = 25
finestra_bagno = assemblyDiagramInit([3,1,3])([[1.5,1,1.5],[1],[1.5,1,1.5]])
casa = diagram2cell(finestra_bagno,casa,toMerge)
toMerge = 32
finestra_camera2 = assemblyDiagramInit([3,1,3])([[1.5,1,1.5],[1],[1.5,1,1.5]])
casa = diagram2cell(finestra_camera2,casa,toMerge)
toMerge = 33
finestra_sala = assemblyDiagramInit([3,1,3])([[3,9,4],[1],[1.5,1.5,1]])
casa = diagram2cell(finestra_sala,casa,toMerge)
toRemove = [42,48,50,54,58,64,68,74,82,88,91,97,100,103,106,109,115,121,124,127]
casa = casa[0], [cell for k,cell in enumerate(casa[1]) if not (k in toRemove)]
casa_hpc = SKEL_1(STRUCT(MKPOLS(casa)))
casa_hpc = cellNumbering (casa,casa_hpc)(range(len(casa[1])),CYAN,2)
#VIEW(casa_hpc)
#DRAW(casa)
casa = STRUCT(MKPOLS(casa))
#VIEW(casa)
############## VETRI ####################
glass_camera = MATERIAL([1,1,1,0.1,  0,0,0.8,0.5,  1,1,1,0.1, 0,0,0,0.1, 100])(GRID([[28],[0.6],[1]]))
glass_cucina = R([1,2])(PI/2)(MATERIAL([1,1,1,0.1,  0,0,0.8,0.5,  1,1,1,0.1, 0,0,0,0.1, 100])(GRID([[5],[0.6],[1.5]])))
glass_sala = MATERIAL([1,1,1,0.1,  0,0,0.8,0.5,  1,1,1,0.1, 0,0,0,0.1, 100])(GRID([[8],[0.6],[1.5]]))
solido = STRUCT([casa, T([1,2,3])([1,0.2,1.5])(glass_camera), T([1,2,3])([0.8,11,1.5])(glass_cucina), T([1,2,3,])([20,18.2,1.5])(glass_sala)])
############## FINE VETRI ####################
############## PORTE ####################
porta_ingresso = (CUBOID([2,0.6,3]))
porta_cameretta =(CUBOID([1.5,0.6,3]))
porta_bagno = (CUBOID([1.5,0.6,3]))
porta_camera = R([1,2])(PI/2)(CUBOID([1.6,0.6,3]))
porta_camera2 = R([1,2])(PI/2)(CUBOID([1.6,0.6,3]))
porta_cucina = R([1,2])(PI/2)(CUBOID([2,0.6,3]))
porta_sala = R([1,2])(PI/2)(CUBOID([3,0.6,3]))
porte = STRUCT([T([1,2])([9.5,18.2])(porta_ingresso), T([1,2])([12,6.2])(porta_cameretta),T([1,2])([17.5,6.2])(porta_bagno), T([1,2])([8.8,7.4])(porta_camera),
   T([1,2])([20.8,7.4])(porta_camera2), T([1,2])([8.8,13])(porta_cucina), T([1,2])([12.8,12])(porta_sala)])
porte = STRUCT([COLOR([0.42,0.27,0.08])(porte)])
############## FINE PORTE ####################
solido = STRUCT([porte, solido])
#VIEW(solido)

####################### INIZIO SCALE PAVIMENTO E TETTO ########################
solido = T(3)(0.5)(STRUCT([solido]))
zerbino = T([1,2])([9,19])(CUBOID([3,3,0.5]))
pavimento = CUBOID([30,19,0.5])
zerbino_traslato = T([1,2])([6.5,19])(CUBOID([3,3,0.5]))
solido = STRUCT([solido, pavimento, T(3)(4)(pavimento), zerbino])
scala_a = T(3)(-0.5)(STRUCT(NN(5)([T([1,3])([-0.5,0.5]),zerbino_traslato])))
pezzo_mancante = T([1,2,3])([4,22,2])(CUBOID([4,3,0.5]))
scala_b = T([2,3])([3,2])(STRUCT(NN(5)([T([1,3])([0.5,0.5]),zerbino_traslato])))
scale = STRUCT([scala_a,scala_b,pezzo_mancante])
scale = STRUCT([scale, T([3])([4.5])(scale)])
####################FINE SCALE PAVIMENTO E TETTO #########################
palazzo = STRUCT([solido, T(3)(4.5)(solido), T(3)(9)(solido),scale])
#VIEW(palazzo)
#################### COPERTURA SCALE ####################
copertura_scale1 = T([1,2,3])([4,25,4])(MATERIAL([1,1,1,0.1,  0,0,0.8,0.5,  1,1,1,0.1, 0,0,0,0.1, 100])(GRID([[8.4],[0.4],[9]])))
copertura_scale2 = T([1,2])([4,19])(MATERIAL([1,1,1,0.1,  0,0,0.8,0.5,  1,1,1,0.1, 0,0,0,0.1, 100])(GRID([[0.4],[6],[13]])))
copertura_scale3 = T([1,2])([12,19])(MATERIAL([1,1,1,0.1,  0,0,0.8,0.5,  1,1,1,0.1, 0,0,0,0.1, 100])(GRID([[0.4],[6],[13]])))
copertura_superiore = T([1,2,3])([4,18.9,13])(MATERIAL([1,1,1,0.1,  0,0,0.8,0.5,  1,1,1,0.1, 0,0,0,0.1, 100])(GRID([[8.4],[6.5],[0.1]])))
coperture = STRUCT([copertura_scale1,copertura_scale3,copertura_scale2, copertura_superiore])
#################### FINE COPERTURA SCALE #################### 
palazzo = STRUCT([palazzo,coperture])
#################### GRONDAIA ####################
dominio = INTERVALS(1)(20)
grondaia = BEZIER(S1)([[2.25, 3.57], [2.26, 3.05], [2.71, 3.06], [2.75, 3.56]]) 
grondaia_map = MAP(grondaia)(dominio)
grondaia_map12 = R([2,3])(PI/2)(PROD([grondaia_map ,Q(20)]))
grondaia_map_1 = T([1,2,3])([-2.8,19.5,10])(grondaia_map12)
grondaia_map_2 = T([1,2,3])([27.8,19.5,10])(grondaia_map12)
grondaia_map_3 = R([2,3])(PI/2)(PROD([grondaia_map ,Q(31)]))
grondaia_map_3 = T([1,2,3])([-0.5,-2.8,10])(R([1,2])(PI/2)(grondaia_map_3))
grondaia_map_4 = T(2)(19.6)(grondaia_map_3)
discendente_1 = T([1,2])([5,-3.7])(PROD([grondaia_map ,Q(13.5)]))
discendente_2 = T([1,2,3])([7,18.8,13.5])(R([2,3])(PI)(discendente_1))
grondaie = STRUCT([grondaia_map_1, grondaia_map_2, grondaia_map_3, grondaia_map_4, discendente_1,discendente_2])
#################### FINE GRONDAIA ####################
palazzo = STRUCT([palazzo, COLOR(BLUE)(grondaie)])
#################### ERBA ####################
erba = BEZIER(S1)([[0.27, 2.61], [1.5, 4.95], [8.29, 1.68], [10.65, 4.43]])
erba_map = MAP(erba)(dominio)
erba_map_prima = R([2,3])(PI/2)(PROD([erba_map ,Q(0.2)]))
erba_map_prima = COLOR(GREEN)(T([3])([-3.5])(erba_map_prima))
erba_map = (STRUCT(NN(30)([T([1,2])([0,0.3]),erba_map_prima])))
erba_map = R([1,2])(PI/2)(erba_map)
erba_map_lato1 = T([2])(10)(erba_map)
erba_map_lato2 = T([1,2])([39,-11])(R([1,2])(PI/2)(STRUCT(NN(160)([T([1,2])([0,0.3]),erba_map_prima]))))
erba_mapLato = T(2)(-1)(STRUCT([erba_map, erba_map_lato1]))
erba_mapLato2 = T(1)(39)(erba_mapLato)
erba_map_lato3 = T(2)(30)(erba_map_lato2)
prato = STRUCT([erba_mapLato,erba_mapLato2, erba_map_lato2, erba_map_lato3])
#################### FINE ERBA ####################
#VIEW(erba)

palazzo = STRUCT([palazzo, prato])

VIEW(palazzo)
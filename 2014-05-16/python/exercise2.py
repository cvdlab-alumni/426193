from pyplasm import *
from larcc import *

def cellNumberingModificato (larModel,hpcModel):
   V,CV = larModel
   def cellNumbering (cellSubset,color=WHITE,scalingFactor=1,start=0):
      text = TEXTWITHATTRIBUTES (TEXTALIGNMENT='centre', TEXTANGLE=0, 
                     TEXTWIDTH=0.1*scalingFactor, 
                     TEXTHEIGHT=0.2*scalingFactor, 
                     TEXTSPACING=0.025*scalingFactor)
      hpcList = [hpcModel]
      for cell in cellSubset:
         point = CCOMB([V[v] for v in CV[cell]])
         hpcList.append(T([1,2,3])(point)(COLOR(color)(text(str(cell+start)))))
      return STRUCT(hpcList)
   return cellNumbering

DRAW = COMP([VIEW,STRUCT,MKPOLS])
number = 0

##################################cucina_camera
cucina_camera = assemblyDiagramInit([3,5,1])([[1,7,1],[1,8,1,8,1],[4]])
V,CV = cucina_camera
cucina_camera_hpc = SKEL_1(STRUCT(MKPOLS(cucina_camera)))
cucina_camera_hpc = cellNumberingModificato (cucina_camera,cucina_camera_hpc)(range(len(CV)),CYAN,2)
#number = number + len(CV)
#VIEW(cucina_camera_hpc)

toRemove = [6,8]
cucina_camera = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(cucina_camera)

cucina_camera_hpc = SKEL_1(STRUCT(MKPOLS(cucina_camera)))
cucina_camera_hpc = cellNumbering (cucina_camera,cucina_camera_hpc)(range(len(cucina_camera[1])),CYAN,2)
#VIEW(cucina_camera_hpc)

toMerge = 11
porta_cucina = assemblyDiagramInit([1,3,2])([[1],[3,2,3],[3,1]])
cucina_camera = diagram2cell(porta_cucina,cucina_camera,toMerge)
cucina_camera_hpc = SKEL_1(STRUCT(MKPOLS(cucina_camera)))
cucina_camera_hpc = cellNumbering (cucina_camera,cucina_camera_hpc)(range(len(cucina_camera[1])),CYAN,2)
#VIEW(cucina_camera_hpc)

toRemove = [14]
cucina_camera = cucina_camera[0], [cell for k,cell in enumerate(cucina_camera[1]) if not (k in toRemove)]
#DRAW(cucina_camera)

toMerge = 9
porta_cucina = assemblyDiagramInit([1,2,2])([[1],[6.5,1.5],[3,1]])
cucina_camera = diagram2cell(porta_cucina,cucina_camera,toMerge)
cucina_camera_hpc = SKEL_1(STRUCT(MKPOLS(cucina_camera)))
cucina_camera_hpc = cellNumbering (cucina_camera,cucina_camera_hpc)(range(len(cucina_camera[1])),CYAN,2)
#VIEW(cucina_camera_hpc)

toRemove = [18]
cucina_camera = cucina_camera[0], [cell for k,cell in enumerate(cucina_camera[1]) if not (k in toRemove)]
#DRAW(cucina_camera)

toMerge = 5
finestra_camera = assemblyDiagramInit([3,1,3])([[1.5,1,1.5],[1],[1.5,1,1.5]])
cucina_camera = diagram2cell(finestra_camera,cucina_camera,toMerge)
cucina_camera_hpc = SKEL_1(STRUCT(MKPOLS(cucina_camera)))
cucina_camera_hpc = cellNumbering (cucina_camera,cucina_camera_hpc)(range(len(cucina_camera[1])),CYAN,2)
#VIEW(cucina_camera_hpc)

toRemove = [19,22]
cucina_camera = cucina_camera[0], [cell for k,cell in enumerate(cucina_camera[1]) if not (k in toRemove)]
#DRAW(cucina_camera)

toMerge = 3
finestra_camera = assemblyDiagramInit([1,3,3])([[1],[2,4,2],[1.5,1.5,1]])
cucina_camera = diagram2cell(finestra_camera,cucina_camera,toMerge)
cucina_camera_hpc = SKEL_1(STRUCT(MKPOLS(cucina_camera)))
cucina_camera_hpc = cellNumbering (cucina_camera,cucina_camera_hpc)(range(len(cucina_camera[1])),CYAN,2)
#VIEW(cucina_camera_hpc)

toRemove = [28]
cucina_camera = cucina_camera[0], [cell for k,cell in enumerate(cucina_camera[1]) if not (k in toRemove)]
#DRAW(cucina_camera)

###########################bagno_camera
bagno_camera = assemblyDiagramInit([3,3,1])([[6,1,4],[1,5,1],[4]])
V,CV = bagno_camera
bagno_camera_hpc = SKEL_1(STRUCT(MKPOLS(bagno_camera)))
bagno_camera_hpc = cellNumberingModificato (bagno_camera,bagno_camera_hpc)(range(len(CV)),CYAN,2)
#number = number + len(CV)
#VIEW(bagno_camera_hpc)

toRemove = [1,7]
bagno_camera = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(bagno_camera)

bagno_camera_hpc = SKEL_1(STRUCT(MKPOLS(bagno_camera)))
bagno_camera_hpc = cellNumbering (bagno_camera,bagno_camera_hpc)(range(len(bagno_camera[1])),CYAN,2)
#VIEW(bagno_camera_hpc)

toMerge = 1
porta_bagno = assemblyDiagramInit([3,1,2])([[3,1.5,1.5],[1],[3,1]])
bagno_camera = diagram2cell(porta_bagno,bagno_camera,toMerge)
bagno_camera_hpc = SKEL_1(STRUCT(MKPOLS(bagno_camera)))
bagno_camera_hpc = cellNumbering (bagno_camera,bagno_camera_hpc)(range(len(bagno_camera[1])),CYAN,2)
#VIEW(bagno_camera_hpc)

toRemove = [8]
bagno_camera = bagno_camera[0], [cell for k,cell in enumerate(bagno_camera[1]) if not (k in toRemove)]
#DRAW(bagno_camera)

toMerge = 5
porta_bagno = assemblyDiagramInit([3,1,2])([[1.5,1.5,1],[1],[3,1]])
bagno_camera = diagram2cell(porta_bagno,bagno_camera,toMerge)
bagno_camera_hpc = SKEL_1(STRUCT(MKPOLS(bagno_camera)))
bagno_camera_hpc = cellNumbering (bagno_camera,bagno_camera_hpc)(range(len(bagno_camera[1])),CYAN,2)
#VIEW(bagno_camera_hpc)

toRemove = [12]
bagno_camera = bagno_camera[0], [cell for k,cell in enumerate(bagno_camera[1]) if not (k in toRemove)]
#DRAW(bagno_camera)

toMerge = 0
porta_bagno = assemblyDiagramInit([3,1,3])([[2,2,2],[1],[1.5,1,1.5]])
bagno_camera = diagram2cell(porta_bagno,bagno_camera,toMerge)
bagno_camera_hpc = SKEL_1(STRUCT(MKPOLS(bagno_camera)))
bagno_camera_hpc = cellNumbering (bagno_camera,bagno_camera_hpc)(range(len(bagno_camera[1])),CYAN,2)
#VIEW(bagno_camera_hpc)

toRemove = [18]
bagno_camera = bagno_camera[0], [cell for k,cell in enumerate(bagno_camera[1]) if not (k in toRemove)]
#DRAW(bagno_camera)

toMerge = 3
porta_bagno = assemblyDiagramInit([3,1,3])([[1.5,1,1.5],[1],[1.5,1,1.5]])
bagno_camera = diagram2cell(porta_bagno,bagno_camera,toMerge)
bagno_camera_hpc = SKEL_1(STRUCT(MKPOLS(bagno_camera)))
bagno_camera_hpc = cellNumbering (bagno_camera,bagno_camera_hpc)(range(len(bagno_camera[1])),CYAN,2)
#VIEW(bagno_camera_hpc)

toRemove = [22]
bagno_camera = bagno_camera[0], [cell for k,cell in enumerate(bagno_camera[1]) if not (k in toRemove)]
#DRAW(bagno_camera)

###################################camera
camera = assemblyDiagramInit([3,2,1])([[1,8,1],[1,8],[4]])
V,CV = camera
camera_hpc = SKEL_1(STRUCT(MKPOLS(camera)))
camera_hpc = cellNumberingModificato (camera,camera_hpc)(range(len(CV)),CYAN,2)
#number = number + len(CV)
#VIEW(camera_hpc)

toRemove = [3]
camera = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(camera)

camera_hpc = SKEL_1(STRUCT(MKPOLS(camera)))
camera_hpc = cellNumbering (camera,camera_hpc)(range(len(camera[1])),CYAN,2)
#VIEW(camera_hpc)

toMerge = 1
porta_camera = assemblyDiagramInit([1,2,2])([[1],[6.5,1.5],[3,1]])
camera = diagram2cell(porta_camera,camera,toMerge)
camera_hpc = SKEL_1(STRUCT(MKPOLS(camera)))
camera_hpc = cellNumbering (camera,camera_hpc)(range(len(camera[1])),CYAN,2)
#VIEW(camera_hpc)

toRemove = [6]
camera = camera[0], [cell for k,cell in enumerate(camera[1]) if not (k in toRemove)]
#DRAW(camera)

toMerge = 1
porta_camera = assemblyDiagramInit([3,1,3])([[1.5,1,1.5],[1],[1.5,1,1.5]])
camera = diagram2cell(porta_camera,camera,toMerge)
camera_hpc = SKEL_1(STRUCT(MKPOLS(camera)))
camera_hpc = cellNumbering (camera,camera_hpc)(range(len(camera[1])),CYAN,2)
#VIEW(camera_hpc)

toRemove = [7,13]
camera = camera[0], [cell for k,cell in enumerate(camera[1]) if not (k in toRemove)]
#DRAW(camera)

######################################sala
sala = assemblyDiagramInit([3,3,1])([[1,16,1],[1,8,1],[4]])
V,CV = sala
sala_hpc = SKEL_1(STRUCT(MKPOLS(sala)))
sala_hpc = cellNumberingModificato (sala,sala_hpc)(range(len(CV)),CYAN,2)
#number = number + len(CV)
#VIEW(sala_hpc)

toRemove = [4]
sala = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(sala)

sala_hpc = SKEL_1(STRUCT(MKPOLS(sala)))
sala_hpc = cellNumbering (sala,sala_hpc)(range(len(sala[1])),CYAN,2)
#VIEW(sala_hpc)

toMerge = 1
porta_sala = assemblyDiagramInit([1,3,2])([[1],[2,3,3],[3,1]])
sala = diagram2cell(porta_sala,sala,toMerge)
sala_hpc = SKEL_1(STRUCT(MKPOLS(sala)))
sala_hpc = cellNumbering (sala,sala_hpc)(range(len(sala[1])),CYAN,2)
#VIEW(sala_hpc)

toRemove = [9]
sala = sala[0], [cell for k,cell in enumerate(sala[1]) if not (k in toRemove)]
#DRAW(sala)

toMerge = 3
porta_sala = assemblyDiagramInit([3,1,3])([[3,9,4],[1],[1.5,1.5,1]])
sala = diagram2cell(porta_sala,sala,toMerge)
sala_hpc = SKEL_1(STRUCT(MKPOLS(sala)))
sala_hpc = cellNumbering (sala,sala_hpc)(range(len(sala[1])),CYAN,2)
#VIEW(sala_hpc)

toRemove = [15]
sala = sala[0], [cell for k,cell in enumerate(sala[1]) if not (k in toRemove)]
#DRAW(sala)

####################################muro
muro = assemblyDiagramInit([1,1,1])([[3],[1],[4]])
V,CV = muro
muro_hpc = SKEL_1(STRUCT(MKPOLS(muro)))
muro_hpc = cellNumberingModificato (muro,muro_hpc)(range(len(CV)),CYAN,2)
#number = number + len(CV)
#VIEW(muro_hpc)

muro_hpc = SKEL_1(STRUCT(MKPOLS(muro)))
muro_hpc = cellNumbering (muro,muro_hpc)(range(len(muro[1])),CYAN,2)
#VIEW(muro_hpc)

toMerge = 0
porta_muro = assemblyDiagramInit([3,1,2])([[0.5,2,0.5],[1],[3,1]])
muro = diagram2cell(porta_muro,muro,toMerge)
muro_hpc = SKEL_1(STRUCT(MKPOLS(muro)))
muro_hpc = cellNumbering (muro,muro_hpc)(range(len(muro[1])),CYAN,2)
#VIEW(muro_hpc)

toRemove = [2]
muro = muro[0], [cell for k,cell in enumerate(muro[1]) if not (k in toRemove)]
#DRAW(muro)
######################fine muro

scheletro = STRUCT([cucina_camera_hpc, T(1)(9)(bagno_camera_hpc), T(1)(20)(camera_hpc), T([1,2])([9,18])(muro_hpc), T([1,2])([12,9])(sala_hpc)])

#VIEW(scheletro)

cucina_camera = STRUCT(MKPOLS(cucina_camera))
bagno_camera = T(1)(9)(STRUCT(MKPOLS(bagno_camera)))
camera = T(1)(20)(STRUCT(MKPOLS(camera)))
muro = T([1,2])([9,18])(STRUCT(MKPOLS(muro)))
sala = T([1,2])([12,9])(STRUCT(MKPOLS(sala)))

solido = T(3)(0.5)(STRUCT([cucina_camera, bagno_camera, camera, muro, sala]))
zerbino = T([1,2])([9,19])(CUBOID([3,3,0.5]))
pavimento = CUBOID([30,19,0.5])
zerbino_traslato = T([1,2])([6.5,19])(CUBOID([3,3,0.5]))
solido = STRUCT([solido, pavimento, T(3)(4)(pavimento), zerbino])
scala_a = T(3)(-0.5)(STRUCT(NN(5)([T([1,3])([-0.5,0.5]),zerbino_traslato])))
pezzo_mancante = T([1,2,3])([4,22,2])(CUBOID([4,3,0.5]))
scala_b = T([2,3])([3,2])(STRUCT(NN(5)([T([1,3])([0.5,0.5]),zerbino_traslato])))
scale = STRUCT([scala_a,scala_b,pezzo_mancante])

scale = STRUCT([scale, T([3])([4.5])(scale)])
palazzo = COLOR([0.89,0.89,0.88])(STRUCT([solido, T(3)(4.5)(solido), T(3)(9)(solido)]))
palazzo = COLOR([1,0.84,0])(STRUCT([scale,palazzo]))
copertura_scale1 = T([1,2])([4,25])(CUBOID([8,0.4,13]))
copertura_scale1_diff = T([1,2])([10,25])(CUBOID([2,0.4,3]))
copertura_scale1 = DIFFERENCE([copertura_scale1, copertura_scale1_diff])
copertura_scale2 = T([1,2])([4,19])(CUBOID([0.4,6,13]))
copertura_scale3 = T([1,2])([12,19])(CUBOID([0.4,6.5,13]))

coperture = STRUCT([copertura_scale1,copertura_scale3,copertura_scale2])
palazzo = STRUCT([palazzo, coperture])



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

palazzo = STRUCT([COLOR([1,0.84,0])(palazzo), COLOR(BLUE)(grondaie)])

pavimentazione = BEZIER(S1)([[0.27, 2.61], [1.5, 4.95], [8.29, 1.68], [10.65, 4.43]])
pavimentazione_map = MAP(pavimentazione)(dominio)
pavimentazione_map_prima = R([2,3])(PI/2)(PROD([pavimentazione_map ,Q(0.2)]))
pavimentazione_map_prima = COLOR(GREEN)(T([3])([-3.5])(pavimentazione_map_prima))
pavimentazione_map = (STRUCT(NN(30)([T([1,2])([0,0.3]),pavimentazione_map_prima])))
pavimentazione_map = R([1,2])(PI/2)(pavimentazione_map)
pavimentazione_map_lato1 = T([2])(10)(pavimentazione_map)
pavimentazione_map_lato2 = T([1,2])([39,-11])(R([1,2])(PI/2)(STRUCT(NN(160)([T([1,2])([0,0.3]),pavimentazione_map_prima]))))

pavimentazione_mapLato = T(2)(-1)(STRUCT([pavimentazione_map, pavimentazione_map_lato1]))
pavimentazione_mapLato2 = T(1)(39)(pavimentazione_mapLato)

pavimentazione_map_lato3 = T(2)(30)(pavimentazione_map_lato2)

pavimentazioni = STRUCT([pavimentazione_mapLato,pavimentazione_mapLato2, pavimentazione_map_lato2, pavimentazione_map_lato3])
#VIEW(pavimentazione_map)

palazzo = STRUCT([palazzo, pavimentazioni])

VIEW(palazzo)
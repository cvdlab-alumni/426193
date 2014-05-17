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

VIEW(scheletro)


cucina_camera = STRUCT(MKPOLS(cucina_camera))
bagno_camera = T(1)(9)(STRUCT(MKPOLS(bagno_camera)))
camera = T(1)(20)(STRUCT(MKPOLS(camera)))
muro = T([1,2])([9,18])(STRUCT(MKPOLS(muro)))
sala = T([1,2])([12,9])(STRUCT(MKPOLS(sala)))

solido = STRUCT([cucina_camera, bagno_camera, camera, muro, sala])

VIEW(solido)
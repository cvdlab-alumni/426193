from pyplasm import *
from larcc import *

#SEMI-CIRCONFERENZA
def disk2D(p):
	u,v = p
	return [v*COS(u), v*SIN(u)]
domain2D = PROD([INTERVALS(PI)(32), INTERVALS(1)(3)])
#FINE SEMI-CIRCONFERENZA
def translatePoints (points, tvect):
	return [VECTSUM([p,tvect]) for p in points]

def rotatePoints (points, angle):
	a = angle
	return [[x*COS(a)-y*SIN(a), x*SIN(a)+y*COS(a)] for x,y in points]

def scalePoints (points, svect):
	return [AA(PROD)(TRANS([p,svect])) for p in points]

def translatePoints (points, tvect):
	return [VECTSUM([p,tvect]) for p in points]

def rotatePoints (points, angle):
	a = angle
	return [[x*COS(a)-y*SIN(a), x*SIN(a)+y*COS(a)] for x,y in points]

def scalePoints (points, svect):
	return [AA(PROD)(TRANS([p,svect])) for p in points]

def larDomain(shape):
	V,CV = larSimplexGrid(shape)
	V = scalePoints(V, [1./d for d in shape])
	return V,CV

def larIntervals(shape):
	def larIntervals0(size):
		V,CV = larDomain(shape)
		V = scalePoints(V, [scaleFactor for scaleFactor in size])
		return V,CV
	return larIntervals0

def larMap(coordFuncs):
	def larMap0(domain):
		V,CV = domain
		V = TRANS(CONS(coordFuncs)(V))
		return V,CV
	return larMap0

def larCircle(radius=1.):
	def larCircle0(shape=36):
		domain = larIntervals([shape])([2*PI])
		V,CV = domain
		x = lambda coords : [radius*COS(p[0]) for p in V]
		y = lambda coords : [radius*SIN(p[0]) for p in V]
		return larMap([x,y])(domain)
	return larCircle0

def larDisk(radius=1.):
	def larDisk0(shape=[36,1]):
		domain = larIntervals(shape)([2*PI,radius])
		V,CV = domain
		x = lambda V : [p[1]*COS(p[0]) for p in V]
		y = lambda V : [p[1]*SIN(p[0]) for p in V]
		return larMap([x,y])(domain)
	return larDisk0

def larDisk(radius=1.):
	def larDisk0(shape=[36,1]):
		domain = larIntervals(shape)([2*PI,radius])
		V,CV = domain
		x = lambda V : [p[1]*COS(p[0]) for p in V]
		y = lambda V : [p[1]*SIN(p[0]) for p in V]
		return larMap([x,y])(domain)
	return larDisk0

def larRing(params):
	r1,r2 = params
	def larRing0(shape=[36,1]):
		V,CV = larIntervals(shape)([2*PI,r2-r1])
		V = translatePoints(V,[0,r1])
		domain = V,CV
		x = lambda V : [p[1] * COS(p[0]) for p in V]
		y = lambda V : [p[1] * SIN(p[0]) for p in V]
		return larMap([x,y])(domain)
	return larRing0

def larCylinder(params):
	radius,height= params
	def larCylinder0(shape=[36,1]):
		domain = larIntervals(shape)([2*PI,1])
		V,CV = domain
		x = lambda V : [radius*COS(p[0]) for p in V]
		y = lambda V : [radius*SIN(p[0]) for p in V]
		z = lambda V : [height*p[1] for p in V]
		mapping = [x,y,z]
		model = larMap(mapping)(domain)
		return model
	return larCylinder0

def larSphere(radius=1):
	def larSphere0(shape=[18,36]):
		V,CV = larIntervals(shape)([PI,2*PI])
		V = translatePoints(V,[-PI/2,-PI])
		domain = V,CV
		x = lambda V : [radius*COS(p[0])*SIN(p[1]) for p in V]
		y = lambda V : [radius*COS(p[0])*COS(p[1]) for p in V]
		z = lambda V : [radius*SIN(p[0]) for p in V]
		return larMap([x,y,z])(domain)
	return larSphere0

def larToroidal(params):
	r,R = params
	def larToroidal0(shape=[24,36]):
		domain = larIntervals(shape)([2*PI,2*PI])
		V,CV = domain
		x = lambda V : [(R + r*COS(p[0])) * COS(p[1]) for p in V]
		y = lambda V : [(R + r*COS(p[0])) * SIN(p[1]) for p in V]
		z = lambda V : [-r * SIN(p[0]) for p in V]
		return larMap([x,y,z])(domain)
	return larToroidal0

def larCrown(params):
	r,R = params
	def larCrown0(shape=[24,36]):
		V,CV = larIntervals(shape)([PI,2*PI])
		V = translatePoints(V,[-PI/2,0])
		domain = V,CV
		x = lambda V : [(R + r*COS(p[0])) * COS(p[1]) for p in V]
		y = lambda V : [(R + r*COS(p[0])) * SIN(p[1]) for p in V]
		z = lambda V : [-r * SIN(p[0]) for p in V]
		return larMap([x,y,z])(domain)
	return larCrown0

def larBall(radius=1):
	def larBall0(shape=[18,36]):
		V,CV = checkModel(larSphere(radius)(shape))
		return V,[range(len(V))]
	return larBall0

def larBall(radius=1):
	def larBall0(shape=[18,36]):
		V,CV = checkModel(larSphere(radius)(shape))
		return V,[range(len(V))]
	return larBall0

def larRod(params):
	radius,height= params
	def larRod0(shape=[36,1]):
		V,CV = checkModel(larCylinder(params)(shape))
		return V,[range(len(V))]
	return larRod0

def larRod(params):
	radius,height= params
	def larRod0(shape=[36,1]):
		V,CV = checkModel(larCylinder(params)(shape))
		return V,[range(len(V))]
	return larRod0

###############FINITI IMPORT##########################

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
modello_3D = T(3)(5.5)(STRUCT([T([1,2])([2.5, 2.5])(modello_3D_b), COLOR([0.84,0.84,0.84])(modello_3D)]))

###########################FINE STRUTTURA CENTRALE 3D###############################

#EDIFICI VICINI
edificio1 = T([1,2])([55,33])(CUBOID([25,12,7]))
edificio2 = T([1,2])([55,-21])(CUBOID([25,12,7]))
edificio2_superirore = T([1,2,3])([60,-17,7])(CUBOID([10,5,1.5]))
edificio3 = T([1,2])([40,-45])(CUBOID([50,18,12]))
edificio3_superiore = T([1,2,3])([65,-40,12])(CUBOID([20,7,2]))
edifici = STRUCT([COLOR([0.95,0.64,0.37])(edificio1),COLOR([0.95,0.64,0.37])(edificio2),COLOR([0,0.2,0.60])(edificio3),edificio2_superirore,edificio3_superiore])
punti = [[-30,-65],[100,-65],[-30,70],[100,70]]
pianta = JOIN(AA(MK)(punti))
edifici_pianta = STRUCT([edifici,COLOR([0.70,0.70,0.70])(pianta)])

small_area = STRUCT([modello_3D, edifici_pianta])
######################FINE EDIFICI VICINI######################
#Prato
prato_laterale_sx = T([1,2])([55,-5])(CUBOID([25,5,1]))
prato_laterale_dx = T([1,2])([55,24])(CUBOID([25,5,1]))
prato_centrale = T([1,2])([55,9])(CUBOID([25,6,1]))
prati = COLOR([0.1,0.75,0.23])(STRUCT([prato_centrale,prato_laterale_sx,prato_laterale_dx])) #,COLOR([0.1,0.75,0.23])(prati)
#ALBERI
sfera = COLOR([0.133,0.545,0.133])(SPHERE(2)([15,15]))
base_tronco = T([1,2,3])([0.3,0.8,0])(COLOR([0.48,0.10,0.])(CONE([1.2,1.2])(8)))
verts_tronco = [[0,0],[0.5,0],[1,0.5],[1,1],[0.5,1.5],[0,1.5],[-0.5,1],[-0.5,0.5]]
cells_tronco = [[1,2,3,4,5,6,7,8]]
pols_tronco = None
tronco = MKPOL([verts_tronco, cells_tronco, pols_tronco])
chioma1_traslata = T([1,2,3])([0,0,5])(sfera)
chioma2_traslata = T([1,2,3])([1,1,4])(sfera)
chioma3_traslata = T([1,2,3])([2,1,4])(sfera)
chioma4_traslata = T([1,2,3])([-2,2,4])(sfera)
chioma5_traslata = T([1,2,3])([2,-1,4])(sfera)
chioma6_traslata = T([1,2,3])([-1,2,4])(sfera)
chioma7_traslata = T([1,2,3])([1,3,4])(sfera)
chioma8_traslata = T([1,2,3])([-1,-2,4])(sfera)
chiome = STRUCT([chioma8_traslata,chioma7_traslata,chioma6_traslata,chioma5_traslata,chioma4_traslata,chioma3_traslata,chioma2_traslata,chioma1_traslata])
tronco_3D_colorato = COLOR([0.48,0.10,0.])(PROD([tronco, Q(5)]))
albero = STRUCT([chiome, tronco_3D_colorato,base_tronco])
alberi_sx = T([1,2,3])([51,-3,1])(STRUCT(NN(3)([T(1)(8),albero])))
alberi_dx = T([1,2,3])([51,25.5,1])(STRUCT(NN(3)([T(1)(8),albero])))

verde = STRUCT([prati, alberi_dx,alberi_sx])

#LUCI
V,CV = larRod([0.3,0.5])([32,1])
base_lampione = STRUCT(MKPOLS([V,CV]))
V,CV = larRod([0.15,3.0])([32,1])
stecca_lampione = STRUCT(MKPOLS([V,CV]))
V,CV = larBall(0.5)()
luce_lampione = STRUCT(MKPOLS([V,CV]))
lampione = STRUCT([COLOR(BLACK)(base_lampione), COLOR(BLACK)(T(3)(0.5)(stecca_lampione)), COLOR(YELLOW)(T(3)(3.5)(luce_lampione))])
lampione_sx = T([1,2,3])([53,10,1])(STRUCT(NN(3)([T(1)(8),lampione])))
lampione_dx = T([1,2,3])([53,14,1])(STRUCT(NN(3)([T(1)(8),lampione])))

#3d completo senza strande
pratone = STRUCT([small_area,verde, lampione_dx, lampione_sx])

#STRADE
strada_sx = T([1,2])([54,1])(CUBOID([45,7,0.5]))
strada_dx = T([1,2])([54,16])(CUBOID([45,7,0.5]))
strada_larga = T([1,2])([39,-25])(CUBOID([15,95,0.5]))
strada_stretta = T([1,2])([-6,-25])(CUBOID([45,17,0.5]))
strada_finale = T([1,2])([-6,-65])(CUBOID([15,45,0.5]))
strade = COLOR([0.31,0.31,0.31])(STRUCT([strada_sx,strada_dx,strada_larga, strada_stretta,strada_finale]))

#BUS STOP
V,CV = larRod([0.2,4.0])([32,1])
stecca_fermata = STRUCT(MKPOLS([V,CV]))
cartello = CUBOID([0.5,2,2])
bus_stop = COLOR(YELLOW)(STRUCT([stecca_fermata, T([1,3])([-0.25, 2])(cartello)]))

modello_finale = STRUCT([strade, pratone, T([1,2])([-6,-50])(bus_stop)])

VIEW(modello_finale)
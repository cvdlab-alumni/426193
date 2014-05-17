from pyplasm import *
from larcc import *

def merging_elimination_numbering(diagrams,master,toRemove,toMerge) :
	for i in range(len(diagrams)) :
		V,CV = master
		massimo = len(CV)-1 
		master = diagram2cell(diagrams[i],master,toMerge[i])
		V,CV = master 
		for j in range(len(toRemove[i])) :
			toRemove[i][j] += massimo 
		master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove[i])]
	return master 

master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
V,CV = master
toRemove = [13,33,17,37]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]  

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)

toRemove = [[2],[4,10]]
toMerge = [29,34]
diagram1 = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])
diagram2 = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
diagrams = [diagram1,diagram2]

master = merging_elimination_numbering(diagrams,master,toRemove,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)  
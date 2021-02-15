import casefoam
import numpy as np
import math
# directory of the base case
baseCase = 'curvature3D'

# list of parent, child and grandchild names
caseStructure = [['gradAlpha', 'RDF','heightFunction','fitParaboloid'],
                 ['hex'],
                 ['Grid1','Grid2','Grid3','Grid4','Grid5','Grid6','Grid7','Grid8','Grid9','Grid10']]

# dictionarys with data for the caseData dictionary
update_gradAlpha = {
    'constant/transportProperties': {
        'surfaceForces': {'curvatureModel': 'gradAlpha'}}}

update_RDF = {
    'constant/transportProperties': {
        'surfaceForces': {'curvatureModel': 'RDF'}}}


update_heightFunction = {
    'constant/transportProperties': {
        'surfaceForces': {'curvatureModel': 'heightFunction'}}}

update_fitParaboloid = {
    'constant/transportProperties': {
        'surfaceForces': {'curvatureModel': 'fitParaboloid'}}}        

update_hex = dict() #{'system/blockMeshDict': {}} # do nothing

# this function does the same as update_coarse etc but is more elegant
def changeBlockMesh(Nx):
    return {
    'system/blockMeshDict': {
            'blocks': ['hex',
                       [0, 1, 2, 3, 4, 5, 6, 7],
                       '(%s %s %s)' % (Nx,Nx, Nx), 
                       'simpleGrading',
                       '(1 1 1)']}}

res = np.logspace(math.log10(20),math.log10(120),10)
res = res.astype(int)

# dictionary of data to update
caseData = {'gradAlpha': update_gradAlpha,
            'RDF': update_RDF,
            'fitParaboloid': update_fitParaboloid,
            'heightFunction': update_heightFunction,
            'hex': update_hex,
            'Grid1': changeBlockMesh(res[0]),
            'Grid2': changeBlockMesh(res[1]),
            'Grid3': changeBlockMesh(res[2]),
            'Grid4': changeBlockMesh(res[3]),
            'Grid5': changeBlockMesh(res[4]),
            'Grid6': changeBlockMesh(res[5]),
            'Grid7': changeBlockMesh(res[6]),
            'Grid8': changeBlockMesh(res[7]),
            'Grid9': changeBlockMesh(res[8]),
            'Grid10': changeBlockMesh(res[9])
            }

# generate cases
casefoam.mkCases(baseCase,caseStructure, caseData, hierarchy='tree',writeDir='Cases')

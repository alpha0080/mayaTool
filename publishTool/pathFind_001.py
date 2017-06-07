import maya.cmds as cmds

##list = cmds.listConnections('rendermanGeoShape')
#for i in list:
 #   print i

#cmds.nodeType('asd_AlembicNode')

def searchLinkingFile(self):
    linkingFileNode = []
    linkingFilePath = {}
    #search Dict ,   mesh,transform,shadingEngine
    linkingSearchDict = {
                          'PxrTexture':'filename',
                          'file':'fileTextureName',
                          'AlembicNode':'abc_File',
                          'gpuCache':'cacheFileName',
                          'RenderManArchive':'filename'}

    for nodeType in linkingSearchDict.keys():
        #return i
        
        getNodes = cmds.ls(typ = nodeType)
        #print nodeType
        
        for node in getNodes:
            
            linkingFileNode.append( node + '.' + linkingSearchDict[nodeType])
    #print linkingFilePath
    
    for i in linkingFileNode:
        
        fileLocation = cmds.getAttr(i)
        linkingFilePath.update({i:fileLocation})
        
    print linkingFilePath

    
searchLinkingFile('a')

    
    
    
    
    
    

cmds.getAttr('PxrTexture1.filename')
cmds.getAttr('file1.fileTextureName')
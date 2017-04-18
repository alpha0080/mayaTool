import maya.cmds as cmds
import pymel.core as pm

totalParticleCount = pm.nParticle('nParticle1', query=True, ct=True)


particlePositionDict={}

for n in range(0,totalParticleCount):
    perParticle = 'nParticleShape1.pt[%s]'%str(n)
    positionPP = cmds.getParticleAttr(perParticle, at='position',a =True)
    particlePositionDict.update({str(n):positionPP})


for n in range(0,totalParticleCount):
    newName = 'instanceObj' + str(n)
    newInstanceObj = cmds.duplicate( 'pSphere1', n=newName )
    cmds.setAttr( "%s.translateX"%newName,particlePositionDict[str(n)][0])
    cmds.setAttr( "%s.translateY"%newName,particlePositionDict[str(n)][1])
    cmds.setAttr( "%s.translateZ"%newName,particlePositionDict[str(n)][2])
    #print newName ,n,particlePositionDict[str(n)][0]
    

   # cmds.parent(instranceGrpName,newInstanceObj)
   
#cmds.setAttr('instanceObj0.translateX',3)
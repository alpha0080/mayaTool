import maya.utils 
import maya.cmds
import pymel.core as pm
import datetime,json

import maya.utils as utils
import threading
##testC
import math,numpy

openFileName  = "C:/mayaProjs/testProj/data/particleToolCache/nParticle1_v001.json"
dataName = open(openFileName,'r')
data = json.load(dataName)  
res={}	
resA={}
resB={}
def do_in_main():
    rotateNormalx = data[str(key)][3]
    rotateNormaly = data[str(key)][4]
    rotateNormalz = data[str(key)][5]  
                    
    rotX=numpy.deg2rad(numpy.arctan2(rotateNormaly,rotateNormalz))   
    rotX=numpy.deg2rad(numpy.arctan2(rotateNormalx,rotateNormalz))         
      
   # rotX = math.degrees(math.atan2(rotateNormaly,rotateNormalz))
    #rotY = math.degrees(math.atan2(rotateNormalx,rotateNormalz))
    res.update({key:(rotX,rotY)})

def do_in_mainB():
    rotateNormalx = data[str(key+2500)][3]
    rotateNormaly = data[str(key+2500)][4]
    rotateNormalz = data[str(key+2500)][5]  
                    
                    
    rotX = math.degrees(math.atan2(rotateNormaly,rotateNormalz))
    rotY = math.degrees(math.atan2(rotateNormalx,rotateNormalz))
    res.update({(key+2500):(rotX,rotY)})
    
td = datetime.datetime.now() - st 
print("\t[Info] Spending time={0}!".format(td))    
for key in range(0,100):
    
    t  = threading.Thread(target=do_in_main, args=())
    #t2  = threading.Thread(target=do_in_mainB, args=())

    t.start()
    #t2.start()
td = datetime.datetime.now() - st 
print("\t[Info] Spending time={0}!".format(td))     





def doSphere( radius ):
	maya.cmds.sphere( radius=radius )
	
##test A	
openFileName  = "C:/mayaProjs/testProj/data/particleToolCache/nParticle1_v001.json"
dataName = open(openFileName,'r')
data = json.load(dataName)  	
res={}
def doJob(key):   

    #print key
    rotateNormalx = data[str(key)][3]
    rotateNormaly = data[str(key)][4]
    rotateNormalz = data[str(key)][5]  
                    
                    
    rotX = math.degrees(math.atan2(rotateNormaly,rotateNormalz))
    rotY = math.degrees(math.atan2(rotateNormalx,rotateNormalz))
    res.update({key:(rotX,rotY)})
    #print rotX,rotY
 

 
for key in range(0,5000):
    maya.utils.executeInMainThreadWithResult( doJob, key)
    td = datetime.datetime.now() - st 
    print("\t[Info] Spending time={0}!".format(td))
    
    
    
    
    if key == 0:
        print("\t[Info] Spending time={0}!".format(td))
    else:
        pass
    if key == 4999:
        print("\t[Info] Spending time={0}!".format(td))
    else:
        pass
    
    
    


#test B
openFileName  = "C:/mayaProjs/testProj/data/particleToolCache/nParticle1_v001.json"
dataName = open(openFileName,'r')
data = json.load(dataName)  
res={}

td = datetime.datetime.now() - st 
print("\t[Info] Spending time={0}!".format(td))
for key in range(0,5000):

    rotateNormalx = data[str(key)][3]
    rotateNormaly = data[str(key)][4]
    rotateNormalz = data[str(key)][5]  
                    
                    
    rotX = math.degrees(math.atan2(rotateNormaly,rotateNormalz))
    rotY = math.degrees(math.atan2(rotateNormalx,rotateNormalz))
    rotX*rotY
    
    
    res.update({key:(rotX,rotY)})



   # maya.utils.processIdleEvents( doJob, f)
    
td = datetime.datetime.now() - st 
print("\t[Info] Spending time={0}!".format(td)) 



st = datetime.datetime.now()  
  
for f in range(5,20):
    doJob(f)
    
td = datetime.datetime.now() - st 
print("\t[Info] Spending time={0}!".format(td)) 



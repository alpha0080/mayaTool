import maya.cmds as cmds

class publishFileState:
    
    def __init__(self,keyFileName):
        
        self.keyFileName = keyFileName
        
    def ribArchiveReOrg(self,ribArchiveName):
        cmds.createNode('gpuCache',n =ribArchiveName +')
        #put the ribArchive into GpuCache Transform
        #ex.   gpuCacheTransform>
        
    def key_pyblishFile(self):
        #typical fileName = projInt_assetTypeInit_assetName_assetProcessInit_master.mb
        #example: ow_cf_c_angelFish_mod_master.mb
        
        self.typicalPublishDateDict ={'key_publishFile':{'projectWorkSpace':'workSpace',
                                                         'fileName':'fullFilePath',
                                                         'fileIcon':'fullIconPath',
                                                         'ribArchive':{'ribArchivePath':{'high':{},'mid':{},'mid':{}},
                                                                       'parentGPUCache':{'high':{},'mid':{},'mid':{}},
                                                                       'startFrame':{},
                                                                       'endFrame':{},
                                                                       'frameRate':{},
                                                                       'isMotionBlur':{}},                                                       
                                                         'gpuCache':'gpuCachePath',
                                                         'publishTime':'time',
                                                         'metaData':{},
                                                         'user':'userName'}}
        
    def addPublishFileAnnounceInfoToAssembleFile(self,assetOrShot,assetClass,assetNow,processNow):
        #self.projectAssembleDescriptionFile
        if isAsset == True :
            self.projectAssembleDescriptionFile['assets'][assetClass][assetNow][assetNow +'.'+assetClass].update({processNow:{self.typicalPublishDateDict['key_publishFile']}})
        else:
            self.projectAssembleDescriptionFile['shot'][assetNow][assetNow].update({processNow:{self.typicalPublishDateDict['key_publishFile']}})

                    
                              
                              
    def publishFileAnnounceDict(self):
        
        fileName = self.root +'/' +self.project +'/' +'publish' +'/' +'global' +'/' +self.project + '_publishAnnonce.json'
        f = open(fileName,'w')        
        data = json.dumps(typicalPublishDateDict, sort_keys=True , indent =4)
        f.write(data)
        f.close
        
        
        

     
        
    def printOut(self):
        
        print 'fileName:', self.keyFileName
        


aa= publishFileState('asd')

aa.printOut()

    
    

def run(self):
    self.buildPublishDescriptionDictStructure()
    self.output()
    

def buildPublishDescriptionDictStructure(self):
    self.projPubishDescriptionDict = {'projName':{'asset':{'character':{'chaA':[{'fileName':'fileParh'},{'fileIcon':'iconPath'},{'ribArchive':'ribPath'},{'fileData':'publlishTime'},{'fileDescription':''}],
                                                                   'chaB':[],
                                                                   'chaC':[]},
                                                        'vehicle':{'vehicleA':[],
                                                                   'vehicleB':[],
                                                                   'vehicleC':[],
                                                                   'vehicleD':[]},
                                                         'set':{'setA':[],
                                                                'setB':[],
                                                                'setC':[],
                                                                'setD':[]},
                                                        'prop':{'propA':[],
                                                                'propB':[],
                                                                'propC':[]},
                                                        'other':{'otherA':[],
                                                                 'otherB':[]}
                                                        },
                                                'shot':{'shot01':[],
                                                        'shot02':[],
                                                        'shot03':[],
                                                        'shot04':[]}
                                                }
                                    }


def publishFileStateKey(self):
    fileStateKey=[{'fileName':'fileParh'},
                  {'fileIcon':'iconPath'},
                  {'ribArchive':'ribPath'},
                  {'fileData':'publlishTime'},
                  {'fileDescription':''}]       
    
    
    
    
                                       

aa= json.dumps(assetName, sort_keys=True , indent =4)  
pprint(aa) 
import json ,pprint


                                                                   
def output(self):
    print self.projPubishDescriptionDict
    

run('test')
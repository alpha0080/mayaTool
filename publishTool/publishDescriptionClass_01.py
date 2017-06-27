

class publishFileState:
    
    def __init__(self,keyFileName):
        
        self.keyFileName = keyFileName
        
    def fileState(self):
        #typical fileName = projInt_assetTypeInit_assetName_assetProcessInit_master.mb
        #example: ow_cf_c_angelFish_mod_master.mb
        
        typicalDict ={{'projectWorkSpace':'workSpace'},
                      {'fileName':'fullFilePath'},
                      {'fileIcon':'fullIconPath'},
                      {'ribArchive':{'ribArchivePath':{'high':{},
                                                       'mid':{},
                                                       'low':{}},
                                     'parentGpu':{'high':{},
                                                  'mid':{},
                                                  'low':{}},
                                     'startFrame':{},
                                     'endFrame':{},
                                     'frameRate':{},
                                     'isMotionBlur':{}}
                      {'gpuCache':'gpuCachePath'},
                      {'publishTime':'time'},
                      {'metaData':{}},
                      {'user':'userName'}
                      }
                      
        
        
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
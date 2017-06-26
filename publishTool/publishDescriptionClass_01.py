
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
                                                        
                                                                   
def output(self):
    print self.projPubishDescriptionDict
    

run('test')
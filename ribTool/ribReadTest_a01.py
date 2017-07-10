import os
import zipfile

class editRibArchive:
    
    def __init__(self):
        self.ribArchiveRootFolder = 'C:/mayaProjs/output/renderman/ribarchives/'
    
    def classTest(self,test):       
        print test
       
    def runEditRibArchiveMain(self,ribArchiveName):
        self.ribArchiveName = ribArchiveName
        print self.ribArchiveName 
        
        self.getRibArchiveDefine()
        
        print 'self.ribArchiveRootFolder',self.ribArchiveRootFolder
        print 'self.ribArchiveFolder',self.ribArchiveFolder
        print 'self.ribArchiveZipName',self.ribArchiveZipName
        print 'self.ribArchiveRiPassJobFile',self.ribArchiveRiPassJobFile
        print 'self.RIBManifest',self.RIBManifest
        print 'self.ribArchiveRlfName',self.ribArchiveRlfName
        self.openZipFile()

    def getRibArchiveDefine(self):
      #  print ribArchiveName
        
        self.ribArchiveFolder = self.ribArchiveRootFolder +'/' +self.ribArchiveName
        self.ribArchiveZipName = self.ribArchiveRootFolder +'/' +self.ribArchiveName +'/' +self.ribArchiveName +'.zip'
        self.ribArchiveRiPassJobFile = 'renderman/ribarchives/' + self.ribArchiveName +'/' + self.ribArchiveName + '.job.rib'  #in zip file
        self.tempribArchiveRiPassJobFile = self.ribArchiveRootFolder +'/' +self.ribArchiveName +'/' + self.ribArchiveName + '.job.rib'
        self.RIBManifest = 'renderman/RIBManifest.json' #in zip file
        self.ribArchiveRlfName = self.ribArchiveRootFolder +'/' + self.ribArchiveName +'/' + self.ribArchiveName +'.job.rlf'
        #ribArchiveSequenceRlfName = ribArchiveRootFolder +'/' +ribArchiveName +'/' +ribArchiveName + seqNum +'.job.rlf'

    def openZipFile(self):
        print self.ribArchiveZipName
        z = zipfile.ZipFile(self.ribArchiveZipName, "r")
        for i in z.namelist():
            print i        
        data = z.read(self.ribArchiveRiPassJobFile,'r')
        z.close
        
       # print data
        tempRibArchiveRiPassJobInfoList = []
        for i in data.split('\n'):
            tempRibArchiveRiPassJobInfoList.append(i)
            
        f = open(self.tempribArchiveRiPassJobFile,'w')
            
       # print tempRibArchiveRiPassJobInfoList 
        
        #z= zipfile.ZipFile(self.ribArchiveZipName, "a")
        #f=z.open(self.ribArchiveRiPassJobFile,'w')
        #print f.read()
        for i in tempRibArchiveRiPassJobInfoList:
            f.write(i+'\n')
        f.write('#test by alpha'+'\n')
        f.write('#test ribArchive edit job.zip'+'\n')
        f.close
     
        z = zipfile.ZipFile(self.ribArchiveZipName, "w")
        z.write(self.tempribArchiveRiPassJobFile,self.ribArchiveRiPassJobFile,zipfile.ZIP_DEFLATED)
        z.close

        
        #f.close

       # z.close
            


a = editRibArchive()  
a.runEditRibArchiveMain('rrrRibArchiveShape')




runEditRibArchiveMain(self)

def editRibArchiveJob(jobFileName):
    dataList= []
    f= open(jobFileName,'r')
    data = f.read()
    for i in data.split('\n'):
        dataList.append(i)
        
    f.close
    print jobFileName.split('/')
    exportFileName = 'C:/mayaProjs/output/renderman/ribarchives/rrrRibArchiveShape/writeOnTest_01.txt'
    writeNewRibArchiveJob(dataList,exportFileName)
    
def writeNewRibArchiveJob(dataList,exportFileName):
    print dataList
    print exportFileName
    f= open(exportFileName,'w')
    for i in dataList:
        
        f.write(i+'\n')
        
    f.close
    
    


editRibArchiveJob('C:/mayaProjs/output/renderman/ribarchives/rrrRibArchiveShape/rrrRibArchiveShape.job.rib')
    ribArchiveName = 'rrrRibArchiveShape'


fileName = 'C:/mayaProjs/output/renderman/ribarchives/rrrRibArchiveShape/rrrRibArchiveShape.job.rib'

dataList = []
f = open(fileName,'r')
for i in f.read().split('\n'):
    dataList.append(i)
f.close


print dataList
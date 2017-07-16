import os
import zipfile
import json


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
        
        
    def replaceFileInZip(self,ribArchiveName):
        ##zipFileName = 'C:/mayaProjs/output/renderman/ribarchives/CubeTTTRibArchiveShape/CubeTTT.zip'
        #extractPath = 'C:/mayaProjs/output/renderman/ribarchives/CubeTTTRibArchiveShape/temp'
        projectRoot = 'c:/mayaProjs/output'
        rendermanWorkspace = 'renderman/ribarchives'
        selectZipFileFullName = projectRoot + '/' + rendermanWorkspace +'/' +ribArchiveName +'/' +ribArchiveName+'.zip'
        jsonFileName = 'RIBManifest.json'
        jobRibFilePath = '/renderman/ribarchives' + '/' + ribArchiveName
        jibRibFileList = []
        zin = zipfile.ZipFile(selectZipFileFullName,'r')         #讀取選定的Zip File
        jsonData = zin.read(jsonFileName)
        rlfFileList=[]
       # rlfSingleFileName = projectRoot + '/' + rendermanWorkspace +'/' + ribArchiveName + countNume + '.rlf'
        #data = json.dumps(jsonData, sort_keys=True)  #編譯成json 且賦予格式 控四格
        data = json.loads(jsonData)

        zin.close
       # print jsonData #the original data from zipfile，look like json format, but str
       # print data
        #print data.keys()
        ##print data['Driver-Files'].keys()
        #ribFileCount = len(data['Driver-Files'].keys())
        #print ribFileCount
        tempDriveFilesKeys =[]
        if len(data['Driver-Files'].keys()) >1:
            for i in data['Driver-Files'].keys():
                tempDriveFilesKeys.append('%04d'%int(i))
                
                
            for i in sorted(tempDriveFilesKeys):
                rlfSingleFileName = projectRoot + '/' + rendermanWorkspace +'/' + ribArchiveName + '.%04d'%int(i) + '.rlf'
                rlfFileList.append(rlfSingleFileName)
                jobRibFileName = jobRibFilePath + '/' +ribArchiveName + '.%04d'%int(i) +'.rib'
                jibRibFileList.append(jobRibFileName)
        else:
            rlfSingleFileName =  projectRoot + '/' + rendermanWorkspace +'/' + ribArchiveName + '.job.rlf'
            jobRibFileName =  jobRibFilePath + '/' +ribArchiveName + '.job.rib'
            rlfFileList.append(rlfSingleFileName)
            jibRibFileList.append(jobRibFileName)

        #    print rlfSingleFileName
        print rlfFileList
        print jobRibFilePath
        print jibRibFileList
         #  print i
       # print '%04d'%ribFileCount
        
a = editRibArchive()
a.replaceFileInZip('pSphereOOORibArchiveShape')


'''
    def ssss(self):
        
        your_delet_file=['RIBManifest.json','asd.txt']  #in zip file
        old_zipfile= zipFileName #新文件
        new_zipfile= zipFileName.split('.')[0]+'_2.zip' #新文件
        zin = zipfile.ZipFile (old_zipfile, 'r') #?取?象
        zout = zipfile.ZipFile (new_zipfile, 'w') #被?入?象
        for item in zin.infolist():
            buffer = zin.read(item.filename)
            if (item.filename!= your_delet_file):  #剔除要?除的文件
                zout.writestr(item, buffer) #把文件?入到新?象中
        zout.close()
        zin.close()
 
        #用新文件覆??文件
        shutil.move(new_zipfile,old_zipfile)




        
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
'''
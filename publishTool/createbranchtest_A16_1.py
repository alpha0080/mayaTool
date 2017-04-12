import os,json

currentProject = "//mcd-server/art_3d_project/3d_pipeline_test/shot/shot_02/lighting/"   

topLevelDirFileSearch = currentProject + "scenes"

topLevelDirList = ['master']
branchPreDict = {"0":{"master":{}}}        

print "check point 01"


#build topLevelDir List------------------------------------------------------------------

for dir,path,file in os.walk(topLevelDirFileSearch):

    allDir = dir.split(topLevelDirFileSearch)[1]

    try:

        if allDir.split("\\")[1] in topLevelDirList:
            pass
        else:
            topLevelDirList.append(allDir.split("\\")[1])
        
    except:
        pass



for i in range(0,len(topLevelDirList)):
   # print i
    branchPreDict.update({str(i):{topLevelDirList[i]:{}}})

#------analyze 2nd level dir and files-------------------
#----------1.for i in branchPreDict.keys(): get search folder from branchPreDict dictionary, make sure index and branch name match
#-------------2.for secLevelItem in os.listdir(secLevelDirSearch):, update 2nd level item into branchPreDict
#----------------3 for thirdLevelItem in os.listdir(thirdLevelDirSearch):, update 3rd level item into branchPreDict
#--------------------4. for fourLevelItem in os.listdir(fourLevelDirSearch): update 4th level item into branchPreDict ,only folder
#--------------os.path.isdir(path),check the path is folder or file
for i in branchPreDict.keys():
    secLevelDirSearch = topLevelDirFileSearch+ '/' + branchPreDict[i].keys()[0]  
    
    branchPreDict[i][branchPreDict[i].keys()[0]].update({'folder':{}})
    branchPreDict[i][branchPreDict[i].keys()[0]].update({'file':{}})
    for secLevelItem in os.listdir(secLevelDirSearch):
        thirdLevelDirSearch = topLevelDirFileSearch+ '/' + branchPreDict[i].keys()[0]+'/'+ secLevelItem       
        if os.path.isdir(thirdLevelDirSearch) == True:
            branchPreDict[i][branchPreDict[i].keys()[0]]['folder'].update({secLevelItem:{}})
            
            
        else:
            branchPreDict[i][branchPreDict[i].keys()[0]]['file'].update({secLevelItem:[]})

        
        
        if os.path.isdir(thirdLevelDirSearch) == True:
            branchPreDict[i][branchPreDict[i].keys()[0]]['folder'][secLevelItem].update({'folder':{}})
            branchPreDict[i][branchPreDict[i].keys()[0]]['folder'][secLevelItem].update({'file':{}})
            
            for thirdLevelItem in os.listdir(thirdLevelDirSearch):

                fourLevelDirSearch = thirdLevelDirSearch +'/'+ thirdLevelItem

                
                if os.path.isdir(fourLevelDirSearch) == True:
                    branchPreDict[i][branchPreDict[i].keys()[0]]['folder'][secLevelItem]['folder'].update({thirdLevelItem:{}})
                    branchPreDict[i][branchPreDict[i].keys()[0]]['folder'][secLevelItem]['folder'][thirdLevelItem].update({'file':{}})
                else:
                    branchPreDict[i][branchPreDict[i].keys()[0]]['folder'][secLevelItem]['file'].update({thirdLevelItem:[]})   

                    
                if os.path.isdir(fourLevelDirSearch) == True:
                    for fourLevelItem in os.listdir(fourLevelDirSearch):
                        print fourLevelItem
                        branchPreDict[i][branchPreDict[i].keys()[0]]['folder'][secLevelItem]['folder'][thirdLevelItem]['file'].update({fourLevelItem:[]}) 
                    
                                

data = json.dumps(branchPreDict, sort_keys=True , indent =4)
print data
    



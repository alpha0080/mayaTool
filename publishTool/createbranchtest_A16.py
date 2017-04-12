import os

currentProject = "//mcd-server/art_3d_project/3d_pipeline_test/shot/shot_02/lighting/"   

topLevelDirFileSearch = currentProject + "scenes"

topLevelDirList = ['master']
branchPreDict = {"0":{"master":{}}}        

print "check point 01"


#build topLevelDir List------------------------------------------------------------------

for dir,path,file in os.walk(topLevelDirFileSearch):
    #print dir,path,file
    allDir = dir.split(topLevelDirFileSearch)[1]
    print allDir
    try:
      #  print allDir.split("\\")[1]
        if allDir.split("\\")[1] in topLevelDirList:
            pass
        else:
            topLevelDirList.append(allDir.split("\\")[1])
        
    except:
        pass

#print "check point 02"

# print topLevelDirList

#find topLevelDir Count ,searching real dir

#build topLevelDir in full dictionary-----------------------------------------------------------


for i in range(0,len(topLevelDirList)):
   # print i
    branchPreDict.update({str(i):{topLevelDirList[i]:{}}})

#------analyze 2nd level dir and files-------------------
#----------1.for i in branchPreDict.keys(): get search folder from branchPreDict dictionary, make sure index and branch name match
#-------------2.for secLevelItem in os.listdir(secLevelDirSearch):, update 2nd level item into branchPreDict
#----------------3 for thirdLevelItem in os.listdir(thirdLevelDirSearch):, update 3rd level item into branchPreDict
#--------------------4. for fourLevelItem in os.listdir(fourLevelDirSearch): update 4th level item into branchPreDict ,only folder
for i in branchPreDict.keys():
    secLevelDirSearch = topLevelDirFileSearch+ '/' + branchPreDict[i].keys()[0]  
    
    if os.path.isdir(secLevelDirSearch) == True:
        print secLevelDirSearch + "    is branch folder"
        
    else:
        print secLevelDirSearch + "    is branch file"

    
    for secLevelItem in os.listdir(secLevelDirSearch):
        branchPreDict[i][branchPreDict[i].keys()[0]].update({secLevelItem:{}})
        thirdLevelDirSearch = topLevelDirFileSearch+ '/' + branchPreDict[i].keys()[0]+'/'+ secLevelItem       
        # check item is or not branch folder        

        try:
            for thirdLevelItem in os.listdir(thirdLevelDirSearch):
                #print thirdLevelItem
                branchPreDict[i][branchPreDict[i].keys()[0]][secLevelItem].update({thirdLevelItem:{}})
                
                fourLevelDirSearch = thirdLevelDirSearch + '/' + thirdLevelDirSearch
                
                try:
                    for fourLevelItem in os.listdir(fourLevelDirSearch):
                        #print fourLevelItem
                        branchPreDict[i][branchPreDict[i].keys()[0]][secLevelItem][thirdLevelItem].update({fourLevelItem:{}})
                    
                except:
                    pass
                
           
        except:
            pass
            
    
    

    
    
    




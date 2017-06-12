
import json
from pprint import pprint


fileName = 'C:/mayaProjs/ani_pop_v01_cf/global/shot/shot02/shot02_lighting.json'
with open(fileName) as data_file:    
    data = json.load(data_file)
    
bb= {'1': {u'g': {u'dgdg': {u'gg': {}}}}, '0': {'master': {}}}   

print data.keys()

#dd= {u'0': {u'master': {}}, u'1': {u'g': {}}} 


#indexNum = sorted(data.keys())
#print indexNum
branchInfoDict = {'0':{'master':{}}}
#branchInfoDict = {}
for i in range(1,len(data.keys())):
    top = data[str(i)].keys()[0]
   # print top
    branchInfoDict.update({str(i):{top:{}}})
    #print i,top,data[str(i)][top]['folder'].keys()
    for sec in data[str(i)][top]['folder'].keys():
      #  print sec
       # branchInfoDict[str(i)][top]
        branchInfoDict[str(i)][top].update({sec:{}})
        
        for third in data[str(i)][top]['folder'][sec]['folder'].keys():
           #     print i,top,sec, data[str(i)][top]['folder'][sec]['folder'].keys()
          #  print data[str(i)][top]['folder'][sec]['folder']
         #   print str(i),top,sec,third
            branchInfoDict[str(i)][top][sec].update({third:{}})




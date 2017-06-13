
import json
from pprint import pprint


fileName =  "//mcd-server/art_3d_project/ani_pop_v01_cf/global/assets/character/bear/bear_model.json"
with open(fileName) as data_file:    
    data = json.load(data_file)
    
branchDict={'1': {u'g2': {u'g22': {u'c2': {}}}}, '0': {'master': {}}, '2': {u'h2': {}}}

cc= {'0': {'master': {}}, '1': {u'g2': {u'g22': {u'c2': {}}}}, '2': {u'h2': {}}} 


print branchDict['1']['g2'].keys()
print cc['1']['g2'].keys()



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




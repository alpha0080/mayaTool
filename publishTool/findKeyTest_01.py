import json
from pprint import pprint

fileName = "C:/mayaProjs/3d_pipeline_test/global/shot/shot_02/shot_02_lighting.json"

with open(fileName) as data_file:    
    data = json.load(data_file)

pprint(data)

print data.keys()

for k, v in data.items():
    for k1, v1 in v.items():
        print(k1)
        
        
for i in data['4'].items():
    print i
    
    
len(data.items())
len(data.keys())


def checkItem(dict,key):
   # for i in range(0,len(data.items())):
       # print data[i]
    print dict[key]
        
for i in data.keys():
    checkItem(data,i)

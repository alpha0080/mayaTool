
import json
from pprint import pprint


fileName = "//mcd-server/art_3d_project/ani_pop_v01_cf/global/assets/character/chicken/chicken_model.json"

with open(fileName) as data_file:    
    data = json.load(data_file)
    
bb= {'1': {u'g': {u'dgdg': {u'gg': {}}}}, '0': {'master': {}}}   



dd= {u'0': {u'master': {}}, u'1': {u'g': {}}} 
print dd['1'].keys()
print bb['1'].keys()



cc= {}
print cc.keys()
for top in data.keys():
    print 'top',top,type(top)
    print data[top]
    cc.update({top:{}})
    print 'data[top].keys()',data[top].keys()
    for sec in data[top].keys():
        cc.update({top:{data[top][sec}})
        



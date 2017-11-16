#fileDescription


alpheBetaCharacterDict = {"1":"a",
                          "2":"b",
                          "3":"c",
                          "4":"d",
                          "5":"e",
                          "6":"f",
                          "7":"g",
                          "8":"h",
                          "9":"i",
                          "10":"j",
                          "11":"k",
                          "12":"l",
                          "13":"m",
                          "14":"n",
                          "15":"o",
                          "16":"p",
                          "17":"q",
                          "18":"r",
                          "19":"s",
                          "20":"t",
                          "21":"u",
                          "22":"v",
                          "23":"w",
                          "24":"x",
                          "25":"y",
                          "26":"z"}


#a= 23
#print '%04d'%a
import json
fileNameDict={}
fileName = 'c:/temp/fileNameTest.json'
assetIndex={"asset0000":""}
assetData = {"itemName":{"aaaaaaaaaaaaaa":""},
             "usedInProject":{"bbbbbbbbbbbbbb":""},
             "ZBrush":{"ccccccccccc":""},
             "mudbox":{"ddddddddddd":""},
             "substancePainter":{"eeeeeeeeeee":"","ffffffffffff":"","ggggggggggg":""},
             "scenes":{"hhhhhhhhhhhhh":"","iiiiiiiiiiiiiii":"","kkkkkkkkkkkkk":""},
             "sourceimages":{"lllllllllllll":"","llllllllllll":"","nnnnnnnnnnnnnn":""},
             "fbx":{"ooooooooooo":"","pppppppppp":"","qqqqqqqqqq":""},
             "obj":{"rrrrrrrrr":"","sssssssssss":"","tttttttttttttt":""},
             "data":{"uuuuuuuuu":"","vvvvvvvvvvvv":"","wwwwwwwwwwwwwwww":""},
             "label":{"aaa1":"","aaa2":"","aaa3":"","aaa4":"","aaa5":"","aaa6":""},
             "keyword":{"asd":"","dfdf":"","sdfdsf":"","ds":"","sdfdsfe":"","fhfgh":""}}
             
             
for i in range(0,99999):
    #itemName = 
    fileNameDict.update({'%04d'%i:assetIndex})
    
#f= open(fileName,'w')
#json.dumps(fileNameDict, sort_keys=True , indent =4)  

#f.write(fileNameDict)
#f.close
with open(fileName, 'w') as f:
    json.dump(fileNameDict, f)
    
    
print fileNameDict["82449"]
    

import json

fileName = "C:/mayaProjs/3d_pipeline_test/global/shot_02_lighting.json"

with open(fileName, 'r') as f:
    
    data = json.load(f)

data['1']




import os

folder = "C:/mayaProjs/3d_pipeline_test/global/shot"

os.path.isdir(folder) == True

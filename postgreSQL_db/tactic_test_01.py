import getTacticData ,json
print "run getDataFromTactic start"
publishConfigFile = '//mcd-one/database/assets/scripts/maya_scripts/publishToolConfig.json'

with open(publishConfigFile, 'r') as f:
    publishToolSettingData = json.load(f)

scripts_path = "//mcd-one/database/assets"
sys.path.append(scripts_path +  "/client")
sys.path.append(scripts_path + "/scripts/tactic_scripts/ui")

tacticHostName = publishToolSettingData['tacticHostName']
tacticHostIP = publishToolSettingData['tacticHostIP']
loginID = publishToolSettingData['tacticID']
loginPW = publishToolSettingData['tacticPW']
root = publishToolSettingData['root']
fileTypeFillet = publishToolSettingData['fileTypeFillet']

import getTacticDataC
reload(getTacticDataC)


tactic = getTacticDataC.connectToTactic(tacticHostName,tacticHostIP,loginID,loginPW)

userInfo =  tactic.runTactic('user')
userInfo[0].keys()
for i in userInfo:
    print i['display_name'],i['department'],i['section']
    


print 'adsadsads \n bbbbb'
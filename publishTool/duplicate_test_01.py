from shutil import copyfile
import os,sys
import maya.cmds as cmds

copyfile(src, dst)

srcFolder = 'c:/temp/test/src'
dstFolder = 'c:/temp/test/dst'



for i in os.listdir('c:/temp/test/src'):
    print i
    
    
    
projectName/publish/assets/character
                          /vehicle
                          /set
                          /prop
                          /other
                   /shot
                         
                         
                         
publishFolderRequest ={ 'publish':{'assets':{'character':{},
                                             'vehicle':{},
                                             'set':{},
                                             'prop':{},
                                             'other':{}
                                             },
                                   'shot':{'shot01':{},
                                           'shot02':{}
                                           }
                                   }}
                                             
                                             
publishFolderRequest['publish']['assets']                                                    